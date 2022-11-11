import cv2

img = cv2.imread("pres.jpeg") 

img1 = img[605:605+44, 70:70+236]
bigger1 = cv2.resize(img1, (500, 200))
gray1 = cv2.cvtColor(bigger1, cv2.COLOR_BGR2GRAY)

img2 = img[648:648+44, 71:71+236]
bigger2 = cv2.resize(img2, (500, 200))
gray2 = cv2.cvtColor(bigger2, cv2.COLOR_BGR2GRAY)

img3 = img[691:691+44, 71:71+236]
bigger3 = cv2.resize(img3, (500, 200))
gray3 = cv2.cvtColor(bigger3, cv2.COLOR_BGR2GRAY)

img4 = img[735:735+44, 71:71+236]
bigger4 = cv2.resize(img4, (500, 200))
gray4 = cv2.cvtColor(bigger4, cv2.COLOR_BGR2GRAY)

img5 = img[775:775+44, 71:71+236]
bigger5 = cv2.resize(img5, (500, 200))
gray5 = cv2.cvtColor(bigger5, cv2.COLOR_BGR2GRAY)

img6 = img[819:819+44, 71:71+236]
bigger6 = cv2.resize(img6, (500, 200))
gray6 = cv2.cvtColor(bigger6, cv2.COLOR_BGR2GRAY)

cv2.imwrite("demo/test/crop1.jpg", gray1)
cv2.imwrite("demo/test/crop2.jpg", gray2)
cv2.imwrite("demo/test/crop3.jpg", gray3)
cv2.imwrite("demo/test/crop4.jpg", gray4)
cv2.imwrite("demo/test/crop5.jpg", gray5)
cv2.imwrite("demo/test/crop6.jpg", gray6)