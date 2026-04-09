import cv2 as cv

img = cv.imread('data\download (5).jpg')

# cv.imshow("Profile", img)

# Converting an image to gray scale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray",gray)

#Blur
# blur = cv.GaussianBlur(img,(9,9), cv.BORDER_DEFAULT)
# cv.imshow("Blur",blur)

# Edge Cascade
canny = cv.Canny(img, 125,175)
cv.imshow("canny",canny)

# Dilating the image
dilated = cv.dilate(canny, (9,9), iterations=1)
cv.imshow("dilated",dilated)

# Eroding
eroded = cv.erode(dilated,(3,3),iterations=1)
cv.imshow("eroded",eroded)

# Resize

resized = cv.resize(img, (500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("resize",resized)

# Cropped
cropped = img[50:200,200:400]
cv.imshow("cropped",cropped)

cv.waitKey(0)