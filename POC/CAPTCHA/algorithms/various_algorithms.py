from classes.captcha import Captcha
from classes.classimage import ClassImage


def decisionAllForClasses(images_file):
    return "lista delle classi gia finite", "classe task"

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