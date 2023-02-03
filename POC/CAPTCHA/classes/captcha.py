import json
import random
import hashlib
import time
from .classimage import ClassImage
from .image import Image


class Captcha:
    
    def choiceOfImages(self,images_file, classes_image):
        self.list_images = list()
        for classe in classes_image:
            class_name = classe.getName()
            images_reliable = list()
            images_unreliable = list()
            for image in images_file:
                if image.get("class") == class_name:
                    if image.get("reliability") == 1:
                        images_reliable.append(image)
                    else:
                        images_unreliable.append(image)
            number_reliable = classe.getReliable()
            number_unreliable = classe.getUnreliable()
            for i in range(number_reliable):
                x = random.randrange(0, len(images_reliable)-1)
                image_want = images_reliable.pop(x)
                id = image_want.get("id")
                image = Image(id, class_name, 1)
                self.list_images.append(image)
            for i in range(number_unreliable):
                x = random.randrange(0, len(images_unreliable)-1)
                image_want = images_unreliable.pop(x)
                id = image_want.get("id")
                image = Image(id, class_name, 1)
                self.list_images.append(image)
                
    def sortListOfImages(self):
        self.list_images = random.shuffle(self.list_images)
    
    def solutionGeneration(self):
        self.solution =  ""
        for image in self.list_images:
            if image.getClassName() == self.class_task:
                if image.getReliability() == 1:
                    self.solution = self.solution + "1"
                else:
                    self.solution = self.solution + "3"
            else:
                if image.getReliability() == 1:
                    self.solution = self.solution + "0"
                else:
                    self.solution = self.solution + "2"
        
    def hashCaptcha(self):
        list_id = list()   
        for image in self.list_images:
            id = image.getId()
            list_id.append(id)   
        list_id.sort()
        string_id = "".join(list_id)
        self.id = string_id
        self.time_stamp = time.time()
        
    def checkUnique(self, captcha_file):
        ok = True
        for captcha in captcha_file:
            if captcha.get("id") == self.id:
                ok = False
                break
        return ok
    
    def __init__(self, images_file, classes_image, class_task, captcha_file):
        self.class_task = class_task
        ok = False
        while ok == False:
            choiceOfImages(images_file, classes_image)
            sortListOfImages()
            solutionGeneration()
            hashCaptcha()
            ok = checkUnique(captcha_file) 
        
    def getClassTask(self):
        return self.class_task
    
    def getListImages(self):
        return self.list_images
    
    def getSolution(self):
        return self.solution
    
    def getId(self):
        return self.id
    
    def getTimeStamp(self):
        return self.time_stamp
    
    
    
 
    