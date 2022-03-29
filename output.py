from tkinter import *
import cv2
from PIL import Image, ImageTk

class OutputDisplay:
    def __init__(self,root,filters):
        self.root = root
        self.filters = filters
        self.filters.onOutputRecieved(self.receiveOutput)
        self.max_dimension = (root.winfo_screenwidth()/2,root.winfo_screenheight()/2)

        self.panel = None

    def receiveOutput(self,imgs):
        #Convert color format from BGR to RGB
        img = cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)

        #Convert to PIL format
        img = Image.fromarray(img)
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