from album import Album
from ListePhotos import ListePhotos
import logging
import yaml
import os
import pygame
from config import*
import time
from PIL import Image, ExifTags
import RPi.GPIO as GPIO
pygame.init() 
BOUTON1 = 6
BOUTON2= 17
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(BOUTON1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(BOUTON2, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#-------------------------------------------------------
def getRotation(fichier):
  for orientation in ExifTags.TAGS.keys(): 
    if ExifTags.TAGS[orientation]=='Orientation': 
        return 0 

  print("Orientation (Indice) : ", orientation) 
  try: 
      exifData = img._getexif() 
      print("Orientation (Valeur) : ", exifData[orientation]) 
  except: 
      print("Pas de donnée EXIF")   

  return exifData[orientation]

    # Extraire l'information EXIF de rotation de l'image

#-------------------------------------------------------
def aspectScale(img,tailleEcran):
  nomFichier, extensionFichier = os.path.splitext(img) 
  print(nomFichier, extensionFichier)   

  try: 
      img = Image.open(img) 
      rgbImg = img.convert('RGB') 
# Mettre a l'echelle l'image 'img' pour s'ajuster à 'tailleEcran'.
      rgbImg = rgbImg.resize(tailleEcran) 
      rgbImg = rgbImg.rotate(45) 
      rgbImg.save(nomFichier + ".jpg","JPEG") 
  except OSError: 
      print("Impossible de convertir", img)
  return rgbImg
# Respecter les proportion de l'image originale


#-------------------------------------------------------
def cornerPos(img, tailleEcran):
    
    #rect = img.get_rect()
    #rect2.center = ((tailleEcran[0]- height)/2, (tailleEcran[1] -width)/2)

    width, height = img.size
    rect = pygame.Rect(0,0,(tailleEcran[0]- height)/2, (tailleEcran[1] -width)/2)
    #rect.top = ((tailleEcran[0]- height)/2, (tailleEcran[1] -width)/2)

    return rect
    # Position du coin de l'image
#-------------------------------------------------------
def event_btnAlbum(channel):
  print("Event: Bouton Album")
#-------------------------------------------------------
def event_btnVeille(channel):
  print("Event: Bouton Veille")

#-------------------------------------------------------
config = Config()
album=Album(config)
listePhotos = ListePhotos(album.getAlbumCourant())
screen = pygame.display.set_mode(config.SCREEN_SIZE) 
running = True
#-------------------------------------------------------
while running:
  pygame.time.Clock().tick(config.FPS)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
      
    photo = listePhotos.getPhoto()
    img = pygame.image.load(photo)
    rotation = getRotation(photo)
    if rotation != 0:
      img = pygame.transform.rotate(img, rotation)
    img = aspectScale(photo, config.SCREEN_SIZE)
    #screen.blit(img, cornerPos(img,config.SCREEN_SIZE))
    screen.blit(img, cornerPos(img,config.SCREEN_SIZE))

    pygame.display.flip()
#-------------------------------------------------------
pygame.quit()