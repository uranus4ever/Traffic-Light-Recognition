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
pic_night = mpimg.imread('./image/nightClip4--00148.png')


day_r = pic_day_r[400:480, 780:820, :]
day_g = pic_day_g[380:460, 1000:1060, :]
day_y = pic_day_y[360:410, 720:750, :]

"""
Through test, 
A channel from LAB space can identify RED from GREEN and YELLOW. pixel thres is about 50.
L channel from LUV space can identify YELLOW from RED and GREEN. pixel thres is 90.
"""
def ColorIdentifier(pic, a_thres=50, l_thres=90):

    a_channel = cv2.cvtColor(pic, cv2.COLOR_RGB2Lab)[:, :, 1]
    l_channel = cv2.cvtColor(pic, cv2.COLOR_RGB2LUV)[:, :, 0]

    if (a_channel > a_thres).sum() > 30: # qualified pixel quantity
        return "RED"
    elif (l_channel > l_thres).sum() > 100: # qualified pixel quantity
        return "YELLOW"
    else:
        return "GREEN"


def TransferColor(origin, ch="a"):
    if ch == "l_lab":
        out = cv2.cvtColor(origin, cv2.COLOR_RGB2Lab)[:, :, 0]
    elif ch == "a":
        out = cv2.cvtColor(origin, cv2.COLOR_RGB2Lab)[:, :, 1]
    elif ch == "b":
        out = cv2.cvtColor(origin, cv2.COLOR_RGB2Lab)[:, :, 2]
    elif ch == "l_luv":
        out = cv2.cvtColor(origin, cv2.COLOR_RGB2LUV)[:, :, 0]
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
    p = PlotPic([TransferColor(day_r, 'a'), TransferColor(day_r, 'l_luv'),
                 TransferColor(day_g, 'a'), TransferColor(day_g, 'l_luv'),
                 TransferColor(day_y, 'a'), TransferColor(day_y, 'l_luv')])
    print(ColorIdentifier(day_r), ColorIdentifier(day_g), ColorIdentifier(day_y))

