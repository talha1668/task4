import cv2 as cv
import numpy as np

img = cv.imread('Snapchat-2081338652.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blankx = np.zeros((img.shape[0], img.shape[1]), np.uint8)
blanky = np.zeros((img.shape[0], img.shape[1]), np.uint8)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if i == j == 0:
            pass
        elif j == 0:
            pass
        else:
            if abs(int(img[i][j]) - int(img[i][j - 1])) > 30:
                blankx[i][j] = 255

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if i == j == 0:
            pass
        elif i == 0:
            pass
        else:
            if abs(int(img[i][j]) - int(img[i - 1][j])) > 30:
                blanky[i][j] = 255
#
# cv.imshow("img", img)
# cv.imshow("horizontal pixcel difference", blankx)
# cv.imshow("verticle pixcel difference: ", blanky)
# blank = cv.bitwise_or(blankx, blanky)
# cv.imshow("final", blank)
# cv.waitKey(0)
sobelx=cv.Sobel(img,cv.CV_64F,1,0)
sobely=cv.Sobel(img,cv.CV_64F,0,1)
combine_sobel=cv.bitwise_or(sobelx,sobely)

canny=cv.Canny(img,150,175)

cv.imshow('canny',canny)

cv.imshow('combine',combine_sobel)
cv.imshow('sobel x',sobelx)
cv.imshow('sobel y',sobely)
cv.waitKey(0)