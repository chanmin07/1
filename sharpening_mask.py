import cv2 as cv
import numpy as np
#smoothing
roi = cv.imread('lenna(gray).jpg')
roi_gray = cv.cvtColor(roi,cv.COLOR_BGR2GRAY)

#mask = np.array([
#    [0,-1,0],
#    [-1,5,-1],
#    [0,-1,0]
#])
#mask2 = np.array([
#    [-1,-1,-1],
#    [-1,9,-1],
#    [-1,-1,-1]
#])

mask = np.array([ #가우시안 필터
    [0.0000,0.0000,0.0002,0.0000,0.0000],
    [0.0000,0.0113,0.0837,0.0113,0.0000],
    [0.0002,0.0837,0.6187,0.0837,0.0002],
    [0.0000,0.0113,0.0837,0.0113,0.0000],
    [0.0000,0.0000,0.0002,0.0000,0.0000]])


output_box = np.zeros((roi.shape[0],roi.shape[1]),dtype=np.uint8)
#output_box = np.zeros((roi.shape[0],roi.shape[1]))

for j in range(1,roi.shape[0]-1):
    for i in range(1,roi.shape[1]-1):
        sum = 0
        for r in range(-1,2):
            for c in range(-1,2):
                sum += roi_gray.item(j+r,i+c)* mask.item(r+1,c+1)  #mask 값
        if np.sum(mask) > 0:
            sum //= np.sum(mask)  # mask 요소값의 합
        if sum > 255:
            sum = 255
        if sum < 0:
            sum = 0
        output_box.itemset(j,i,sum)

cv.imshow('origin',roi_gray)
cv.imshow('box_mask',output_box)
cv.waitKey(0)
#cv.destroyAllWindows()