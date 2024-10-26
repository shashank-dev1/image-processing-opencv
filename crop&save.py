import cv2
import cv2.colored_kinfu
import numpy as np

# Read an image
img = cv2.imread('cody-scott-milewski-aCnkRlBD0i4-unsplash.jpg')

# croping img
img_crop = img[0:300,0:500]

# saving img any format
cv2.imwrite('a sample for crop.jpg',img_crop)

cv2.imshow('window',img_crop)
cv2.waitKey(0)