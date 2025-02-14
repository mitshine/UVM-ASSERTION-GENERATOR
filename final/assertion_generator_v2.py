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
root.wm_iconbitmap('icon.ico')
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
         #if combo2.get() == "2":
         #    messagebox.showinfo("What user choose", "you choose clock delay")
         #else:
         label.config(text="property sample;\n  @(posedge clk) "+random.choice(string.ascii_letters).lower()+"##"+combo2.get()+random.choice(string.ascii_letters).lower()+";\nendproperty\nlabel: assert property (sample);")
     elif combo1.get() == "Implication Operator":
         #if combo2.get() == "->":
         #    label.config(text=random.choice(string.ascii_letters).lower()+combo2.get()+random.choice(string.ascii_letters).lower())
         #elif combo2.get() == "=>":
         label.config(text="property sample;\n  @(posedge clk) "+random.choice(string.ascii_letters).lower()+combo2.get()+random.choice(string.ascii_letters).lower()+";\nendproperty\nlabel: assert property (sample);")
     elif combo1.get() == "Delay Range":
         label.config(text="property sample;\n  @(posedge clk) "+random.choice(string.ascii_letters).lower()+"|->##["+combo2.get()+":"+combo3.get()+"]"+random.choice(string.ascii_letters).lower()+";\nendproperty\nlabel: assert property (sample);")
     elif combo1.get() == "$rose":
         label.config(text="property sample;\n  @(posedge clk)  "+random.choice(string.ascii_letters).lower()+"|->"+combo1.get()+"("+random.choice(string.ascii_letters).lower()+")"+";\nendproperty\nlabel: assert property (sample);")
     elif combo1.get() == "$fell":
         label.config(text="property sample;\n  @(posedge clk)  "+random.choice(string.ascii_letters).lower()+"|->"+combo1.get()+"("+random.choice(string.ascii_letters).lower()+")"+";\nendproperty\nlabel: assert property (sample);")
     elif combo1.get() == "$past":
         label.config(text="property sample;\n  @(posedge clk)  "+random.choice(string.ascii_letters).lower()+"|->("+combo1.get()+"("+random.choice(string.ascii_letters).lower()+", "+str(random.randint(1, 10))+") == 1'b1)"+";\nendproperty\nlabel: assert property (sample);")
     elif combo1.get() == "disable iff":
         label.config(text="property sample;\ndisable iff(reset)\n  @(posedge clk) "+random.choice(string.ascii_letters).lower()+"|->"+"("+random.choice(string.ascii_letters).lower()+")"+";\nendproperty\nlabel: assert property (sample);")
     elif combo1.get() == "Consecutive Repetition Operator":
         label.config(text="property sample;\n  @(posedge clk) $rose("+random.choice(string.ascii_letters).lower()+")|=>"+random.choice(string.ascii_letters).lower()+"[*"+combo2.get()+"]"+"##1"+random.choice(string.ascii_letters).lower()+";\nendproperty\nlabel: assert property (sample);")
     elif combo1.get() == "Go To Repetition Operator":
         label.config(text="property sample;\n  @(posedge clk) $rose("+random.choice(string.ascii_letters).lower()+")|->"+random.choice(string.ascii_letters).lower()+"[->"+combo2.get()+"]"+"##1"+random.choice(string.ascii_letters).lower()+";\nendproperty\nlabel: assert property (sample);")
     elif combo1.get() == "Non-Consecutive Repetition Operator":
         label.config(text="property sample;\n  @(posedge clk) $rose("+random.choice(string.ascii_letters).lower()+")|->"+random.choice(string.ascii_letters).lower()+"[="+combo2.get()+"]"+"##1"+random.choice(string.ascii_letters).lower()+";\nendproperty\nlabel: assert property (sample);")
     elif combo1.get() == "If else inside property":
         label.config(text="property sample;\n  @(posedge clk) $rose("+random.choice(string.ascii_letters).lower()+")|=>\nif("+random.choice(string.ascii_letters).lower()+")\n("+random.choice(string.ascii_letters).lower()+"[->"+combo2.get()+"] ##1 "+random.choice(string.ascii_letters).lower()+")\nelse\n"+"("+random.choice(string.ascii_letters).lower()+"->"+combo2.get()+"] ##1 "+random.choice(string.ascii_letters).lower()+");\nendproperty\n"+"label: assert property(sample);")
     
def maincombo():
    global combo1, combo2, combo3
    #Note: combo3 is only for Delay Range option
    Types=["Clock Delay","Implication Operator","Delay Range","$rose", "$fell", "$stable", "$past", "disable iff", "Consecutive Repetition Operator", "Go To Repetition Operator", "Non-Consecutive Repetition Operator", "If else inside property"]
    label1 = Label(root, text="Type of assertion")
    label1.place(relx=0.28,rely=0.2)
    combo1=Combobox(frame1,values=Types, cursor="hand2")
    max_width = get_max_width(Types)
    combo1.configure(width=max_width)
    combo1.place(relx=0.05,rely=0.25)
    combo1.bind('<<ComboboxSelected>>', combofill)
    label2 = Label(root, text="Values")
    label2.place(relx=0.61, rely=0.2)
    combo2=Combobox(frame1,values=v, cursor="hand2")
    combo2.place(relx=0.45,rely=0.25)
    combo3=Combobox(frame1,values=v, cursor="hand2")
    combo3.place(relx=0.7,rely=0.25)
def combofill(event):
    if combo1.get()=="Clock Delay":
        v=[1,2,3,4,5,6,7,8,9,10]
        w=[]
    elif combo1.get()=="Implication Operator":
        v=["|->","|=>"]
        w=[]
    elif combo1.get()=="Delay Range":
        v=[1,2,3,4,5]
        w=[1,2,3,4,5]
    elif combo1.get()=="Consecutive Repetition Operator":
        v=[1,2,3,4,5]
        w=[]
    elif combo1.get()=="Go To Repetition Operator":
        v=[1,2,3,4,5]
        w=[]
    elif combo1.get()=="Non-Consecutive Repetition Operator":
        v=[1,2,3,4,5]
        w=[]
    elif combo1.get()=="If else inside property":
        v=[1,2,3,4,5]
        w=[]
    else:
        v=[]
        w=[]
    combo2.config(values=v)
    combo3.config(values=w)

maincombo()
btn = Button(root, text="Get Assertion",command=checkcmbo, cursor="hand2")
btn.place(relx="0.443",rely="0.2")
label = Label(root, text="Assertion will appear here...", font=("Arial", 15))
label.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()