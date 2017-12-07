import sys
import cv2
import numpy

import base64
import requests

def get_as_base64(url1):
    return base64.b64encode(requests.get(url1).content)
#URL where the image is stored
url1 = ""
fh1= open("C:/Users/Home/Desktop/retrieve1.jpg","wb")
fh1.write(base64.b64decode(get_as_base64(url1)))
fh1.close()

def get_as_base64(url2):
    return base64.b64encode(requests.get(url2).content)
#URL where the image is stored
url2 = ""
fh2= open("C:/Users/Home/Desktop/retrieve2.jpg","wb")
fh2.write(base64.b64decode(get_as_base64(url2)))
fh2.close()

path1="C:/Users/Home/Desktop/retrieve1.jpg"
path2="C:/Users/Home/Desktop/retrieve2.jpg"
img1=cv2.imread(path1)
img2=cv2.imread(path2)
dst=cv2.addWeighted(img1,0.5,img2,0.5,0)
cv2.imshow('dst', dst) 
cv2.waitKey(0)
