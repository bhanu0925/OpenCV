import cv2

# 0 = in build webcam
# 1 = external webcam, like usb
# Path of the video
cap = cv2.VideoCapture(0)

while True:
    ret_,frame = cap.read()
    cv2.imshow("my video",frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cap.release()
        break
cv2.destroyAllWindows()



