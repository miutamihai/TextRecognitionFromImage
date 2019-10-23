from skimage import color, data, restoration
from scipy.signal import convolve2d
import numpy as np

def deblur_image(image):
	img = color.rgb2gray(image)
	psf = np.ones((5,5)) / 25
	img = convolve2d(img, psf, 'same')
	img += 0.1 * img.std() * np.random.standard_normal(img.shape)
	return restoration.wiener(img, psf, 1100)
