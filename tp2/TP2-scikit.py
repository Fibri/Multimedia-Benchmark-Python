# coding: utf8
# skimage >= 0.12

from skimage import util
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from skimage import io, color, filters


def convulution_1D():
    v = np.array([1, 1, 1])
    return np.convolve(v, v)


def filtre_moyenneur_1D():
    signal = np.ones(100)
    signal[0:50] = 0
    masque = np.ones(3) / 3
    plt.hist(signal)
    plt.show()
    np.convolve(signal, masque)


def deriv1D():
    sequence = np.array([0, 0, 0, 1, 2, 5, 5, 5, 5, 5, 5, 3, 3, 3, 9, 9, 9, 9, 9, 9, 8, 4])
    masque = np.array([1, 0, -1])
    derivee = np.convolve(sequence, masque)
    sequence_etendue = np.zeros(sequence.size + 1)
    sequence_etendue[1:sequence_etendue.size] = sequence
    fig = plt.figure()
    fig.add_subplot(1, 2, 1)
    plt.plot(sequence_etendue)
    fig.add_subplot(1, 2, 2)
    plt.plot(derivee)
    plt.show()


def filtre2D(img):
    N=3
    type_bruit = 'AG'

    selem = np.ones([3,3])
    if type_bruit == 'AG':
        bruit = util.random_noise(np.zeros(img.shape),mode='gaussian')
        img_bruitee = util.random_noise(img, mode='gaussian')
    else:
        bruit = util.random_noise(np.zeros(img.shape), mode='s&p')
        img_bruitee = util.random_noise(img, mode='s&p')

    img_bruit_median = filters.median(img_bruitee,selem)
    img_bruit_linear = ndimage.convolve(img_bruitee,selem)

    fig = plt.figure()

    if type_bruit == 'SP':
        bruit_linear = ndimage.convolve(bruit, selem)
        img_linear = ndimage.convolve(img, selem)
        fig.add_subplot(3,3,1)
        plt.imshow(img, cmap='gray')
        fig.add_subplot(3,3,2)
        plt.imshow(bruit, cmap='gray')
        fig.add_subplot(3,3,3)
        plt.imshow(img_bruitee, cmap='gray')
        fig.add_subplot(3,3,4)
        plt.imshow(img_linear, cmap='gray')
        fig.add_subplot(3,3,5)
        plt.imshow(bruit_linear, cmap='gray')
        fig.add_subplot(3,3,6)
        plt.imshow(img_bruit_linear, cmap='gray')
        fig.add_subplot(3,3,9)
        plt.imshow(img_bruit_median, cmap='gray')
    else:
        fig.add_subplot(2,2,1)
        plt.imshow(img, cmap='gray')
        fig.add_subplot(2,2,2)
        plt.imshow(img_bruitee, cmap='gray')
        fig.add_subplot(2,2,3)
        plt.imshow(img_bruit_linear, cmap='gray')
        fig.add_subplot(2,2,4)
        plt.imshow(img_bruit_median, cmap='gray')
    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    img = color.rgb2gray(io.imread("talvi.jpg"))

    # convulution_1D()
    # filtre_moyenneur_1D()
    #deriv1D()
    filtre2D(img)
