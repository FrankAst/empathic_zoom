# Zoom Empático 
Asistente para reuniones de Zoom que ayudará a identificar en 'casi' tiempo real cómo se siente la audiencia. Con esta herramienta, los usuarios pueden adaptar rápidamente su estilo de presentación según las emociones de los espectadores. Al monitorear las expresiones faciales y las reacciones de los participantes, el bot proporciona valiosos insights que pueden usarse para medir el compromiso de la audiencia y ajustar las didácticas en consecuencia.

## Bibliotecas necesarias
* FER: Versión usada 22.5.1 - Biblioteca de Reconocimiento de Emociones Faciales.
* Tensorflow: Versión 2.8.0 (compatibilidad con FER).
* Selenium: Versión 4.21.0 - Herramienta automatizada para navegadores.
* Pyautogui: Versión 0.9.54 - Biblioteca de automatización de GUI multiplataforma para Python.
* PIL: Biblioteca de Imágenes de Python - Proporciona capacidades de procesamiento de imágenes en Python.
* Numpy: Paquete fundamental para la computación científica en Python.
* cv2: Versión 4.9.0 - Biblioteca OpenCV utilizada para capturar capturas de pantalla durante la llamada.
* Tkinter: Versión 8.6.12 - Interfaz estándar de Python para el kit de herramientas GUI de Tk.

Otros requisitos:

* Chromedriver: debe coincidir con la versión de tu navegador Chrome.

Recomendación: usar un entorno virtual (venv) para instalar las bibliotecas requeridas.

## Funcionamiento
Una vez que se inicia la llamada de Zoom, asegúrate de ejecutar el bot y proporcionarle el enlace y la contraseña correctos. Después, sólo asegúrate que el bot se una correctamente a la llamada y presta atención a las señales:

* Luz roja: ['triste', 'enojado', 'asco', 'miedo']
* Luz amarilla: ['neutral']
* Luz verde: ['feliz', 'sorpresa']
Además de la señal de color, también verás cuál fue la emoción más fuerte entre los participantes en cada revisión.
En caso de estar realizando una presentación, ajustar la ventana del browser (en la que opera el bot) manualmente para maximizar el espacio de videos.

******************************************************************************************************************************************************************


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


