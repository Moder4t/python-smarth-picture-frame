import os
import pygame
#-------------------------------------------------------

class ListePhotos():
#-------------------------------------------------------
    def __init__(self, path):
        extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']
        self.listePhotos = []
        listeTmp = os.listdir(path)
        for photo in listeTmp:
            filename, ext = os.path.splitext(photo)
            e = ext.lower()
            if e in extensions:
                self.listePhotos.append(path + photo)
        self.photoCourante = 0
        self.noImage = "no-image.jpg"
#-------------------------------------------------------
    def getPhoto(self):
        photo = self.listePhotos[self.photoCourante]
        if self.photoCourante < (len(self.listePhotos) - 1):
            self.photoCourante = self.photoCourante + 1
        else:
            self.photoCourante = 0
            
        if len(self.listePhotos) == 0:
            photo = self.noImage
                       
        return(photo)
#-------------------------------------------------------

if __name__ == "__main__":
    print ("Début du test\n")
        #################################
    """ À compléter """
    
    print("\nFin du test")