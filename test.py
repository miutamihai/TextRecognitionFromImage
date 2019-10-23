import cv2
from deblur_image import deblur_image

image = cv2.imread("RedBullCan.jpeg")
image = deblur_image(image)
cv2.imshow("Image", image)
key = cv2.waitKey(0)
