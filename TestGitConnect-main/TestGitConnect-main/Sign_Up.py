# GUI Test
from tkinter import *
from tkinter import messagebox
import ast

root = Tk()
root.geometry("500x300+300+200")
root.title("HVM Library - SIGN UP")
root.configure(bg='#ffffff')
root.resizable(False,False)

img = PhotoImage(file= 'SignUp10.png',)
Label(root,image=img,border=0,bg='#cccccc').place(x=80,y=20)

frame=Frame(root,width=300,height=400,bg='#ffffff')
frame.place(x=0,y=-50)

heading=Label(frame,text='Sign Up',fg="#57a1f8",bg='white',font=('Microsoft Yahei UI Light',18,'bold'))
heading.place(x=100,y=80)

def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    if user.get()=='':
        user.insert(0,'Username')
user = Entry(frame,width=35,fg='black',border=0,bg='#ffffff',font=('Microsoft Yahei UI Light',8))
user.place(x=50,y=150)
user.insert(0, 'Username')
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)
Frame(frame,width=200,height=2,bg='black').place(x=50,y=165)
def on_enter(e):
    user_id.delete(0,'end')
def on_leave(e):
    if user_id.get()=='':
        user.insert(0,'User ID')
user_id = Entry(frame,width=35,fg='black',border=0,bg='#ffffff',font=('Microsoft Yahei UI Light',8))
user_id.place(x=50,y=170)
user_id.insert(0, 'User ID')
user_id.bind("<FocusIn>",on_enter)
user_id.bind("<FocusOut>",on_leave)
def on_enter(e):
    passw.delete(0,'end')
Frame(frame,width=200,height=2,bg='black').place(x=50,y=185)
def on_leave(e):
    if passw.get()=='':
        passw.insert(0,'Password')
passw = Entry(frame,width=35,fg='black',border=0,bg='#ffffff',font=('Microsoft Yahei UI Light',8))
passw.place(x=50,y=190)
passw.insert(0, 'Password')
passw.bind("<FocusIn>",on_enter)
passw.bind("<FocusOut>",on_leave)
Frame(frame,width=200,height=2,bg='black').place(x=50,y=205)
def on_enter(e):
    cpassw.delete(0,'end')
def on_leave(e):
    if cpassw.get()=='':
        cpassw.insert(0,'Confirm Password')
cpassw = Entry(frame,width=35,fg='black',border=0,bg='#ffffff',font=('Microsoft Yahei UI Light',8))
cpassw.place(x=50,y=210)
cpassw.insert(0, 'Confirm Password')
cpassw.bind("<FocusIn>",on_enter)
cpassw.bind("<FocusOut>",on_leave)
Frame(frame,width=200,height=2,bg='black').place(x=50,y=225)

Button(frame,width=15,pady=3,text='Sign Up',bg='#57a1f8',fg='white',border=0).place(x=100,y=250)
label=Label(frame,text='I have an account |',fg='black',bg='white',cursor='hand2',font=('Microsoft Yahei UI Light',8))
label.place(x=90,y=320)
signin=Button(frame,text='Sign In',border=0,bg='white',cursor='hand2',fg='#57a1f8')
signin.place(x=190,y=320)
root.mainloop()