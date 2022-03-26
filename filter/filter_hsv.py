from tkinter import *
import cv2

from .filter_base import FilterBase

class HSVFilter(FilterBase):
    def __init__(self,root):
        super().__init__(root)

        self.var_h_min = DoubleVar()
        self.var_h_max = DoubleVar()
        self.var_s_min = DoubleVar()
        self.var_s_max = DoubleVar()
        self.var_v_min = DoubleVar()
        self.var_v_max = DoubleVar()

        self.s_h_min = Scale(root,label="HUE MIN:        ",variable=self.var_h_min,from_=0,to=360,length=600,orient=HORIZONTAL)
        self.s_h_max = Scale(root,label="HUE MAX:        ",variable=self.var_h_max,from_=0,to=360,length=600,orient=HORIZONTAL)

        self.s_s_min = Scale(root,label="SATURATION MIN: ",variable=self.var_s_min,from_=0,to=255,length=600,orient=HORIZONTAL)
        self.s_s_max = Scale(root,label="SATURATION MAX: ",variable=self.var_s_max,from_=0,to=255,length=600,orient=HORIZONTAL)

        self.s_v_min = Scale(root,label="VALUE MIN:      ",variable=self.var_v_min,from_=0,to=255,length=600,orient=HORIZONTAL)
        self.s_v_max = Scale(root,label="VALUE MAX:      ",variable=self.var_v_max,from_=0,to=255,length=600,orient=HORIZONTAL)

        self.s_h_min.pack(anchor=CENTER)
        self.s_h_max.pack(anchor=CENTER)
        self.s_s_min.pack(anchor=CENTER)
        self.s_s_max.pack(anchor=CENTER)
        self.s_v_min.pack(anchor=CENTER)
        self.s_v_max.pack(anchor=CENTER)
    

    def applyFilter(self,img):
        if(img is None):
            return

        min = (self.var_h_min.get(), self.var_s_min.get(), self.var_v_min.get())
        max = (self.var_h_max.get(), self.var_s_max.get(), self.var_v_max.get())

        return cv2.inRange(img,min,max)

        
        
