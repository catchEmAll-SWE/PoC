# import random
import qrandom

from classes.captcha import Captcha
from classes.classimage import ClassImage


def decisionAllForClasses(images_file):

    # select a number of classes to use in the captcha (ex. cars, tables...)
    # min 2, max 4 different classes

    categories = []
    for image in images_file:
        category = image.get("class")
        if category not in categories:
            categories.append(category)

    # pip install quantum-random

    # how_many_categories = randrange(2, 5)
    how_many_categories = qrandom.randrange(2, 5)

    classes = []
    for i in range(how_many_categories-1):
        new_category_id = qrandom.randrange(0, len(categories))
        while categories[new_category_id] in classes:
            new_category_id = qrandom.randrange(0, len(categories))

        new_category_name = categories[new_category_id]
        classes.append(ClassImage(new_category_name))

    # select a number of images for each class
    # and then select a number of safe images for each class, minimum 1 safe image

    maximum_images = 9 - len(classes) + 1;
    for i in len(classes)-1:
        image_class = classes(i)

        if i < len(classes)-1:
            image_class.setTotal(qrandom.randrange(1, maximum_images+1))
            maximum_images -= image_class.total+1
        else:
            image_class.setTotal(maximum_images)

        image_class.setReliable(qrandom.radrange(1, image_class.getTotal()+1))
        image_class.setUnreliable(image_class.getTotal() - image_class.getReliable())

    # select the task class

    task_class_id = qrandom.randrange(0, len(classes))
    task_class = classes[task_class_id].getName()

    return classes, task_class

def writingCaptcha(captcha, captcha_file):
    captcha_to_insert = {}
    id = captcha.getId()
    solution = captcha.getSolution()
    time_stamp = captcha.getTimeStamp()
    captcha_to_insert.update({"id":id})
    captcha_to_insert.update({"solution":solution})
    captcha_to_insert.update({"timestamp":time_stamp})
    captcha_file.append(captcha_to_insert)
    return captcha_file
