import json
import sys
sys.path.insert(1, '/classes')
from classes.captcha import Captcha
from classes.classimage import ClassImage
from classes.image import Image
from various_algorithms import decisionAllForClasses, writingCaptcha
 
#bisogna importare qualche modulo path per impostare la corretta path, vedi script di correzzione documenti fatto dagli altri

open_file = open('\images.json')
images_file = json.load(open_file)

open_file = open('\captcha.json')
captcha_file = json.load(open_file)

classes_image, class_task = decisionAllForClasses(images_file)
captcha = Captcha(images_file, classes_image, class_task, captcha_file)
captcha_file = writingCaptcha(captcha, captcha_file)
print('test')
    


