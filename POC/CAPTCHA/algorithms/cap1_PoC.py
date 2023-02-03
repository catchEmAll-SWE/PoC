from turtle import delay
import cv2 as cv
#from matplotlib import pyplot as plt
import numpy as np
#import imutils
import urllib.request
from pyunsplash import PyUnsplash



for i in range(1):
    req = urllib.request.urlopen('https://source.unsplash.com/AEQymR1fOOU')
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv.imdecode(arr, -1)

    #cv.imshow(str(i)+" normal", img)
    #if cv.waitKey() & 0xff == 27: quit()

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #cv.imshow(str(i)+" gray", gray)
    #if cv.waitKey() & 0xff == 27: quit()

    bilFilter = cv.bilateralFilter(gray, 11, 17, 17)
    edge = cv.Canny(bilFilter, 20, 200)
    cv.imshow(str(i), edge)
    delay(1)

if cv.waitKey() & 0xff == 27: quit()
