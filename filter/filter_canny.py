from tkinter import *
import cv2

from filter.filter_base import FilterBase

class CannyFilter(FilterBase):
    def __init__(self,root):
        super().__init__(root)

        self.var_min = DoubleVar()
        self.var_max = DoubleVar()

        self.s_min = Scale(root,label="MIN THRESHOLDS: ",variable=self.var_min,from_=0,to=255,length=600,orient=HORIZONTAL)
        self.s_max = Scale(root,label="MAX THRESHOLDS: ",variable=self.var_max,from_=0,to=255,length=600,orient=HORIZONTAL)
        
        self.s_min.pack(anchor=CENTER)
        self.s_max.pack(anchor=CENTER)

        #TODO Add option to edit aperature size (ie kernel that should be range between 3-7 with odd number only)

    def applyFilter(self,img):

        min = self.var_min.get()
        max = self.var_max.get()

        return cv2.Canny(img,max,min)