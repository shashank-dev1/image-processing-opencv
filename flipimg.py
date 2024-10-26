import cv2
import cv2.colored_kinfu
import numpy as np

# Read an image
img = cv2.imread('cody-scott-milewski-aCnkRlBD0i4-unsplash.jpg')

# fliping pics(1,0,-1)
img_flip = cv2.flip (img,0)

cv2.imshow('window',img_flip)
cv2.waitKey(0)