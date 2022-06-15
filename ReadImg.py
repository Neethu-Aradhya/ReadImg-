import cv2 as cv
from cv2 import imshow
from cv2 import blur
import numpy as np
 
#blank = np.zeros((500,500),dtype='uint8')
#cv.imshow("blank",blank)

img =cv.imread("img100.png")
#cv.imshow('my picture',img)

#print("see the picture")

        # Write text on image
#cv.putText(img,"I love coding" ,(200,50),cv.FONT_HERSHEY_SIMPLEX,1,(108,255,200),2)
#cv.imshow('My picture',img)

        #convrting to grayscale
       
gray= cv.cvtColor(img,cv.COLOR_BGRA2GRAY)
cv,imshow("gray",gray)


           #Blur
#blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)    
#cv.imshow("Blur",blur)       
cv.waitKey(0)