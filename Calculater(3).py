#to import tkinter module
import tkinter as tk

#to define main window
main_window = tk.Tk()


main_window.title('Calci - By TechMaster')
main_window.geometry("300x440")

#variable
entryboxvalue = tk.StringVar()
expression =''

display = tk.Entry(main_window,textvariable=entryboxvalue,font=("Arial",22))
display.place(x=10, y=10, width=280, height=60)



#function

def seven():
    global expression
    expression += '7'
    entryboxvalue.set(expression)
def four():
    global expression
    expression += '4'
    entryboxvalue.set(expression)
def one():
    global expression
    expression += '1'
    entryboxvalue.set(expression)
def eight():
    global expression
    expression += '8'
    entryboxvalue.set(expression)
def five():
    global expression
    expression += '5'
    entryboxvalue.set(expression)
def tow():
    global expression
    expression += '2'
    entryboxvalue.set(expression)
def zero():
    global expression
    expression += '0'
    entryboxvalue.set(expression)
def nine():
    global expression
    expression += '9'
    entryboxvalue.set(expression)
def tow():
    global expression
    expression += '2'
    entryboxvalue.set(expression)
def six():
    global expression
    expression += '6'
    entryboxvalue.set(expression)
def three():
    global expression
    expression += '3'
    entryboxvalue.set(expression)
def four():
    global expression
    expression += '4'
    entryboxvalue.set(expression)

def addfn():
    global expression
    expression += '+'
    entryboxvalue.set(expression)

def eqlfn():
    global expression
    expression = expression + '=' +str(eval(expression))
    entryboxvalue.set(expression)

def back():
    global expression
    expression += 'back'
    entryboxvalue.set(expression)


def multiplyfn():
    global expression
    expression += '*'
    entryboxvalue.set(expression)








button_7 = tk.Button(main_window,text='7',width=4,height=2,font=("Arial",19),fg="black",bg="#faf096",command=seven)
button_7.place(x=10,y=70)
button_4 = tk.Button(main_window,text='4',width=4,height=2,font=("Arial",19),fg="black",bg="#9df3f5",command=four)
button_4.place(x=10,y=145)
button_1 = tk.Button(main_window,text='1',width=4,height=2,font=("Arial",19),fg="black",bg="#faf096",command=one)
button_1.place(x=10,y=215)
button_n = tk.Button(main_window,text='/',width=4,height=2,font=("Arial",19),fg="black",bg="#9df3f5",)
button_n.place(x=10,y=285)
button_8 = tk.Button(main_window,text='8',width=4,height=2,font=("Arial",19),fg="black",bg="#9df3f5",command=eight)
button_8.place(x=80,y=70)
button_5 = tk.Button(main_window,text='5',width=4,height=2,font=("Arial",19),fg="black",bg="#faf096",command=five)
button_5.place(x=80,y=145)
button_2 = tk.Button(main_window,text='2',width=4,height=2,font=("Arial",19),fg="black",bg="#9df3f5",command=tow)
button_2.place(x=80,y=215)
button_0 = tk.Button(main_window,text='0',width=4,height=2,font=("Arial",19),fg="black",bg="#faf096",command=zero)
button_0.place(x=80,y=285)
button_9 = tk.Button(main_window,text='9',width=4,height=2,font=("Arial",19),fg="black",bg="#faf096",command=nine)
button_9.place(x=150,y=70)
button_6 = tk.Button(main_window,text='6',width=4,height=2,font=("Arial",19),fg="black",bg="#9df3f5",command=six)
button_6.place(x=150,y=145)
button_3 = tk.Button(main_window,text='3',width=4,height=2,font=("Arial",19),fg="black",bg="#faf096",command=three)
button_3.place(x=150,y=215)
button_q = tk.Button(main_window,text='.',width=4,height=2,font=("Arial",19),fg="black", bg="#9df3f5")
button_q.place(x=150,y=285)
button_a = tk.Button(main_window,text='+',width=4,height=2,font=("Arial",19),fg="black",bg="#9df3f5",command=addfn)
button_a.place(x=220,y=70)
button_s = tk.Button(main_window,text='-',width=4,height=2,font=("Arial",19),fg="black",bg="#faf096")
button_s.place(x=220,y=145)
button_d = tk.Button(main_window,text='*',width=4,height=2,font=("Arial",19),fg="black",bg="#9df3f5",command=multiplyfn)
button_d.place(x=220,y=215)
button_f = tk.Button(main_window,text='back',width=4,height=2,font=("Arial",19),fg="black",bg="red",command=back)
button_f.place(x=220,y=285)
button_g = tk.Button(main_window,text='=',width=10,height=2,font=("Arial",19),fg="black",bg="#faf096",command=eqlfn)
button_g.place(x=70,y=362)





# button1 = tk.Button(main_window, text=' 1 ', fg='black', bg='red', width=30)




main_window.mainloop()   #for main window