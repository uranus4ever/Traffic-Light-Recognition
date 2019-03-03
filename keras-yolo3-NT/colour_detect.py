import cv2
import matplotlib.pyplot as plt
import numpy


def get_roi(box, image):
    top, left, bottom, right = box
    roi = image[top:bottom, left:right]
    return roi


image = cv2.imread('C:/Users/tag2sgh/Documents/GitHub/Traffic-Light-Recognition/keras-yolo3-NT/test_data/traffic_light.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
box = 70, 276, 126, 303
roi = get_roi(box, image)
ax = plt.subplot(2, 1, 1)
ax.imshow(image)
ax = plt.subplot(2, 1, 2)
ax.imshow(roi)
plt.show()
