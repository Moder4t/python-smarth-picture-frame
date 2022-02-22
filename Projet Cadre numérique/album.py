import os
#-------------------------------------------------------

class Album():
#-------------------------------------------------------

    def __init__(self, config):
        self.config = config
        self.albums = os.listdir(self.config.PATH)
        self.albumCourant = 0
#-------------------------------------------------------
       
    def affiche(self):
        if os.path.exists(self.config.PATH):
            print ("Le répertoire album existe")
        else:
            print ("Le répertoire album n'existe pas")
            
        print(self.albums)
#-------------------------------------------------------
    
    def getAlbumCourant(self):
        return self.config.PATH + self.albums[self.albumCourant]  + "/"
#-------------------------------------------------------
    
    def getNextAlbum(self):
        if self.albumCourant < (len(self.albums) - 1):
            self.albumCourant = self.albumCourant + 1
        else:
            self.albumCourant = 0
        
        return self.config.PATH + self.albums[self.albumCourant] + "/"   
#-------------------------------------------------------
        
    def getAlbumName(self):
        return (self.albums[self.albumCourant])
#-------------------------------------------------------
    
if __name__ == "__main__":
    print ("Début du test\n")
    from config import *
    config = Config()    
    a = Album(config)
    a.affiche()
    print(a.getAlbumCourant())
    print(a.getNextAlbum())    
    print("\nFin du test")