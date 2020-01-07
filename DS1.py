# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 20:53:22 2019

@author: RIO
"""

import  cv2
import numpy as np
#D:\Py_Workspace_spyder_Project\img
from matplotlib import pyplot as plt

img = cv2.imread('D:\\Py_Workspace_spyder_Project\\img\watch.jpg',cv2.IMREAD_GRAYSCALE)

"""
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
plt.show()

