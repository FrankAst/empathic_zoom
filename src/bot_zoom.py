from selenium import webdriver
import pyautogui as pag
import time

from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from PIL import ImageGrab
import cv2
from fer import FER

#import pygetwindow as gw
import subprocess
import numpy as np

# Ask user for URL:
URL = str(input("Ingrese link de zoom meeting:"))


# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

driver.get(URL)

print("Driver initialized...")

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

# Gallery view
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


# Emotions functions
print("Bot is ready to detect emotions...\n")

detector = FER(mtcnn=True)

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

# Display using old fashioned alert button
def display_strongest_emotion(emotion):
    # Activate the Zoom window using xdotool
    subprocess.run(["xdotool", "search", "--name", "Zoom", "windowactivate"])
    
    # Display the emotion on the screen using pyautogui
    pag.alert(f'The strongest emotion detected is: {emotion}')
    time.sleep(3)
    pag.press('enter')

# Display screenshots - not good for real-time.
def display_strongest_emotion_overlay(emotion):
    # Capture the screen
    screen = capture_screen()
    
    # Convert image to BGR format
    screen_bgr = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    
    # Add the strongest emotion text to the image
    cv2.putText(screen_bgr, f'Strongest Emotion: {emotion}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    
    # Display the image in a window
    cv2.imshow('Zoom Emotion Detection', screen_bgr)
    
    # Wait for 1 second to display the image, then close the window
    cv2.waitKey(1000)
    
# Display using pyautogui - writes the text on the screen, not good.    
def display_strongest_emotion_pyautogui(emotion):
    # Clear any previous text overlays
    pag.press('esc')
    
    # Overlay the text on the screen
    pag.moveTo(100, 100)
    pag.click()
    pag.write(f'Strongest Emotion: {emotion}', interval=0.1)

def display_strongest_emotion_terminal(emotion, num_faces):
    print(f'Strongest Emotion: {emotion}')
    print(f'Number of Faces: {num_faces}')

'''
def display_strongest_emotion(emotion):
    # Get the Zoom window
    zoom_window = gw.getWindowsWithTitle('Zoom')[0]
    zoom_window.activate()
    
    # Display the emotion on the screen using pyautogui
    pyautogui.alert(f'The strongest emotion detected is: {emotion}')
'''

# Working loop
# Keep the script running to maintain the bot in the meeting
try:
    while True:
        # Take a screenshot
        screen = capture_screen()
        
        # Analyze the emotions in the screenshot
        emotions = analyze_emotions(screen)
        num_faces = len(emotions)
        # Determine the strongest emotion
        strongest_emotion = get_strongest_emotion(emotions)
        
        # Display the strongest emotion
        display_strongest_emotion_terminal(strongest_emotion)
        
        
        # Wait for 5 seconds before taking the next screenshot
        time.sleep(5)
        
except KeyboardInterrupt:
    print("Bot hard stopped")
    driver.quit()
    




