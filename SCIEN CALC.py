 
from tkinter import *
from tkinter import ttk
import tkinter
from math import sin,cos,tan,log,e,log10,sqrt

root=Tk()
root.title("CALCULATOR")
root.configure(bg="black")
root.geometry("350x400")
root.maxsize(400,400)

operator = ""
text_Input = StringVar()

def Click(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def eval_all():
  try:
    global operator
    s=str(eval(operator)) 
    text_Input.set(s)
    operator=""
  except:
    s="ERROR!!!"
    text_Input.set(s)

#def clear():
    #entru.delete(0,END)

def clear(): 
    global operator
    operator = "" 
    text_Input.set("")
    
def backspace():
  global operator
  operator=""
  text_Input.set(text_Input.get()[0:-1])




temp=0
def ans_func():
    global operator
    operator=""
    entru.insert(0,operator)

def round_off():
  global operator
  opertaor=""
  entru.delete(-1,END)

#def sin_func():
  #text_Input.set("sin(")
  #p=str()
  
#def quit():
#   root.destroy()

entru=Entry(root,foreground="Black",background="white",font="verdana,bold",bd=3,textvariable=text_Input,relief=SUNKEN)
entru.place(width=157,height=30,x=80,y=119)

g=Button(root,text=1,bg="black",foreground="cyan",height=1,width=2,font="Verdana",relief=RAISED,command=lambda:Click(1))
g.place(x=119,y=246)
k=Button(root,text=2,foreground="cyan",bg="black",height=1,width=2,font="Verdana",relief=RAISED,command=lambda:Click(2))
#k.grid(row=10,column=1)
k.place(x=149,y=246)
l=Button(root,text=3,foreground="cyan",bg="black",height=1,width=2,font="Verdana",relief=RAISED,command=lambda:Click(3))
#l.grid(row=10,column=2)
l.place(x=179,y=246)
o=Button(root,text=4,foreground="cyan",bg="black",height=1,width=2,font="Verdana",relief=RAISED,command=lambda:Click(4))
#o.grid(row=9,column=0)
o.place(x=119,y=214)
y=Button(root,text=5,foreground="cyan",bg="black",height=1,width=2,font="Verdana",relief=RAISED,command=lambda:Click(5))
#y.grid(row=9,column=1)
y.place(x=149,y=214)
i=Button(root,text=6,foreground="cyan",bg="black",height=1,width=2,font="Verdana",relief=RAISED,command=lambda:Click(6))
#i.grid(row=9,column=2)
i.place(x=179,y=214)
j=Button(root,text=7,foreground="cyan",bg="black",height=1,width=2,font="Verdana",relief=RAISED,command=lambda:Click(7))
#j.grid(row=8,column=0)
j.place(x=119,y=182)
m=Button(root,text=8,foreground="cyan",bg="black",height=1,width=2,font="Verdana",relief=RAISED,command=lambda:Click(8))
#m.grid(row=8,column=1)
m.place(x=149,y=182)
n=Button(root,text=9,foreground="cyan",bg="black",height=1,width=2,font="Verdana",relief=RAISED,command=lambda:Click(9))
#n.grid(row=8,column=2)
n.place(x=179,y=182)
e=Button(root,text=0,foreground="cyan",bg="black",height=1,width=2,font="Verdana",relief=RAISED,command=lambda:Click(0))
#e.grid(row=11,column=1)
e.place(x=149,y=278)


s_sum=Button(root,text="+",bg="black",foreground="yellow",height=1,width=2,font="Verdana",relief=RAISED,command=lambda:Click("+"))
#s_sum.grid(row=10,column=3)
s_sum.place(x=209,y=246)
f_sub=Button(root,text="-",bg="black",foreground="yellow",height=1,width=2,font="Verdana",relief=RAISED,command=lambda:Click("-"))
#f_sub.grid(row=9,column=3)
f_sub.place(x=209,y=214)
h_mul=Button(root,text="x",bg="black",foreground="yellow",height=1,width=2,font="Verdana",relief=RAISED,command=lambda:Click("*"))
#h_mul.grid(row=8,column=3)
h_mul.place(x=209,y=182)
r_div=Button(root,text="÷",bg="black",foreground="yellow",height=1,width=2,font="Verdana",relief=RAISED,command=lambda:Click("/"))
#r_div.grid(row=7,column=3)
r_div.place(x=209,y=150)


r_root=Button(root,text="^",bg="black",foreground="yellow",height=1,width=2,font="Verdana",command=lambda:Click("^"))
r_root.place(x=179,y=150)
c_clear=Button(root,text="AC",bg="black",fg="yellow",height=1,width=2,font="Verdana",command=lambda:clear())
c_clear.place(x=119,y=278)
P_point=Button(root,text=".",bg="black",foreground="yellow",height=1,width=2,font="Verdana",command=lambda:Click("."))
P_point.place(x=179,y=278)
ans=Button(root,text="=",bg="black",fg="yellow",height=1,width=2,font="Verdana",command=eval_all)
ans.place(x=209,y=278)
back_space=Button(root,text="⌫",bg="black",fg="yellow",height=1,width=3,font="Verdana",command=backspace)
back_space.place(x=239,y=118)
x=Button(root,text="Ans",bg="black",fg="yellow",height=1,width=3,font="Verdana",command=ans_func)
x.place(x=79,y=150)
Brac_open=Button(root,text="(",bg="black",fg="yellow",height=1,width=2,font="Verdana",command=lambda:Click("("))
Brac_open.place(x=119,y=150)
Brac_close=Button(root,text=")",bg="black",fg="yellow",height=1,width=2,font="Verdana",command=lambda:Click(")"))
Brac_close.place(x=149,y=150) 
sin_func=Button(root,text="sin",bg="black",fg="yellow",height=1,width=3,font="Verdana",command=lambda:Click("sin("))
sin_func.place(x=239,y=278)
cos_func=Button(root,text="cos",bg="black",fg="yellow",height=1,width=3,font="Verdana",command=lambda:Click("cos("))
cos_func.place(x=239,y=246)
tan_func=Button(root,text="tan",bg="black",fg="yellow",height=1,width=3,font="Verdana",command=lambda:Click("tan("))
tan_func.place(x=239,y=214)
Fact_mode=Button(root,text="!",bg="black",fg="yellow",height=1,width=3,font="Verdana",command=lambda:Click("math.factorial("))
Fact_mode.place(x=79,y=278)
ln_func=Button(root,text="ln",bg="black",fg="yellow",height=1,width=3,font="Verdana",command=lambda:Click("log("))
ln_func.place(x=239,y=182)
log_func=Button(root,text="log",bg="black",fg="yellow",height=1,width=3,font="Verdana",command=lambda:Click("log("))
log_func.place(x=239,y=150)
Sqrt_func=Button(root,text="√ ",bg="black",fg="yellow",height=1,width=2,font="Verdana",command=lambda:Click("sqrt("))
Sqrt_func.place(x=179,y=150)
pow_func=Button(root,text="e",bg="black",fg="yellow",height=1,width=3,font="Verdana",command=lambda:Click("exp("))
pow_func.place(x=79,y=246)
#open_func=Button(root,text="2nd",bg="black",fg="yellow",height=1,width=2,font="Verdana",command=lambda:Click(open=))
#open_func.place(x=260,y=150)
deg_conv=Button(root,text="Deg",bg="black",fg="yellow",height=1,width=3,font="Verdana",command=lambda:Click("math.degrees("))
deg_conv.place(x=79,y=214)
rad_conv=Button(root,text="Rad",bg="black",fg="yellow",height=1,width=3,font="Verdana",command=lambda:Click("math.radians("))
rad_conv.place(x=79,y=182)
#X=Button(root,text="X",bg="black",fg="yellow",height=1,width=3,font="Verdana",command=quit)
#X.place(x=310,y=2)
root.mainloop()









