
# Adaptive thresholding

import cv2
import numpy as np

# reading the image
image = cv2.imread(r'.\img\resized.jpg',0)
#image = image.astype(np.uint8)

#image = image.img_to_array(image, dtype='uint8')
op_img = cv2.adaptiveThreshold(image,127,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)



#for pic in img:
cv2.imshow('My pic', op_img)
cv2.waitKeyEx(0)
cv2.destroyAllWindows()