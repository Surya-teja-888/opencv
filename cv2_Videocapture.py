
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    _,thr = cv2.threshold(gray,120,255,cv2.THRESH_BINARY)

    blur = cv2.bilateralFilter(gray,10,80,80)

    # Kernel for sharpening the Image
    kernel = np.array([[-1,-1,-1],
                       [-1,9,-1],
                       [-1,-1,-1]])

    # Kernel for Edge Detection
    kernel_1 = np.array([[-1, -1, -1],
                         [-1, 8, -1],
                         [-1, -1, -1]])

    # Image Sharpening
    image_sharpen = cv2.filter2D(blur,-1,kernel=kernel)

    # Edge Detection
    edge_detection = cv2.filter2D(image_sharpen,-1,kernel=kernel_1)

    # Finding and Drawing contours
    contours,_ = cv2.findContours(thr,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    print(contours)
    #Drawing contours
    cv2.drawContours(edge_detection,contours,-1,(0,255,255))

    cv2.imshow("Frame",edge_detection)


    k = cv2.waitKey(40)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()