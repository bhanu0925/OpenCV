import cv2
"""capturing fro webcam and saving as video"""

cap2 = cv2.VideoCapture(0,cv2.CAP_DSHOW)

##DIVX,XVID,MJPG,X264,WMV1,WMV2

fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
# contains 4 parameter, name, codec,fps,resolution
output = cv2.VideoWriter(r'.\video\output.avi',fourcc,20.0,(640,480),0)


while cap2.isOpened():
    ret,frame2 = cap2.read()
    if ret == True: ## until the frames are availble
        frame2 = cv2.resize(frame2,(500,400))
        grey = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Color",frame2)
        cv2.imshow("grey", grey)
        output.write(grey)
        if cv2.waitKey(25) & 0xFF == ord('q'):  # mili second will decide how fast the video will play.
            break
    else:
        break
cap2.release()
output.release()
cv2.destroyAllWindows()