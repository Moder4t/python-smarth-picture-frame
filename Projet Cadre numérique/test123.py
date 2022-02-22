Charger un fichier d’image 
from PIL import Image 
img = Image.open("bird.png") 
print(img.format, img.size, img.mode)  

Extraire l’information EXIF 
from PIL import Image, ExifTags 
img = Image.open("Paris.jpg")   

for orientation in ExifTags.TAGS.keys(): 
    if ExifTags.TAGS[orientation]=='Orientation': 
        break   

print("Orientation (Indice) : ", orientation) 
try: 
    exifData = img._getexif() 
    print("Orientation (Valeur) : ", exifData[orientation]) 
except: 
    print("Pas de donnée EXIF")   

# 1 -> 0 deg; 3 -> 180 deg; 6 -> 270 deg; 8 -> 90 deg 
# Référence: https://stackoverflow.com/questions/13872331/rotating-an-image-with-orientation-specified-in-exif-using-python-without-pil-in 
 
Convertir en JPEG 
import os 
from PIL import Image   

fichierImg = "bird.png" 
nomFichier, extensionFichier = os.path.splitext(fichierImg) 
print(nomFichier, extensionFichier) 

try: 
    img = Image.open(fichierImg) 
    rgbImg = img.convert('RGB') 
    rgbImg.save(nomFichier + ".jpg") 
except OSError: 
    print("Impossible de convertir", fichierImg)  

Générer une vignette 
import os 
from PIL import Image   

fichierImg = "bird.png" 
taille = (128, 128)   

nomFichier, extensionFichier = os.path.splitext(fichierImg) 
print(nomFichier, extensionFichier)   

try: 
    img = Image.open(fichierImg) 
    rgbImg = img.convert('RGB') 
    rgbImg.thumbnail(taille) 
    rgbImg.save(nomFichier + ".thumbnail","JPEG") 
except OSError: 
    print("Impossible de convertir", fichierImg)  

Appliquer des transformations à une image 
import os 
from PIL import Image   

fichierImg = "bird.png"   

nomFichier, extensionFichier = os.path.splitext(fichierImg) 
print(nomFichier, extensionFichier)   

try: 
    img = Image.open(fichierImg) 
    rgbImg = img.convert('RGB') 
    rgbImg = rgbImg.resize((128, 128)) 
    rgbImg = rgbImg.rotate(45) 
    rgbImg.save(nomFichier + ".jpg","JPEG") 
except OSError: 
    print("Impossible de convertir", fichierImg) 