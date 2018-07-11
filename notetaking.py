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




def notes_update():

    update_root = Tk()
    update_root.title("Notes")

    update_root.geometry("500x500")
    update_root.minsize(500,500)
    update_root.maxsize(700,700)
    T = Text(update_root, height=20, width=50)
    T.place(x=45,y=80)
    entry4 = Entry(update_root, width='20', border=3)
    entry4.place(x=28, y=20)
    entry4.insert(0, 'Name')
    entry5 = Entry(update_root, width='20', border=3)
    entry5.place(x=23, y=10)
    entry5.insert(0, 'subject')
    entry6 = Entry(update_root, width='100', border=3)
    entry6.place(x=5, y=150)
    label=Label(update_root,text="Welcome to NOTETAKING APP",fg='blue', font='bold 10')
    label.place(x=150,y=10)
    b = Button(update_root,text='Save', width=25,borderwidth=5)
    b.place(x=20,y=450)
    b = Button(update_root, text='Cancel', width=25, borderwidth=5)
    b.place(x=285,y=450)
    name = entry4.get()
    subject = entry5.get()
    print(subject)
    notes = T.get('1.0', 'end')
    print(notes)
    qr1 = "insert into notetaking values('" + name + "','" + subject + "','" + notes + "');"
    try:
        cursor.execute(qr1)
        db.commit()
    except:
        db.rollback()
        update_root.mainloop()



def delete_notes():
    delete_root = Tk()
    delete_root.title("notes")
    delete_root.geometry("500x500")
    delete_root.minsize(500,500)
    delete_root.maxsize(700,700)
    delete_root.resizable(False, False)
    T = Text(delete_root, height=20, width=50)
    T.place(x=45, y=80)
    label = Label(delete_root, text="Welcome to NOTETAKING APP", fg='blue', font='bold 10')
    label.place(x=150, y=10)
    b = Button(delete_root, text='Save', width=25, borderwidth=5)
    b.place(x=20, y=450)
    b = Button(delete_root, text='Cancel', width=25, borderwidth=5)
    b.place(x=285, y=450)
    delete_root.mainloop()

    # def notes_insert3():
    #     name = entry7.get()
    #     print(name)
    #     subject = entry8.get()
    #     print(subject)
    #     notes = T.get('1.0', 'end')
    #     print(notes)
    #     qr1 = "insert into notetaking values('" + name + "','" + subject + "','" + notes + "');"
    #     try:
    #         cursor.execute(qr1)
    #         db.commit()
    #     except:
    #         db.rollback()
    #
    # entry7 = Entry(delete_root, width='20', border=3)
    # entry7.place(x=10, y=10)
    # entry7.insert1(0, 'Name')
    # entry8 = Entry(delete_root, width='20', border=3)
    # entry8.place(x=20, y=20)
    # entry8.insert2(0, 'subject')
    # entry9= Entry(delete_root, width='100', border=3)
    # entry9.place(x=4, y=10)


root=Tk()
T=Text(root,height=20,width=50)
T.place(x=150,y=250)
T.insert(END,"Hey Everyone\nThis is an MY Note Taking\n")
root.title("Note Taking")
root.geometry("500x500")
root.minsize(700,700)
root.maxsize(500,500)
b=Button(text='exit',width=25,command=25,borderwidth=5)
b.place(x=250,y=670)
b=Button(text='save',width=25,borderwidth=5,command=notes_insert)
b.place(x=250,y=630)
# b=Button(text='Search Notes',width=11,command=25,borderwidth=1)
# b.place(x=615,y=150)
label=Label(text="Welcome to NOTETAKING APP",fg='blue',font='bold 10')
label.place(x=250,y=10)
b=Button(text='update',width=11,command=notes_update,borderwidth=9)
b.place(x=50,y=40)
b=Button(text='delete',width=11,command=delete_notes,borderwidth=9)
b.place(x=540,y=40)


entry1=Entry(root,width='20',border=3)
entry1.place(x=280,y=40)
entry1.insert(0,'Name')
entry2=Entry(root,width='20',border=3)
entry2.place(x=280,y=80)
entry2.insert(0,'subject')
entry3=Entry(root,width='100',border=3)
entry3.place(x=5,y=150)







root.mainloop()
