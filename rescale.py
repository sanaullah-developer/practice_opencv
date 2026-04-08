import cv2 as cv
def rescaleFrame(frame, scale=0.65):
    # work for photo and video
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height):
    # work for live video
    capture.set(3,width)
    capture.set(4,height)


img = cv.imread("data/profile.jpg")
cv.imshow("Profile",img)

rescale_img = rescaleFrame(img)
cv.imshow("profile_rescale",rescale_img)

cv.waitKey(0)
   
# capture = cv.VideoCapture("data/cars.mp4")

# while True:
#     isTrue, frame = capture.read()

#     frame_resized = rescaleFrame(frame)

#     cv.imshow("video",frame_resized)
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()