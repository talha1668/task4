import numpy as np
import cv2

path=("Snapchat-2081338652.jpg")

image=cv2.imread(path)
grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
h, w = grayimg.shape

cv2.imshow("orignal",grayimg)

for i in range(h):
    for j in range(w):
        if (int(grayimg[i][j])-int(grayimg[i][j-1]))>150:

            grayimg[i][j]=255

        else:
            grayimg[i][j] = 0
print(grayimg)


cv2.imshow("gray image",grayimg)
cv2.waitKey(0)