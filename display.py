from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import numpy as np
import cv2
from PIL import Image, ImageTk

class ImgDisplay:
    def __init__(self,max_width,max_height): 
        #Display normal image
        self.panel =None

        #Filtered Image
        self.panel_filter = None

        #OpenCV version of Image so it does filetering
        self.img_cv = None

        self.prev_min = (0,0,0)
        self.prev_max = (0,0,0)

        self.screen_max = (max_width/2,max_height/2)

    def uploadImg(self):
        path = filedialog.askopenfilename()
        if(not len(path) > 0):
            return

        #Read image from path
        self.img_cv = cv2.imread(path)

        if(self.img_cv is None):
            print(f"Error: Unable to read file: {path}")
            return

        #Convert color format from BGR to RGB
        img = cv2.cvtColor(self.img_cv,cv2.COLOR_BGR2RGB)
        #Convert to PIL format
        img = Image.fromarray(img)
        img.thumbnail(self.screen_max, Image.ANTIALIAS)
        #Convert to Tkinter format
        img = ImageTk.PhotoImage(img)

        if(self.panel == None):
            self.panel = Label(image=img)
            self.panel.image = img
            self.panel.pack(side="left",padx=10,pady=10)
        else:
            #Attach image to the panel
            self.panel.configure(image=img)
            #reserve image to panel so it doesn't remove when collected by gc
            self.panel.image = img

        #Convert GBR to HSV
        self.img_cv = cv2.cvtColor(self.img_cv,cv2.COLOR_BGR2HSV)
        self.filterUpdate()
    
    def filterUpdate(self,min=None,max=None):
        if(self.img_cv is None):
            return

        if(min==None):
            min = self.prev_min
        if(max==None):
            max = self.prev_max

        img_filter = cv2.inRange(self.img_cv,min,max)
        self.prev_min = min
        self.prev_max = max

        img_filter = Image.fromarray(img_filter)
        img_filter.thumbnail(self.screen_max, Image.ANTIALIAS)
        img_filter = ImageTk.PhotoImage(img_filter)

        if(self.panel_filter == None):
            self.panel_filter = Label(image=img_filter)
            self.panel_filter.image = img_filter
            self.panel_filter.pack(side="left",padx=10,pady=10)
        else:
            self.panel_filter.configure(image=img_filter)
            self.panel_filter.image = img_filter


class FilterSlider:
    def __init__(self,root,img=None):

        if(type(img) is not ImgDisplay):
            print("Warn: No target image to set the filter")
            self.displayImg = None
        else:
            self.displayImg = img
        
        self.root = root

        self.var_h_min = DoubleVar()
        self.var_h_max = DoubleVar()
        self.var_s_min = DoubleVar()
        self.var_s_max = DoubleVar()
        self.var_v_min = DoubleVar()
        self.var_v_max = DoubleVar()

        self.s_h_min = Scale(root,label="HUE MIN:        ",variable=self.var_h_min,from_=0,to=360,length=600,orient=HORIZONTAL,command=self.updateValues)
        self.s_h_max = Scale(root,label="HUE MAX:        ",variable=self.var_h_max,from_=0,to=360,length=600,orient=HORIZONTAL,command=self.updateValues)

        self.s_s_min = Scale(root,label="SATURATION MIN: ",variable=self.var_s_min,from_=0,to=255,length=600,orient=HORIZONTAL,command=self.updateValues)
        self.s_s_max = Scale(root,label="SATURATION MAX: ",variable=self.var_s_max,from_=0,to=255,length=600,orient=HORIZONTAL,command=self.updateValues)

        self.s_v_min = Scale(root,label="VALUE MIN:      ",variable=self.var_v_min,from_=0,to=255,length=600,orient=HORIZONTAL,command=self.updateValues)
        self.s_v_max = Scale(root,label="VALUE MAX:      ",variable=self.var_v_max,from_=0,to=255,length=600,orient=HORIZONTAL,command=self.updateValues)

        self.s_h_min.pack(anchor=CENTER)
        self.s_h_max.pack(anchor=CENTER)
        self.s_s_min.pack(anchor=CENTER)
        self.s_s_max.pack(anchor=CENTER)
        self.s_v_min.pack(anchor=CENTER)
        self.s_v_max.pack(anchor=CENTER)

    def updateValues(self,*args):
        if(self.displayImg is None):
            print("Warn.updateValues: displayImg is not intialized")
            return
        
        self.displayImg.filterUpdate(
            (self.var_h_min.get(), self.var_s_min.get(), self.var_v_min.get()),
            (self.var_h_max.get(), self.var_s_max.get(), self.var_v_max.get())
        )

if __name__ == "__main__":
    
    #Entry point tkinter
    root = Tk()
    root.title("HSV Filter Slider")

    display = ImgDisplay(root.winfo_screenwidth(),root.winfo_screenheight())
    slider = FilterSlider(root,display)

    #Upload Button
    btn = ttk.Button(root,text="Upload",command=display.uploadImg)
    btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")

    #Loop
    root.mainloop()