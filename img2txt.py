# Import required packages
import os
from pytesseract import pytesseract
import pyperclip
from PIL import ImageGrab, Image

def grab_img():
	try:
		# Grab image from clipboard and save it in Data folder
		im = ImageGrab.grabclipboard()
		im.save('Data\content.png','PNG')
		return "Data\content.png"
	except:
		print("No image found at clipboard")

def read(image_path):

	try:
		path_to_tesseract = r"tesseract\tesseract.exe"
		
		# Opening the image & storing it in an image object
		img = Image.open(image_path)
		
		# Providing the tesseract executable
		# location to pytesseract library
		pytesseract.tesseract_cmd = path_to_tesseract
		
		# Passing the image object to image_to_string() function
		# This function will extract the text from the image
		text = pytesseract.image_to_string(img)
		
		# Displaying the extracted text
		#  print(text[:-1])
		pyperclip.copy(text[:-1])
		os.remove(image_path)
		print("Text Copied into the Clipboard !")
	except: print("Try to copy an image then Try Again !")



img = grab_img()
read(image_path=img)


  



