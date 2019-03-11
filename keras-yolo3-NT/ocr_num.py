from PIL import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np

image = Image.open('C:/Users/tag2sgh/Documents/GitHub/Traffic-Light-Recognition/keras-yolo3-NT/test_data/ocr02.jpg')
box = 342, 387, 413, 429
top, left, bottom, right = box
box_ocr = left, top, right, bottom
roi = image.crop(box_ocr)
R, G, B = roi.split()
roi_grey = roi.convert('L')

threshold = 195
table = []
for i in range(256):
    if i < threshold:
        table.append(1)
    else:
        table.append(0)

roi_bin = roi_grey.point(table, '1')

ax = plt.subplot(2, 3, 1)
ax.set_title('Origin')
ax.imshow(image)
ax = plt.subplot(2, 3, 2)
ax.set_title('ROI')
ax.imshow(roi)
ax = plt.subplot(2, 3, 3)
ax.set_title('blur')
ax.imshow(blur)
ax = plt.subplot(2, 3, 4)
ax.set_title('R')
ax.imshow(R, cmap='binary')
ax = plt.subplot(2, 3, 5)
ax.set_title('G')
ax.imshow(G, cmap='binary')
ax = plt.subplot(2, 3, 6)
ax.set_title('B')
ax.imshow(B, cmap='binary')
plt.show()
