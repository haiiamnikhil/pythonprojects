import cv2 as cv
import os
import timeit as time
import pandas as pd
import numpy as np
import openpyxl

# Path below represents the respective path of train images.
# New images can be added to this folder related to the Model.
# If the Path of your local system is different, it can be modified.

path = os.listdir("Models")

# Below is the main function for changing. It automatically categories images and save then on respective folders.

def imagechange():
    bimage = 0
    hist_name = 0
    for images in path:
        bimage=bimage+1
        file = cv.imread(os.path.join("Models",images),0)
        save_dir = os.path.join("bwimage")
        cv.imwrite(os.path.join(save_dir,f"flower{bimage}.jpg"),file)

        # Image convert to HistImage.
        hist_name = hist_name+1

        # Change "file" below to "images" to get the HistImage of the orginal Image
        histimage = cv.equalizeHist(file)
        save_hist_img = os.path.join("histimage")
        cv.imwrite(os.path.join(save_hist_img,f"flower{hist_name}.jpg"),histimage)

        # start_time = time.timeit()
        flatten_image = histimage.flatten()
        # print(flatten_image.shape)
        create_xl = pd.DataFrame(columns=flatten_image)
        create_xl.to_csv('trainfile.csv', mode='a', index=False)
        stop_time = time.timeit()
        # print(start_time - stop_time)
    print("Process Sucess")



# Function avoid the occurence of errors
def callfunction():
    try:
        if os.path.isdir("bwimage") == True and os.path.isdir("histimage") == True:
            imagechange()

        else:
            os.mkdir("histimage")
            os.mkdir("bwimage")
            imagechange()

    except FileExistsError:
        imagechange()

callfunction()