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
                val = HSVFilter(tab)
            elif name == "Canny":
                val = CannyFilter(tab)
            self.filters[name] = val

        self.notebook.pack(expand = 1, fill="both")


    def currentFilter(self):
        text = self.notebook.tab(self.notebook.select(), "text")
        return self.filters[text]
        
