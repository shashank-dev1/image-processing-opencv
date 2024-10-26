import cv2
import cv2.colored_kinfu
import numpy as np

# Read an image
img = cv2.imread('cody-scott-milewski-aCnkRlBD0i4-unsplash.jpg')

# for type of image
# print(type(img))

# for orignal image shape 
# print(img.shape)

# for converting rgb to gray
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# print(img_gray.shape)


# playing with rgb chanales 
# imgBlue = img[:,:,0]
# imgGreen =  img[:,:,1]
# imgRed = img[:,:,2]

# new_img = np.hstack((imgBlue, imgGreen, imgRed))

cv2.imshow('window', img_gray)

cv2.waitKey(0)