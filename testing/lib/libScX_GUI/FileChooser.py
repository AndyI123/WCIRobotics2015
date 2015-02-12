import sys

__author__ = 'hc'

#This opens a file chooser

from Tkinter import Tk
from tkFileDialog import askopenfilename

#So hacky :)
myself = current_module = sys.modules[__name__];

def fileChooser(title):
    root = Tk()
    root.withdraw() #Prevent window from appearing
    filename = askopenfilename(title=title) # show an "Open" dialog box and return the path to the selected file
    root.quit()
    root.destroy()
    reload(myself)
    return filename