import mahotas
import mahotas.demos
import numpy as np
from pylab import imshow, gray, show
from os import path

img = mahotas.demos.load('lean', as_grey = True)
img = img.astype(np.uint8)

#Seuillage avec méthode Otsu
seuillage_otsu = mahotas.otsu(img)
imshow(img > seuillage_otsu)
show()

#seuillage avec méthode Riddler_Calvard
seuillage_rc = mahotas.rc(img)
imshow(img > seuillage_rc)
show()