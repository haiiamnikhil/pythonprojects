import numpy as np
import cv2
import pandas as pd

image = cv2.imread("lotus.jpg",0)
cv2.imshow("testimage",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(np.shape(image))
reshaped = image.flatten()
print(reshaped)
new_image = cv2.imshow("changed",reshaped)
cv2.waitKey(0)
cv2.destroyAllWindows()