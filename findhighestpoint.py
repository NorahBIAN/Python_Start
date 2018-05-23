# -*- coding: utf-8 -*-
"""
Created on Tue May  8 13:39:10 2018

@author: byy
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(1)
levelFlag = False

while(1):

    # Take each frame
    _, frame = cap.read()
    
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of the color of cola in HSV
    #这里问题很严重，阈值应该如何合理的设定，对于视频噪声影响很大
    lower_cola = np.array([0,0,0])
    upper_cola = np.array([180,255,46])
    # Threshold the HSV image to get only cola colors
    mask = cv2.inRange(hsv, lower_cola, upper_cola)
    #filter out noise by GaussianBlur
    maskresult = cv2.GaussianBlur(mask,(5,5),0)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_xor(frame,frame, mask= maskresult)
     # 检索模式为树形cv2.RETR_TREE，
#    image,contours,hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #draw contours on the frame
#    frame = cv2.drawContours(frame, contours, -1, (0,255,0), 3) 

    kernel = np.ones((10,10),np.uint8)
    erosion = cv2.erode(maskresult,kernel,iterations = 1)
    dilation = cv2.dilate(erosion,kernel,iterations = 1)
    
    x,y,w,h = cv2.boundingRect(dilation)
    frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)



    lower_red = np.array([156,43,46])
    upper_red = np.array([180,255,255])    
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    mask1result = cv2.GaussianBlur(mask1,(5,5),0)
    res1 = cv2.bitwise_xor(frame,frame, mask= mask1result)
#    image1,contours1,hierarchy1 = cv2.findContours(mask1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#    frame = cv2.drawContours(frame, contours1, -1, (255,0,0), 2) 
    kernel1 = np.ones((6,6),np.uint8)
    erosion1 = cv2.erode(mask1result,kernel1,iterations = 1)
    dilation1 = cv2.dilate(erosion1,kernel1,iterations = 1)
    
    x1,y1,w1,h1 = cv2.boundingRect(dilation1)
    frame = cv2.rectangle(frame,(x1,y1),(x1+w1,y1+h1),(255,0,0),2)


#    x,y,w,h = cv2.boundingRect(contours[0])
#    frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    
    #output the highest vertical position of the contours

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    
    cv2.imshow('mask1',mask1)
    k = cv2.waitKey(5)& 0xFF
    if y > y1:
        levelFlag = True
    else:
         levelFlag = False
         print('stop pouring')
    
 
    
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()