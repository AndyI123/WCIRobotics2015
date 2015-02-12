__author__ = 'hc'

#This shows an image file since image.show() is lame...

#WARNING:
#This class depends on ImageTK, if it is not installed on your computer, this will throw an error
#There are many ways to install it, for example on Debian, you must install this package: python-imaging-tk

from PIL import ImageTk
import PIL.Image
from Tkinter import *

#So hacky :)
myself = current_module = sys.modules[__name__];

def showImage(imageFile, caption):
    root = Tk()

    #Set the window title
    root.wm_title(caption)

    #Sorry guys, I have to do this because I'm too lazy to make the image dynamically resize
    root.resizable(width=FALSE, height=FALSE)

    image = PIL.Image.open(imageFile)
    photo = ImageTk.PhotoImage(image, master=root)

    #And we also have to resize the window to the image size...
    width,height=image.size
    root.geometry('{}x{}'.format(width, height))

    label = Label(root, image=photo)
    label.image = photo
    label.pack(expand=True, fill=BOTH)
    root.mainloop()
    root.quit()

    #Clear all the variables? Is this necessary? I'll put it here just in case...
    reload(myself)