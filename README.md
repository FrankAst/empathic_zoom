# Empathic zoom
This is a companion for zoom calls that will help identify in near-real time how the audience feels. With this tool, users can quickly adapt their presentation style based on the emotions of the viewers. By monitoring the facial expressions and emotions of the participants, the bot provides valuable insights that can be used to gauge the audience's engagement and adjust the delivery accordingly.
## Nedeed libraries
* FER: Version used 22.5.1 - Facial Emotion Recognition library.
* Tensorflow: Version 2.8.0 (FER compatibility)
* Selenium: Version 4.21.0 - Automated browser toolkit.
* Pyautogui: Version 0.9.54 - Cross-platform GUI automation library for Python.
* PIL: Python Imaging Library - Provides image processing capabilities in Python.
* Numpy: Fundamental package for scientific computing in Python.
* cv2: Version 4.9.0 - OpenCV library used to capture the screenshots during the call. 
* Tkinter: Version 8.6.12 - Standard Python interface to the Tk GUI toolkit.

Other requirements:

* Chromedriver: should match your chrome browser version.


Recommendation: running a venv to install the required libraries.

## Functioning
Once you start your zoom call, make sure to run the bot and give it the right link and password. Afterthat, just make sure the bot successfully joins the call and pay attention to the signallying:

* Red light: ['sad', 'angry', 'disgust', 'fear']
* Yellow light: ['neutral']
* Green light: ['happy', 'surprise']

On top of the colour signal, you will also see what was the strongest emotion across the participants on each revision.


