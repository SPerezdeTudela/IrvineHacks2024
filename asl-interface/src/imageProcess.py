
import fileinput
import base64
import numpy as np 
import cv2

def get_data(): 
    try:
        # Receives image data from Node JS
        # Will be a base64 string, which we can decode to get the bytes
        for line in fileinput.input():
            image += line 
    except OSError:
        print("Found OSError")
    
    return image

def decode(image):
    return base64.b64decode(image)

def run():
    image = get_data()
    image_byte = decode(image)
    

    #Notes: 
    #Maybe turn into image, and then return back a grayscale array?
    #Not sure when the resiing should happen
    #How to send to Azra?


    #Have to get it to grayscale here
    buffer = np.fromstring(image_byte, np.float32)
    
    #The line below turns it into image, but I don't think that's necesary
    #image_array = cv2.imdecode(buffer, cv2.IMREAD_GRAYSCALE) #Reads to grayscale

    #Resize to 28 x 28 



