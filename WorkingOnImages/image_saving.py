import cv2

# reading the image
image = cv2.imread(filename=r'.\img\nature.jpg', flags=0)
print("original size : ", image.shape)

## resizing will be in width and height formate, but shapre will be (height , width) format

new_blk_image = cv2.resize(image,dsize=(450,430))
print("new image size : ", new_blk_image.shape)

# displaying image
# window name
# image matrix - image varoable
cv2.imshow('My pic', new_blk_image)
cv2.imwrite(r'.\img\Resized_blk.jpg',new_blk_image)

cv2.waitKeyEx(0)
cv2.destroyAllWindows()