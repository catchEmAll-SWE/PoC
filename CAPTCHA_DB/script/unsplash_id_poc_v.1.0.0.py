import requests as rq
import json
import os
import mysql.connector
from time import sleep
import cv2 as cv
import pymysql


ACCESS_KEY = "1CoGBz63unkif-f4iBuOzL4g6o2oP-OMmFoMs7quj24"
valuableWord = ["car"]
classi = ["macchine"]
# database connection
db = pymysql.connect(host="localhost", port=3307, user="root", passwd="root", database="captcha_db")
mycursor = db.cursor()

for i in range(1):
    r = rq.get(
          'https://api.unsplash.com/photos/random/?w=200&h=200&query={0}&client_id={1}'.format(valuableWord[i], ACCESS_KEY),allow_redirects=True)
    jsonContent = json.loads(r.content)
    dir = "./assets/" + jsonContent["id"] + '.jpg'
    print(jsonContent["id"])
    mycursor.execute("INSERT INTO image (id,class,reliability,path) VALUES(%s,%s,%s,%s)", (jsonContent["id"],classi[i],50,dir))
    db.commit()
    image = rq.get(jsonContent["urls"]["regular"], allow_redirects=True)
    with open(dir, 'wb') as f:
        f.write(image.content)
    raw_image = cv.imread(dir)
    gray = cv.cvtColor(raw_image, cv.COLOR_BGR2GRAY)
    bilFilter = cv.bilateralFilter(gray, 11, 17, 17)
    canny = cv.Canny(bilFilter, 20, 200)
    cv.imwrite(dir, canny)




