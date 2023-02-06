import requests as rq
import json
import os
import mysql.connector
from time import sleep
import cv2 as cv
import urllib.request
import numpy as np


ACCESS_KEY = "1CoGBz63unkif-f4iBuOzL4g6o2oP-OMmFoMs7quj24"
valuableWord = ["ship", "car", "bird", "bottle", "laptop"]
db = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd = "root-1234",
    database = "captcha_db"
)
mycursor = db.cursor()
dir = './immagini/' + 'img.jpg'
for i in range(5):
    r = rq.get(
          'https://api.unsplash.com/photos/random/?w=200&h=200&query={0}&client_id={1}'.format(valuableWord[i], ACCESS_KEY),allow_redirects=True)
    jsonContent = json.loads(r.content)
    mycursor.execute("INSERT INTO immagine (idImmagine,classeImmagine,sicurezzaImmagine) VALUES(%s,%s,%s)", (jsonContent["id"],valuableWord[i],0))
    db.commit()
    dir = './immagini/' + jsonContent["id"] + '.jpg'
    image = rq.get(jsonContent["urls"]["regular"], allow_redirects=True)
    open(dir, 'wb').write(image.content)
    raw_image = cv.imread(dir)
    gray = cv.cvtColor(raw_image, cv.COLOR_BGR2GRAY)
    bilFilter = cv.bilateralFilter(gray, 11, 17, 17)
    canny = cv.Canny(bilFilter, 20, 200)
    cv.imwrite(dir, canny)


