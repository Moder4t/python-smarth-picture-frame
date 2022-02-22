import logging
import yaml
import os
class Config():
    def __init__(self):
        # Niveau des log
        self.LOG_LEVEL = logging.DEBUG
        #self.LOG_LEVEL = logging.CRITICAL
        
      #  self.CONFIG_FILE_NAME = "Config.yaml"
        ################################
        fichier = open("/home/pi/Desktop/Projet 3/config.YAML", "r") 
        config = yaml.load(fichier) 
        """ À compléter: la lecture du fichier de config """
        self.WAKEUP = config['wakeup']
        self.CLOSE = config['close']
        self.PERIOD = config['period']
        self.PATH = config['path']
        
        self.SCREEN_WIDTH = 400
        self.SCREEN_HEIGHT = 300
        self.SCREEN_SIZE = (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.FPS = 100
        
        
    def affiche(self):
        #####################################
        """ À compléter: Afficher  tout les attributs de la classe """
        print(self.WAKEUP)
        print(self.CLOSE)
        print(self.PERIOD)
        print(self.PATH)

    def getPeriod(self):
        chaine = self.PERIOD 
        heure,minute,seconde = map(int, chaine.split(':'))
        return (heure * 3600 + minute * 60 + seconde)
if __name__ == "__main__":
    print ("Début du test\n")
    
    a = Config()
    a.affiche()
    print(a.getPeriod())
    
    print("\nFin du test")