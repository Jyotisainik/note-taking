# import tkinter
# from tkinter import *
# from PIL import ImageTk,Image
# root=Tk()
# import os
# img=ImageTk.PhotoImage(Image.open("C:\\Users\\A-1\\Documents\\jyoti.jpg"))
# panel=Label(root, image=img)
# panel.pack(side="bottom",fill="both",expand="yes")
# root.mainloop()


import tkinter
from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Note Taking")
root.geometry("300x300")
root.resizable(False,False)
root.minsize(700,700)
root.maxsize(300,300)
import os
img=ImageTk.PhotoImage(Image.open("C:\\Users\\A-1\\Documents\\jyoti.jpg"))
panel=Label(root, image=img)
panel.pack(side="top",fill="both",expand="yes")
b = Button(root, text='insert', width=25, borderwidth=5)
b.place(x=35, y=55)
b = Button(root, text='update', width=11, borderwidth=5)
b.place(x=40, y=15)
b = Button(root, text='delete', width=11, borderwidth=5)
b.place(x=40, y=15)

root.mainloop()

