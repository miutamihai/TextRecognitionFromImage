import scipy.misc
from scipy import misc
from scipy.misc.pilutil import Image

 
im = Image.open('Heineken.png')
im_array = scipy.misc.fromimage(im)
im_inverse = 255 - im_array
im_result = scipy.misc.toimage(im_inverse)
misc.imsave('InversedHeineken.png',im_result)
