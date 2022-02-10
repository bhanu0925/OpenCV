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


cap2 = cv2.VideoCapture(r'.\video\BMW.mp4')

while True:
    ret_,frame2 = cap2.read()
    frame2 = cv2.resize(frame2,(700,400))
    cv2.imshow("my video",frame2)

    if cv2.waitKey(25) & 0xFF == ord('q'):  # mili second will decide how fast the video will play.
        cap2.release()
        break
cv2.destroyAllWindows()




