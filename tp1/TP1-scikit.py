# coding: utf8
# skimage >= 0.12

from skimage import data, io, color, exposure, img_as_float, transform, filters
import matplotlib
import matplotlib.pyplot as plt
from scipy import ndimage
from PIL import Image
import numpy
import scipy
from skimage._shared.interpolation import extend_image



def quantification(img):
    # q = float(input("Coefficient de quantification : "))
    q = 30
    imgQ = img.copy()
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            imgQ[x][y] = q * round(img[x][y] / q)

    fig = plt.figure()
    fig.add_subplot(1, 2, 1)
    plt.imshow(Image.fromarray(img), cmap='Greys_r')
    fig.add_subplot(1, 2, 2)
    plt.imshow(Image.fromarray(imgQ), cmap='Greys_r')
    plt.show()
    return imgQ

def quadratique(img1, img2):
    if img1.shape == img2.shape:
        err_quadratique = 0
        for x in range(img1.shape[0]):
            for y in range(img1.shape[1]):
                diff= int(img1[x][y]) - int(img2[x][y])
                err_quadratique=err_quadratique+diff*diff
        err_moyenne=err_quadratique/(img1.shape[0] * img1.shape[1])
        return err_moyenne
    else:
        print("Les images ne sont pas de la même taille")

def seuillage(img):
    # seuil= int(input('Veuillez saisir la valeur du SEUIL:'))
    seuil = 128
    imgS = img <= filters.threshold_otsu(img)

    fig = plt.figure()
    fig.add_subplot(1, 2, 1)
    plt.imshow(img, cmap='Greys_r')
    fig.add_subplot(1, 2, 2)
    plt.imshow(imgS, cmap='Greys')
    plt.show()
    return imgS

def plot_img_and_hist(img, axes, bins=256):

    img = img_as_float(img)
    ax_img, ax_hist = axes
    ax_cdf = ax_hist.twinx()

    # Display image
    ax_img.imshow(img, cmap=plt.cm.gray)
    ax_img.set_axis_off()
    ax_img.set_adjustable('box-forced')

    # Display histogram
    ax_hist.hist(img.ravel()*256 , bins=bins, histtype='bar', color='cyan', normed=True)
    ax_hist.ticklabel_format(axis='y', style='scientific', scilimits=(0, 0))
    ax_hist.set_xlabel('Pixel intensity')
    ax_hist.set_xlim(0, 255)
    ax_hist.set_yticks([])


    # Display cumulative distribution
    img_cdf, bins = exposure.cumulative_distribution(img*256, bins)
    ax_cdf.plot(bins, img_cdf, 'r')
    ax_cdf.set_yticks([])

    return ax_img, ax_hist, ax_cdf

def egalisation(Img):
    N = 30
    fig = plt.figure()
    axes = numpy.zeros((1,2), dtype=numpy.object)

    axes[0,0] = fig.add_subplot(1, 2, 1)
    axes[0,1] = fig.add_subplot(1, 2, 2)

    ax_img, ax_hist, ax_cdf = plot_img_and_hist(Img, axes[0 , :], N)
    ax_img.set_title('Image')

    y_min, y_max = ax_hist.get_ylim()
    ax_hist.set_ylabel('Nombre de pixels')
    ax_hist.set_yticks(numpy.linspace(0, y_max, 5))
    fig.tight_layout()
    plt.show()

def agrandissement(img):
    img_bilinear = transform.rescale(img, scale=2, mode='wrap', preserve_range=True, order=1)
    # order=1 <=> bi-linear (skimage.transform.wrap)
    img_nearNeighbor = transform.rescale(image=img, scale=2, mode='wrap', preserve_range=True, order=0)
    # order=0 <=> nearest neighbor (skimage.transform.wrap)

    print(quadratique(img_nearNeighbor,img_bilinear))   # debug

    fig = plt.figure()
    fig.add_subplot(1, 2, 1)
    plt.imshow(img_bilinear, cmap='Greys_r')
    fig.add_subplot(1, 2, 2)
    plt.imshow(img_nearNeighbor, cmap='Greys_r')
    plt.show()


if __name__ == '__main__':
    img = Image.open("talvi.jpg").convert('L')
    img = numpy.array(img, numpy.uint8)

    #print(quadratique(quantification(img), img))
    #seuillage(img)
    # egalisation(seuillage(img))
    agrandissement(img)
