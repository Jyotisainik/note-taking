import tkinter
from tkinter import *
from PIL import ImageTk,Image
root=Tk()
import os
img=ImageTk.PhotoImage(Image.open("C:\\Users\\A-1\\Documents\\jyoti.jpg"))
panel=Label(root, image=img)
panel.pack(side="bottom",fill="both",expand="yes")
root.mainloop()
