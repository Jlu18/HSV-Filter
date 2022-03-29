from tkinter import *
from tkinter import ttk

from filter.filter_canny import CannyFilter
from filter.filter_hsv import HSVFilter

class FilterTabs:
    def __init__(self,root):
        #List of available filters
        self.filters = {
            "HSV":None,
            "Canny":None
        }

        self.root = root
        self.notebook = ttk.Notebook(root)

        for name,_ in self.filters.items():
            tab = ttk.Frame(self.notebook)
            self.notebook.add(tab,text=name)

            if name == "HSV":
                val = HSVFilter(tab,self.onFilterGenerated)
            elif name == "Canny":
                val = CannyFilter(tab,self.onFilterGenerated)
            self.filters[name] = val

        self.notebook.pack(expand = 1, fill="both")
        self.notebook.bind('<<NotebookTabChanged>>',self.setCurrentTab)
    
    def setInputImage(self,img):
        self.input = img
        self.currentFilter.setImage(img)
    
    def setCurrentTab(self, *args):
        text = self.notebook.tab(self.notebook.select(), "text")
        self.currentFilter = self.filters[text]
        self.currentFilter.applyFilter()

    def onOutputRecieved(self,callback):
        self.callback = callback

    def onFilterGenerated(self,img):
        self.callback(img)

        

