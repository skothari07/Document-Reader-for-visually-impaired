# Document Reader for visually impaired

The challenges faced by the visually impaired people in reading printed texts in their day-today life are often not well understood. This project is a prototype which helps the user to listen to the contents of the text images in English. It involves extraction of text from the image and converting the text to translated audio output in the languages mentioned above. This is done using Raspberry Pi 3 model B and a camera module with the   concepts   of   Tesseract   OCR [Optical Character Recognition] engine and pyttsx3 module which is the textual input to speech engine. The model is programmed using Python language. It is portable and easy to use thus providing a better reading experience to the visually challenged people as enjoyed by their sighted peers. 

<h3>METHODOLOGY:</h3>

<h4>Image acquisition:</h4></br>  In this step, the images of the text can be captured by the inbuilt camera. Depending on the camera used, the quality of the image is captured. We are using the external webcam to capture an image of the text.
Image pre-processing: This step consists of colour to gray scale conversion, edge detection, noise removal, bending and cutting and thresholding. The image is converted to gray scale as many OpenCV functions require the input parameter as a gray scale image. Bilateral filter is used for noise removal. 


<h4>Image to text conversion:</h4></br> The above diagram 4 shows the flow of Text-To-Speech. The first block is the image pre- processing modules and the OCR. It converts the pre-processed image, which is in .png or .jpg form, to a .txt file. We are using the Tesseract OCR .


<h4>Text to speech conversion:</h4></br>  The second block is the voice processing module. It converts the .txt file to an audio output. Module pyttsx3 is used to convert text obtained in above step to speech. Here, the text is converted to speech using an offline speech synthesizer called pyttsx3. The Raspberry Pi has an on-board audio jack; the on-board audio is generated by a PWM output. 

![Flowchart](2.PNG)

NOTE: I myself have not made/contributed to modules: pyttsx3 and pytesseract. I just used these already available open-source modules for fast development (and it was not in scope of my project which focused on IOT side of things).
