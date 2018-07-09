import tkinter
from tkinter import *
import pymysql
db=pymysql.connect('localhost','root','system','notetaking')
cursor=db.cursor()
def notes_insert():
    name=entry1.get()
    print(name)
    subject=entry2.get()
    print(subject)
    notes=T.get('1.0','end')
    print(notes)
    qr1="insert into notetaking values('"+name+"','"+subject+"','"+notes+"');"
    try:
        cursor.execute(qr1)
        db.commit()
    except:
        db.rollback()


# def myListbox():
#     root = Tk()
#     root.title('List')
#     root.geometry('200x150+200+150')

root=Tk()
T=Text(root,height=20,width=50)
T.place(x=150,y=250)
#T.insert(END,"Hey Everyone\nThis is an MY Note Taking\n")
root.title("Note Taking")
root.geometry("500x500")
root.minsize(700,700)
root.maxsize(500,500)
b=Button(text='exit',width=25,command=25,borderwidth=5)
b.place(x=250,y=670)
b=Button(text='save',width=25,borderwidth=5,command=notes_insert)
b.place(x=250,y=630)
b=Button(text='Search Notes',width=11,command=25,borderwidth=1)
b.place(x=615,y=150)
label=Label(text="Welcome to NOTETAKING APP",fg='blue',font=20)
label.place(x=250,y=10)

entry1=Entry(root,width='20',border=3)
entry1.place(x=280,y=40)
entry1.insert(0,'Name')
entry2=Entry(root,width='20',border=3)
entry2.place(x=280,y=80)
entry2.insert(0,'subject')
entry3=Entry(root,width='100',border=3)
entry3.place(x=5,y=150)





root.mainloop()
