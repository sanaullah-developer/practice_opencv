import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
# cv.imshow("blank",blank)

# 1. Paint the image a certain colour
# blank[:] = 0,255,0
# we can also give the colour in a certain range
# blank[200:300,300:500] = 0,0,255
# cv.imshow("Green",blank)


# 2. Draw a ractangle
cv.rectangle(blank, (100,100), (400,400), (0,255,0), thickness=-1) # thickness show how much the ractangle will have width and -1 show filled
# cv.imshow("Ractangle",blank)

# 3. Draw a circle
cv.circle(blank, (250,250),50, (0,0,255), thickness=-1)
# cv.imshow("Circle",blank)
cv.line(blank,(100,100), (400,400), (255,255,255), thickness=5)
cv.line(blank,(100,400),(400,100),(255,255,255), thickness=5)

# 4. write text
cv.putText(blank, "Hello There", (150,60), cv.FONT_HERSHEY_TRIPLEX, 1.0,(0,255,0),2)

cv.imshow("whole picture",blank)
cv.waitKey(0)