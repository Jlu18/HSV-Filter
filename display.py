from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

from filter.tab_filters import FilterTabs

class Display:
    def __init__(self,root,layout=(1,1),filter=None): 

        self.root = root
        self.filter = filter

        #Dynamic layouts
        self.layout = layout
        self.screen_size = (root.winfo_screenwidth(),root.winfo_screenheight())
        self.calcImgDimension()

        #Upload Button
        self.btn = ttk.Button(self.root,text="Upload",command=self.uploadImg)
        self.btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")

        #Panels
        self.panels = [None]*layout[0]*layout[1]

        print(self.panels[0])

    def uploadImg(self):
        path = filedialog.askopenfilename()
        if(not len(path) > 0):
            return

        #Read image from path
        self.img_cv = cv2.imread(path)

        if(self.img_cv is None):
            print(f"Error: Unable to read file: {path}")
            return
        
        self.updateImg(self.img_cv,0)
    
    def updateImg(self,img,index):
        panel = self.panels[index]
        img_tk = self.cv2tk(img)
        if(panel == None):
            panel = Label(image=img_tk)
            panel.image = img_tk
            panel.pack(side="left",padx=10,pady=10)
        else:
            panel.configure(image=img_tk)
            panel.image = img_tk

# Setter and utility tools
    def setLayout(self,layout): 
        self.layout = layout
        self.calcImgDimension()

    def setScreenSize(self,screen_size):
        self.screen_size = screen_size
        self.calcImgDimension()

    def calcImgDimension(self):
        self.max_dimension = (
            self.screen_size[0]/self.layout[0],
            self.screen_size[1]/self.layout[1]
        )

    def cv2tk(self,img):
        #Convert color format from BGR to RGB
        img = cv2.cvtColor(self.img_cv,cv2.COLOR_BGR2RGB)
        #Convert to PIL format
        img = Image.fromarray(img)
        img.thumbnail(self.screen_max, Image.ANTIALIAS)
        #Convert to Tkinter format
        return ImageTk.PhotoImage(img)


#Entry point
if __name__ == "__main__":
    #Entry point tkinter
    root = Tk()
    root.title("Image Filter")

    FilterTabs(root)
    Display(root)

    #Loop
    root.mainloop()