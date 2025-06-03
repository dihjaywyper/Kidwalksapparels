from tkinter import *

window=Tk()

window.title('Main menu')
window.geometry('1270x668+0+0')
window.resizable(0,0)
window.config(bg='white')

titleLabel=Label(window,text='  Kidwalks Apparels-Staff and Inventory Management system',font=('times new roman',30, 'bold'),bg='#010c48',fg='white',anchor='w')
titleLabel.place(x=0,y=0,relwidth=1)

logoutButton=Button(window,text='logout',font=('times new roman',15,'bold'),fg='#010c48')
logoutButton.place(x=1180,y=5)

window.mainloop()
