from skimage import data, io, color, exposure, img_as_float
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

    ax_img, ax_hist, ax_cdf = plot_img_and_hist(img, axes[0 , :], N)
    ax_img.set_title('Image')

    y_min, y_max = ax_hist.get_ylim()
    ax_hist.set_ylabel('Number of pixels')
    ax_hist.set_yticks(numpy.linspace(0, y_max, 5))
    fig.tight_layout()
    plt.show()



if __name__ == '__main__':
    img = Image.open("lena.png").convert('L')
    nImg = numpy.array(img, numpy.uint8)

    # quantification(nImg)
    # seuillage(nImg)
    egalisation(img)
