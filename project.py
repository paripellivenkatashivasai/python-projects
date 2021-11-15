import cv2
image=cv2.imread('Hulk.jpg')   

grey_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)  

invert=cv2.bitwise_not(grey_image) 

blur=cv2.GaussianBlur(invert,(21,21),00)  

invertedblur=cv2.bitwise_not(blur)  

sketch=cv2.divide(grey_image,invertedblur,scale=256.0)  

cv2.imwrite('Hulksketch.png',sketch)