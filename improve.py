import cv2
import numpy as np
import scipy.misc
from scipy import misc
 
im = cv2.imread('perlenbach-closeup.jpg')
im = im/255.0
im_power_law_transformation = cv2.pow(im,0.6)
misc.imsave('ImprovedPerlenbach.jpg', im_power_law_transformation)

