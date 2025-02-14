from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import string
import random

# Function to find the width of the longest item
def get_max_width(items):
    return max(len(item) for item in items)

def change_label_text():
    label.config(text=combo1.get()+"##2"+combo2.get())

v1=[]
root = Tk()
root.geometry('800x500')

root.title('Assertion Generator') 
#label = Label(root, text="test")

frame1=Frame(root,bg='#80c1ff',bd=5)
frame1.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')
lower_frame=Frame(root,bg='#80c1ff',bd=10)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')
v=[]

def checkcmbo():
     if combo1.get() == "Clock Delay":
         if combo2.get() == "2":
             messagebox.showinfo("What user choose", "you choose clock delay")
         else:
             label.config(text=random.choice(string.ascii_letters).lower()+"##"+combo2.get()+random.choice(string.ascii_letters).lower())
     elif combo1.get() == "Implication Operator":
         if combo2.get() == "->":
             label.config(text=random.choice(string.ascii_letters).lower()+combo2.get()+random.choice(string.ascii_letters).lower())
         elif combo2.get() == "=>":
             label.config(text=random.choice(string.ascii_letters).lower()+combo2.get()+random.choice(string.ascii_letters).lower())

def maincombo():
    global combo1, combo2
    Types=["Clock Delay","Implication Operator","Continuous Operator","Consecutive Operator", "Non-Consecutive Operator"]
    label1 = Label(root, text="Type of assertion")
    label1.place(relx=0.28,rely=0.2)
    combo1=Combobox(frame1,values=Types, cursor="hand2")
    max_width = get_max_width(Types)
    combo1.configure(width=max_width)
    combo1.place(relx=0.15,rely=0.25)
    combo1.bind('<<ComboboxSelected>>', combofill)
    label2 = Label(root, text="Value")
    label2.place(relx=0.61, rely=0.2)
    combo2=Combobox(frame1,values=v, cursor="hand2")
    combo2.place(relx=0.55,rely=0.25)
def combofill(event):
    if combo1.get()=="Clock Delay":
        v=[1,2,3,4,5,6,7,8,9,10]
    elif combo1.get()=="Implication Operator":
        v=["->","=>"]
    else:
        v=[]
    combo2.config(values=v)

maincombo()
btn = Button(root, text="Get Assertion",command=checkcmbo, cursor="hand2")
btn.place(relx="0.443",rely="0.2")
label = Label(root, text="Assertion will appear here...", font=("Arial", 25))
label.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()