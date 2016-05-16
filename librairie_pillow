
import io
import os
from PIL import Image
from itertools import izip
from pylab import *
import matplotlib.pyplot as plt
im = Image.open("test2.png")

# Affichage des valeurs de pixels d'une image

def affichage_pixels(img):
    (largeur,hauteur) = im.size
    data=im.getdata()
    print("Valeurs des pixels: ")
    l= list(data)
    for x in range(hauteur):
        print(l[x:largeur])
    
# Affichage de l'histogramme des valeurs de pixels
    
def affichage_histogramme(img,x):  # x: précision de l'histogramme
    data=im.getdata()
    xlim(0.0,256.0)
    plt.hist(data,x)
    
# Qauntification d'une image
    
def quantification(img,x): # x: nbre de couleurs
    result = img.convert('P', palette=Image.ADAPTIVE, colors=x)
    result.show()
    return result
    

def quadratique(img1, img2):
    assert img1.mode == img2.mode, "Type d'image différente"
    assert img1.size == img2.size, "Tailles différentes"
     
    pairs = izip(img1.getdata(), img2.getdata())
    if len(img1.getbands()) == 1:
        dif = sum(abs(p1-p2) for p1,p2 in pairs)
    else:
        dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
     
    ncomponents = img1.size[0] * img1.size[1] * 3
    print ("Difference (en %):", (dif / 255.0 * 100) / ncomponents)
        
def seuillage(image,seuil):
    (largeur,hauteur) = image.size
    index=0
    data=image.getdata()
    l= list(data)
    for x in range(hauteur):
        for y in range(largeur):
            if(len(l[index])==3):
                (r,g,b)=l[index]
            else:
                (r,g,b,d)=l[index]
            Gris = 0.2125*r + 0.7154*g + 0.0721*b
            if(Gris>seuil):
                image.putpixel((x,y),(255,255,255))
            else:
                image.putpixel((x,y),(0,0,0))
            index=index+1
    return image
    
im4=seuillage(im,150)
im4.show()
