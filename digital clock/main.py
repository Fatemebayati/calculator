from tkinter import *
import time
window=Tk()
window.title("Digital Clock")
window.geometry('600x400')

def mytime():
    hour=time.strftime('%I')
    minute=time.strftime('%M')
    second=time.strftime('%S')
    pm_am=time.strftime('%p')
    day=time.strftime('%A')
    zone=time.strftime('%Z')
    mytext=hour+":"+minute+":"+second+" "+pm_am
    mytext2=day+", "+zone
    mylabel.config(text=mytext)
    mylabel2.config(text=mytext2)
    mylabel.after(1000,mytime)

mylabel=Label(window,text="",font=('Arial',66),fg='white', bg='black')
mylabel2=Label(window,text="",font=("Arial",28))
mylabel.pack()
mylabel2.pack()
mytime()
window.mainloop()