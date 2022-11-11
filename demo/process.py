import cv2
import sys

img = cv2.imread(sys.path[0]+"/test3.jpeg", 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite('demo/testp3.jpg', gray)