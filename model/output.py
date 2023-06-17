# -*- coding: utf-8 -*-
"""output.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10lR01-X8BZYcHBMkcE9QhZPQICE8Slnr
"""

import cv2
from PIL import Image
# create.png
img = cv2.imread('./instance-level_human_parsing/instance-level_human_parsing/Training/Images/0001255.jpg') 

# mask.png
mask = cv2.imread('/content/drive/MyDrive/project/mask.png')  

mask = cv2.resize(mask, (img.shape[1], img.shape[0]))
output = cv2.bitwise_and(img, mask)

cv2.imwrite("output.png", output)

def convertImage():
    img = Image.open('output.png')
    img = img.convert("RGBA")
 
    datas = img.getdata()
 
    newData = []
 
    for item in datas:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
 
    img.putdata(newData)
    img.save("/content/drive/MyDrive/project/output.png", "PNG")
    print("Successful")
    
convertImage()