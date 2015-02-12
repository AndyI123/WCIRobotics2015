__author__ = 'hc'

from Tkinter import *

#So hacky :)
myself = current_module = sys.modules[__name__];

#WARNING:
#After show_menu() is invoked, the menu's buttons are reset!

#This is a very basic menu
def init_menu():
    myself.root = Tk()
    myself.frame = Frame(myself.root)
    myself.frame.pack()

    myself.button = Button(
        myself.frame, text="QUIT", fg="red", command=myself.suicide)
    myself.button.pack(side=LEFT)
    myself.buttonList = []

def add_button(text, function, side):
    if(side == "LEFT"):
        side=LEFT
    elif(side == "RIGHT"):
        side=RIGHT
    button = Button(myself.root, text=text, command=function)
    button.pack(side=side)
    myself.buttonList.append(button) # Keep a reference so the button stays :)

#Makes the window commit suicide :)
def suicide():
    myself.root.quit()
    myself.root.destroy()
    reload(myself) #reload myself :)

def show_menu():
    myself.root.mainloop()
    myself.root.quit()
    reload(myself) #reload myself :)
    #myself.root.destroy() # makes sure the program ends properly :|