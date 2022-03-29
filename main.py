from tkinter import *

from filter.tab_filters import FilterTabs
from input import InputDisplay
from output import OutputDisplay

#Entry point
if __name__ == "__main__":
    #Entry point tkinter
    root = Tk()
    root.title("Image Filter")

    filters = FilterTabs(root)
    InputDisplay(root,filters)
    OutputDisplay(root,filters)

    #Loop
    root.mainloop()