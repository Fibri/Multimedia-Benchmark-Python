import matplotlib.pyplot as plt
import numpy as np

from skimage import io, color


def spectre(img):
    transfourier = np.fft.fft(img)
    fft_img = np.abs(np.log(np.fft.fftshift(transfourier)))

    invtransfourier = np.fft.ifft(transfourier)
    invtransfourier = np.abs(invtransfourier)

    fig = plt.figure()
    fig.add_subplot(1, 2, 1)
    plt.imshow(fft_img, cmap='gray')
    fig.add_subplot(1, 2, 2)
    plt.imshow(invtransfourier, cmap='gray')
    plt.show()


def chess(paramh, paramv):
    img = np.zeros([256, 256])
    for i in range(256):
        for j in range(256):
            if np.sin(2 * np.pi * i / paramh) * np.sin(j * 2 * np.pi / paramv) > 0:
                img[i][j] = 255


if __name__ == '__main__':
    img = color.rgb2gray(io.imread("texture2.jpg"))
    spectre(img)
