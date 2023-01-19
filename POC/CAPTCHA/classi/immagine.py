class Immagine:
    def __init__(self,id, path, nomeclasse,sicura):
        self.id = id 
        self.path = path 
        self.nomeclasse = nomeclasse
        self.sicura = sicura
    
    def getId(self):
        return self.id
    
    def getPath(self):
        return self.path

    def getNomeClasse(self):
        return self.nomeclasse

    def getSicura(self):
        return self.sicura