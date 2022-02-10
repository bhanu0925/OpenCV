#importing libraries
import cv2
cap = cv2.VideoCapture(r".\video\BMW.mp4")
check , vid = cap.read()
count = 0
check = True
framelist = []
while(check == True):
    cv2.imwrite(r".\video\frame%d.jpg" %count , vid)
    check , vid = cap.read()
    framelist.append(vid)
    count += 1

# last value in the frame_list is None
# because when video reaches to the end
# then false value store in check variable
# and None value is store in vide variable.

# removing the last value from the
# frame_list by using pop method of List
framelist.pop()
framelist.reverse()
for frame in framelist:
    cv2.imshow("Frame" , frame)
    if cv2.waitKey(25) and 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()