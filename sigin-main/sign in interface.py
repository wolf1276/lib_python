# sign in interface
from tkinter import*


root = Tk()
root.geometry("600x300+300+200")
root.title("HVM LIBRARY - SIGN IN")
root.configure(bg='#ffffff')
root.resizable(False,False)

img = PhotoImage(file= 'startup.png',)
Label(root,image=img,border=0,bg='#cccccc').place(x=250,y=-8)

frame=Frame(root,width=0,height=0,bg='#ff0000')
frame.place(x=50,y=-50)

heading=Label(text='Sign in',fg="#000000",bg='white',font=('Poppins sans serif',22,))
heading.place(x=75,y=55)



root.mainloop()