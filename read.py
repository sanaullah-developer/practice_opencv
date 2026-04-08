import cv2 as cv

# img = cv.imread("data/profile.jpg")

# cv.imshow("Profile", img)

# cv.waitKey(0)


#reading videos

capture = cv.VideoCapture("data/cars.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow("video",frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()