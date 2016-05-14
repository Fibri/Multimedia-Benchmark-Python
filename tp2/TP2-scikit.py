# coding: utf8
# skimage >= 0.12


from skimage import io, color
from scipy.ndimage import convolve
import numpy as np

def convulution_1D():
    v = np.array([ 1,  1,  1])
    return np.convolve(v,v,mode='full')

def filtre_moyenneur_1D():
    signal = np.ones(100)
    signal[0:50] = 0



if __name__ == '__main__':
    img = color.rgb2gray(io.imread("talvi.jpg"))

    #convulution_1D()
    filtre_moyenneur_1D()