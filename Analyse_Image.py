''' Import d'une image de la camera de la raspberry

from picamera.array import PiRGBArray
from picamera import PiCamera
import time

def importCamImage():
    camera = PiCamera()
    rawCapture = PiRGBArray(camera)
    time.sleep(0.1)
    camera.capture(rawCapture, format="bgr")
    return rawCapture.array
'''

import imutils # pour l'installer depius la console : pip install imutils
import cv2 # pour l'installer depius la console : pip install opencv-contrib-python --upgrade
# plus simple : utiliser pipenv avec le fichier Pipfile.lock associe au projet pour creer un environnement virtuel

def importLocalImage():
    return cv2.imread("TrollFace.jpg")

# import l'image depuis le dossier local
image = importLocalImage()
(h, w, d) = image.shape
print(image.shape)

# Reduit la taille de l'image pour etre affiche
resized = imutils.resize(image, width = 1800)
print(resized.shape)

cv2.imshow("Image", resized)

# Presser 0 pour quitter la fenetre
cv2.waitKey(0)