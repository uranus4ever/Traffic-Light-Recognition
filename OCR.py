# -*- coding: UTF-8 -*-
import pytesseract
from PIL import Image
import copy
import cv2

filename = './OCR_pic/1.jpg'
img = cv2.imread(filename)
rows = img.shape[0]
cols = img.shape[1]
# transfer to grayfile
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cover = copy.copy(gray)
# transfer to opposite value of gray
for i in range(rows):
    for j in range(cols):
        cover[i][j] = 255-cover[i][j]
cv2.imshow('img', cover)
cv2.waitKey()
# hhh = Image.open(filename1)
# code = pytesseract.image_to_string(cover, lang='chi_sim')
code = pytesseract.image_to_string(cover, lang = 'eng')
print(code)
cv2.destroyAllWindows()