import cv2 as cv
import numpy as np
import os
path=os.listdir("C:\\Users\\User\\PycharmProjects\\ModelTraining_Python\\Models")
for images in path:
# img = 0
    image = cv.imread(images,0)
    # print(image.shape)
    cv.imshow("image",image)
    cv.waitKey(0)
    cv.destroyAllWindows()