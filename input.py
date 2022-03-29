from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

class InputDisplay:
    def __init__(self,root,filters): 

        self.panel = None

        self.root = root
        self.filters = filters
        
        self.max_dimension = (root.winfo_screenwidth()/2,root.winfo_screenheight()/2)

        #Upload Button
        self.btn = ttk.Button(self.root,text="Upload",command=self.uploadImg)
        self.btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")

    def uploadImg(self):
        path = filedialog.askopenfilename()
        if(not len(path) > 0):
            return

        #Read image from path
        self.img_cv = cv2.imread(path)

        if(self.img_cv is None):
            print(f"Error: Unable to read file: {path}")
            return

        #send the img to filter
        self.filters.setInputImage(self.img_cv)

        #Convert color format from BGR to RGB
        img = cv2.cvtColor(self.img_cv,cv2.COLOR_BGR2RGB)

        #Convert to PIL format
        img = Image.fromarray(img)
        print(self.max_dimension)
        img.thumbnail(self.max_dimension, Image.ANTIALIAS)
        
        #Convert to Tkinter format
        img_tk = ImageTk.PhotoImage(img)
        
        if(self.panel == None):
            self.panel = Label(image=img_tk)
            self.panel.image = img_tk
            self.panel.pack(side="left",padx=10,pady=10)
        else:
            self.panel.configure(image=img_tk)
            self.panel.image = img_tk