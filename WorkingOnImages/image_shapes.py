import cv2

# reading the image
# flags = 1 - color image by default, or cv2.IMREAD_COLOR
# flags = 0 - grey , or cv2.IMREAD_GREY
# flags = -1 - colour with alpha channel or cv2.IMREAD_UNCHANGED  - (343,3656,4) shape has 4 channels, transperency channel


image = cv2.imread(filename=r'.\img\nature.jpg', flags=-1)
print(image.shape)  ## (2897,2241,3) , (height, width, rgb) rgb = 0-255, RGB color code chart, or bgr ,

# displaying image
# window name
# image matrix - image varoable
cv2.imshow('My pic', image)

cv2.waitKeyEx(0)
cv2.destroyAllWindows()