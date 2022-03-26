from abc import abstractmethod

#Base abstract class for any filter added to manipulate images
#Any inherited class must construct a widget in tkinter
#   and have a function that takes img and returned a filtered version of the image
class FilterBase:
    def __init__(self,root):
        self.root = root

    #Function to manipulate the image
    @abstractmethod
    def applyFilter(self,img):
        return img

