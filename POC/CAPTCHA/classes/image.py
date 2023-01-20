class Image:
    def __init__(self,id, class_name,reliability):
        self.id = id 
        self.class_name = class_name
        self.reliability = reliability
    
    def getId(self):
        return self.id

    def getClassName(self):
        return self.class_name

    def getReliability(self):
        return self.reliability