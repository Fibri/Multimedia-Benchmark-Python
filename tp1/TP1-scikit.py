from skimage import data, io, color
import matplotlib
import matplotlib.pyplot as plt
from scipy import ndimage
from PIL import Image
import numpy
import scipy



def quantification(nImg):
    # q = float(input("Coefficient de quantification : "))
    q = 30
    nimgQ = nImg.copy()
    for x in range(nImg.shape[0]):
        for y in range(nImg.shape[1]):
            nimgQ[x][y] = q * round(nImg[x][y] / q)

    fig = plt.figure()
    fig.add_subplot(1, 2, 1)
    plt.imshow(Image.fromarray(nImg), cmap='Greys_r')
    fig.add_subplot(1, 2, 2)
    plt.imshow(Image.fromarray(nimgQ), cmap='Greys_r')
    plt.show()

def quadratique(nImg1, nImg2):
    if nImg1.shape == nImg2.shape:
        err_quadratique = 0
        for x in range(nImg.shape[0]):
            for y in range(nImg.shape[1]):
                diff=nImg1(y,x)- nImg2(y,x)
                err_quadratique=err_quadratique+diff*diff
        err_moyenne=err_quadratique/(nImg1.shape[0]*nImg1.shape[1])
        return err_moyenne
    else:
        print("Les images ne sont pas de la même taille")

def seuillage(nImg):
    seuil= int(input('Veuillez saisir la valeur du SEUIL:'))
    nImgS = nImg.copy()
    for x in range(nImgS.shape[0]):
        for y in range(nImgS.shape[1]):
            if nImgS[x][y] > seuil:
                nImgS[x][y] = 255
            else:
                nImgS[x][y] = 0
    fig = plt.figure()
    fig.add_subplot(1, 2, 1)
    plt.imshow(Image.fromarray(nImg), cmap='Greys_r')
    fig.add_subplot(1, 2, 2)
    plt.imshow(Image.fromarray(nImgS), cmap='Greys_r')
    plt.show()




if __name__ == '__main__':
    img = Image.open("lena.png").convert('L')
    nImg = numpy.array(img, numpy.uint8)

    # quantification(nImg)
    seuillage(nImg)
