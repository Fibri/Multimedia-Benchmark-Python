# coding: utf8
# skimage >= 0.12

import matplotlib.pyplot as plt
import numpy as np

from skimage import exposure, transform, filters, io, color, measure
from skimage.util.dtype import dtype_range

def quantification(img):
    # q = float(input("Coefficient de quantification : "))
    q = 30
    imgQ = img.copy()
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            imgQ[x][y] = q * round(img[x][y] / q)

    fig = plt.figure()
    fig.add_subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    fig.add_subplot(1, 2, 2)
    plt.imshow(imgQ, cmap='gray')
    plt.show()
    return imgQ


def quadratique(img1, img2):
    if img1.shape == img2.shape:
        return measure.compare_mse(img1, img2)
    else:
        print("Les images ne sont pas de la même taille")


def seuillage(img):
    # seuil= int(input('Veuillez saisir la valeur du SEUIL:'))
    seuil = 20
    imgS = filters.threshold_isodata(img) <= img

    fig = plt.figure()
    fig.add_subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    fig.add_subplot(1, 2, 2)
    plt.imshow(imgS, cmap='gray')
    plt.show()
    return imgS


def plot_img_and_hist(img, axes, bins=256):

    ax_img, ax_hist = axes
    ax_cdf = ax_hist.twinx()

    # Display image
    ax_img.imshow(img, cmap='gray')
    ax_img.set_axis_off()

    # Display histogram
    ax_hist.hist(img.ravel() * 255, bins=bins)
    ax_hist.ticklabel_format(axis='y', style='scientific', scilimits=(0, 0))
    ax_hist.set_xlabel('Pixel intensity')


    ax_hist.set_xlim(0, 255)
    # Display cumulative distribution
    img_cdf, bins = exposure.cumulative_distribution(img*255, bins)
    ax_cdf.plot(bins, img_cdf, 'r')

    return ax_img, ax_hist, ax_cdf


def egalisation(img):
    # Display results
    fig = plt.figure()
    axes = np.zeros((2, 3), dtype=np.object)
    axes[0,0] = plt.subplot(2, 2, 1, adjustable='box-forced')
    axes[0,1] = plt.subplot(2, 2, 2, sharex=axes[0,0], sharey=axes[0,0], adjustable='box-forced')
    axes[1,0] = plt.subplot(2, 2, 3)
    axes[1,1] = plt.subplot(2, 2, 4)

    img_egalisee = exposure.equalize_hist(img)

    ax_img, ax_hist, ax_cdf = plot_img_and_hist(img, axes[:, 0])
    ax_img.set_title('Image originale')
    ax_hist.set_ylabel('nombre de pixels')

    ax_img, ax_hist, ax_cdf = plot_img_and_hist(img_egalisee, axes[:, 1])
    ax_img.set_title('Image égalisée')

    ax_cdf.set_ylabel("Part de l'intensité totale")


    # prevent overlap of y-axis labels
    fig.subplots_adjust(wspace=0.4)
    plt.show()

def agrandissement(img):
    img_bilinear = transform.rescale(img, scale=2, mode='wrap', preserve_range=True, order=1)
    # order=1 <=> bi-linear (skimage.transform.wrap)
    img_nearNeighbor = transform.rescale(image=img, scale=2, mode='wrap', preserve_range=True, order=0)
    # order=0 <=> nearest neighbor (skimage.transform.wrap)

    print(quadratique(img_nearNeighbor, img_bilinear))  # debug

    fig = plt.figure()
    fig.add_subplot(1, 2, 1)
    plt.imshow(img_bilinear, cmap='gray')
    fig.add_subplot(1, 2, 2)
    plt.imshow(img_nearNeighbor, cmap='gray')
    plt.show()


if __name__ == '__main__':
    img = color.rgb2gray(io.imread("talvi.jpg"))

    # print(quadratique(quantification(img), img))
    # seuillage(img)
    egalisation(img)
    # seuillage(img)
    # agrandissement(img)
