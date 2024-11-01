import cv2
a = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
b = cv2.VideoCapture(0)
while True:
    c_rect, d_img = b.read() # read the image from b and store it to d
    if not c_rect:
        break
    e = cv2.cvtColor(d_img, cv2.COLOR_BGR2GRAY) # convert color from BGR to gray
    f = a.detectMultiScale(e, 1.3, 6 ) # variable into which we have converted the BGR to gray
    for(x1, y1, w1, h1) in f:
        cv2.rectangle(d_img, (x1, y1), (x1+w1, y1+h1), (0, 255, 0), 10)   # rectangle around the face of the imgae taking verticals(x,w) and horizontals(y,h) together with a value which is the format for BGR. just around the face there will be a hollow blue rectangular box of width 5 which will help us to detect the face.
    cv2.imshow('img', d_img) # read the image
    h = cv2.waitKey(1) & 0xff  # to wait for a particular time(sec) to detect the image from the camera/video. if not detected exit from the program.
    if h == 27:
        break

b.release() #exit from the camera
cv2.destroyAllWindows() #closing all windows that was used for detecting face.