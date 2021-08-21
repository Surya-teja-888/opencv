import cv2

# Opening Camera from the Laptop
capture = cv2.VideoCapture(0)

# Getting information like frame width and height
frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS) # FPS means frame per second

print("frame_width: ",frame_width)
print("frame_height",frame_height)
print("Frames per second: ",fps)

while capture.isOpened() is True:

    ret, frame = capture.read() # reading in the same way as cv2.imread()
    # ret is boolean value either it can be True --> 1 or False --> 0
    if ret is True:

        # Displaying image
        cv2.imshow("Frame",frame)

        # Conerting into grau scale image which consists of 8 bits per pixel
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray Frame",gray)

        k = cv2.waitKey(0)
        if k == 27:
            break

capture.release()
cv2.destroyAllWindows()

