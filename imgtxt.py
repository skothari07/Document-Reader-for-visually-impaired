#Importing libraries
import cv2
import numpy as np
import pytesseract
import pyttsx3


try:
    from PIL import Image
except ImportError:
    import Image



#Main code and Logic

#Step 1 is to preprocess the image captured.We are converting coloured image to gray image
def preprocess(image):
	
	gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
	cv2.imwrite("output.jpg" ,gray_image)

def convert():
	text = pytesseract.image_to_string(Image.open('output.jpg'))
	print(text)
	return text

def texttospeech(txt):
	# initialisation 
	engine = pyttsx3.init() 
	rate = engine.getProperty('rate')
	engine.setProperty('rate', rate-70)
	engine.say(txt)
	engine.runAndWait() 


def main():
	# Initialize the camera
	cap = cv2.VideoCapture(1)
	while True:
		ret, frame = cap.read()
		if (ret == False):
			print ("Error opening camera")
			continue


	image = cv2.imread(frame)
	preprocess(image)
	txt = convert()
	texttospeech(txt)

if __name__ == "__main__": 
	main()

