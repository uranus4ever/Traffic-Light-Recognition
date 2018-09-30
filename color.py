import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# from keras.models import Sequential
# from keras.layers import Flatten, Dense, Lambda, Activation, Cropping2D, Dropout
# from keras.layers.convolutional import Convolution2D
# from keras.layers.pooling import MaxPooling2D
# from keras.optimizers import Adam
# from random import sample

# Try to identify RED, YELLO and GREEN
# draw two pictures: day and night. crop the ROI
# import example pics
pic_day_r = mpimg.imread('./image/daySequence1--00150.png')
pic_day_g = mpimg.imread('./image/daySequence1--00222.png')
pic_day_y = mpimg.imread('./image/daySequence1--01902.png')
# pic_night = mpimg.imread('./image/nightClip4--00148.png')

# plt.figure()
# plt.subplot(321)
# plt.imshow(pic_day_r)
# plt.subplot(322)
# plt.imshow(pic_day_r[400:480, 780:820, :])
# plt.subplot(323)
# plt.imshow(pic_day_g)
# plt.subplot(324)
# plt.imshow(pic_day_g[380:460, 1000:1060, :])
# plt.subplot(325)
# plt.imshow(pic_day_y)
# plt.subplot(326)
# plt.imshow(pic_day_y[360:410, 720:750, :])
# plt.show()

day_r = pic_day_r[400:480, 780:820, :]
day_g = pic_day_g[380:460, 1000:1060, :]
day_y = pic_day_y[360:410, 720:750, :]

def ColorIdentfier(pic):

    return


def TransferColor(origin, LAB="b"):
    if LAB == "l":
        out = cv2.cvtColor(origin, cv2.COLOR_RGB2Lab)[:, :, 0]
    elif LAB == "a":
        out = cv2.cvtColor(origin, cv2.COLOR_RGB2Lab)[:, :, 1]
    elif LAB == "b":
        out = cv2.cvtColor(origin, cv2.COLOR_RGB2Lab)[:, :, 2]
    return out

def PlotPic(pic):
    # pic contains 6 pictures
    plt.figure(figsize=(10, 11))
    for i in range(6):
        plt.subplot(3, 2, i+1)
        # identify 3D pic and 1D pic
        if len(pic[i].shape) > 2:
            plt.imshow(pic[i])
        else:
            plt.imshow(pic[i], cmap='gray')
    plt.show()
    return 1

if __name__ == "__main__":
    p = PlotPic([pic_day_r, day_r, pic_day_g, day_g, pic_day_y, day_y])
    print("OK")
