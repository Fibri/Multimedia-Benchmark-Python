# coding: utf8
# skimage >= 0.12

from skimage import util
import matplotlib.pyplot as plt
import numpy as np

from skimage import io, color


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

    if type_bruit == 'AG':
        bruit = util.random_noise(np.zeros(img.shape),mode='gaussian')
        img_bruitee = util.random_noise(img, mode='gaussian')
    else:
        bruit = util.random_noise(np.zeros(img.shape), mode='s&p')
        img_bruitee = util.random_noise(img, mode='s&p')


if __name__ == '__main__':
    img = color.rgb2gray(io.imread("talvi.jpg"))

    # convulution_1D()
    # filtre_moyenneur_1D()
    deriv1D()
