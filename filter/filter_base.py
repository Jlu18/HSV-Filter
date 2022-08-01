from abc import abstractmethod

#Base abstract class for any filter added to manipulate images
#Any inherited class must construct a widget in tkinter
#   and have a function that takes img and returned a filtered version of the image
class FilterBase:
    def __init__(self,root,callback):
        self.root = root
        self.callback = callback
        self.img = None

    #Function to manipulate the image
    #At the end make sure to invoke callback to send back the image to filter tab
    @abstractmethod
    def applyFilter(self):
        pass

    def setImage(self,img):
        self.img = img

