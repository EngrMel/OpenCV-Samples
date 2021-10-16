import cv2 as cv

img = cv.imread('python.jpg')
cv.imshow('Python', img)

cv.waitKey(0)

# Reading Videos
capture = cv.VideoCapture(0)
#capture = cv2.VideoCapture('rtsp://username:password@192.168.1.64/1') #for ip cameras
#capture = cv.VideoCapture('http://192.168.100.41:4747/mjpegfeed?640x480') #for droidcam app

while True:
    isTrue, frame = capture.read()

    # if cv.waitKey(20) & 0xFF==ord('d'):
    # This is the preferred way - if `isTrue` is false (the frame could
    # not be read, or we're at the end of the video), we immediately
    # break from the loop.
    if isTrue:
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()