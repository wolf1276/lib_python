# sign in interface
from tkinter import*


root = Tk()
root.geometry("600x300+300+200")
root.title("HVM LIBRARY - SIGN IN")
root.configure(bg='#ffffff')
root.resizable(True,True)

img = PhotoImage(file= 'file-pic.png',)
Label(root,image=img,border=0,bg='#cccccc').place(x=200,y=-8)




frame=Frame(root,width=0,height=0,bg='#FF0000')
frame.place(x=0,y=0)

heading=Label(text='SIGN IN',fg="#000000",bg='white',font=('Poppins sans serif',22,))
heading.place(x=65,y=55)




root.mainloop()