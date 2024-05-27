# Libraries

import time
import numpy as np


# Selenium imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# PyAutoGUI imports
import pyautogui as pag

# Image processing imports
from PIL import ImageGrab
import cv2
from fer import FER

# GUI
import tkinter as tk
from tkinter import simpledialog


# Asking for URL & password
def get_meeting_details():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    meeting_url = simpledialog.askstring("Meeting URL", "Enter the Zoom meeting URL:")
    meeting_passcode = simpledialog.askstring("Meeting Passcode", "Enter the Zoom meeting passcode (if any):")

    root.destroy()
    return meeting_url, meeting_passcode

URL , passcode = get_meeting_details()

# Ask user for URL:
#URL = str(input("Ingrese link de zoom meeting:"))


################################ Initialize WebDriver ################################
driver = webdriver.Chrome()
driver.maximize_window()

driver.get(URL)

print("Driver initialized...")


# ACTIONS:

#FIRST ACTION: press enter key
print("Opening zoom site:...")
pag.press('enter')

time.sleep(2)

#SECOND ACTION: press button 'Launch Meeting'
#print("Second action: click launch meeting...")

launch_button = driver.find_elements(By.XPATH, '//*[@id="zoom-ui-frame"]/div[2]/div/div[1]/div')
launch_button[0].click()

time.sleep(2)

#THIRD ACTION: press enter key
#print("Third action: click enter")
pag.press('enter')

time.sleep(3)

#FOURTH ACTION: click on 'Join from your Browser
print("Joining via browser...")

join_browser_button = driver.find_elements(By.XPATH, '//*[@id="zoom-ui-frame"]/div[2]/div/div[2]/h3[2]/span/a')
join_browser_button[0].click()

time.sleep(5)

#FIFTH ACTION: disabling audio
print("Disabling audio...")
pag.press('esc')


#SIXTH ACTION: write bot name
print('Completing bot name...')

driver.switch_to.frame(driver.find_element(By.TAG_NAME ,"iframe"))

name_box = driver.find_element(By.XPATH, '//*[@id="input-for-name"]')
name_box.clear()
name_box.send_keys('Empathic Zoom v1')

#driver.switch_to.default_content()
time.sleep(3)

#SEVENTH ACTION: join zoom call
print('Joining call..')
pag.press('enter')

time.sleep(10)

#EIGTH ACTION: disabling audio
print("Disabling audio...")
pag.press('esc')

time.sleep(2)
pag.press('esc')

#NINETH ACTION: Swtich to Gallery view
print('Opening Gallery view..\n')  
time.sleep(2)

# Move the mouse to the top of the screen to make the controls visible
actions = ActionChains(driver)
actions.move_by_offset(10, 10).perform()

# Wait until the "View" button is visible and clickable
print('Waiting for the "View" button to be visible and clickable...\n')
wait = WebDriverWait(driver, 10)
view_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='full-screen-widget__toggle-text' and contains(text(), 'View')]")))

# Click the "View" button to open the view options

view_button.click()

# Press 'down' and 'enter' to switch to gallery view
actions.send_keys(Keys.DOWN).perform()
actions.send_keys(Keys.ENTER).perform()
print("Gallery view active.\n")



################################ Emotions functions ################################

print("Bot is ready to detect emotions...\n")

detector = FER(mtcnn=True)

print("\n Tensorflow loaded...\n")

def analyze_emotions(image):
    # Detect emotions
    emotions = detector.detect_emotions(image) #returns a list of emotions for each face detected. 
    print(emotions)
    return emotions

def get_strongest_emotion(emotions):
    if not emotions:
        return None

    # Calculate average emotion vector
    avg_emotions = {}
    for emotion in emotions:
        for key, value in emotion['emotions'].items():
            if key not in avg_emotions:
                avg_emotions[key] = 0
            avg_emotions[key] += value
    for key in avg_emotions:
        avg_emotions[key] /= len(emotions)

    # Determine the strongest emotion
    strongest_emotion = max(avg_emotions, key=avg_emotions.get)
    return strongest_emotion


def capture_screen():
    # Capture the screen
    screen = ImageGrab.grab()
    screen_np = np.array(screen)
    # Convert RGB to BGR
    screen_bgr = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)
    return screen_bgr



################################ Exploring different ways to display the strongest emotion on screen ################################

def get_traffic_light_color(emotion):
    positive_emotions = ['happy', 'surprise']
    neutral_emotions = ['neutral']
    #negative_emotions = ['sad', 'angry', 'disgust', 'fear']

    if emotion in positive_emotions:
        return 'Green'
    elif emotion in neutral_emotions:
        return 'Yellow'
    else:
        return 'Red'

def update_status_label(emotion, num_faces):
    if emotion:
        traffic_light_color = get_traffic_light_color(emotion)
        status_label.config(text=f'Strongest Emotion: {emotion}\nNumber of Faces: {num_faces}', bg=traffic_light_color)
    else:
        status_label.config(text='No faces detected', bg='Gray')

def analyze_and_update():
    screen = capture_screen()
    emotions = analyze_emotions(screen)
    num_faces = len(emotions)
    strongest_emotion = get_strongest_emotion(emotions)
    update_status_label(strongest_emotion, num_faces)
    root.after(10000, analyze_and_update)  # Schedule the next update in 10 seconds

# Setup tkinter GUI
root = tk.Tk()
root.title("Zoom Emotion Detection")
root.geometry("300x100")
root.attributes("-topmost", True)  # Keep the window on top

status_label = tk.Label(root, text="Initializing...", font=("Helvetica", 14))
status_label.pack(expand=True, fill='both')

root.after(10000, analyze_and_update)  # Schedule the first update in 10 seconds
root.mainloop()

# Clean up
driver.quit()

