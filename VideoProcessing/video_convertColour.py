import cv2
"""converting color of video to grey"""

cap2 = cv2.VideoCapture(r'.\video\charvi.mp4')

while True:
    ret_,frame2 = cap2.read()
    frame2 = cv2.resize(frame2,(500,400))
    grey = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Color",frame2)
    cv2.imshow("grey", grey)

    if cv2.waitKey(25) & 0xFF == ord('q'):  # mili second will decide how fast the video will play.
        cap2.release()
        break
cv2.destroyAllWindows()