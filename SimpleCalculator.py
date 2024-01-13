import tkinter as tk
calcu = ""


def add_to_calcu(symbol):
    global calcu
    calcu +=str(symbol)
    textbox.delete(1.0, "end")
    textbox.insert(1.0, calcu)


def eval_to_calcu():
    global calcu
    try:
        calcu = str(eval(calcu))
        textbox.delete(1.0, "end")
        textbox.insert(1.0, calcu)
    except:
        clear()
        textbox.insert(1.0, "Error")


def clear():
    global calcu
    calcu = ""
    textbox.delete(1.0, "end")


root = tk.Tk()
root.geometry('290x440')
root.title('Calculator')
textbox = tk.Text(root, font=('Arial', 30))
textbox.place(x=10, y=10, height=70, width=270)
bn1 = tk.Button(root, command=lambda: add_to_calcu(1), text='1', font=('Arial', 18))
bn1.place(x=10, y=90, height=60, width=60)
bn2 = tk.Button(root, command=lambda: add_to_calcu(2), text='2', font=('Arial', 18))
bn2.place(x=80, y=90, height=60, width=60)
bn3 = tk.Button(root, command=lambda: add_to_calcu(3), text='3', font=('Arial', 18))
bn3.place(x=150, y=90, height=60, width=60)

bn4 = tk.Button(root, command=lambda: add_to_calcu(4), text='4', font=('Arial', 18))
bn4.place(x=10, y=160, height=60, width=60)
bn5 = tk.Button(root, command=lambda: add_to_calcu(5), text='5', font=('Arial', 18))
bn5.place(x=80, y=160, height=60, width=60)
bn6 = tk.Button(root, command=lambda: add_to_calcu(6), text='6', font=('Arial', 18))
bn6.place(x=150, y=160, height=60, width=60)

bn7 = tk.Button(root,  command=lambda: add_to_calcu(7), text='7', font=('Arial', 18))
bn7.place(x=10, y=230, height=60, width=60)
bn8 = tk.Button(root,  command=lambda: add_to_calcu(8), text='8', font=('Arial', 18))
bn8.place(x=80, y=230, height=60, width=60)
bn9 = tk.Button(root,  command=lambda: add_to_calcu(9), text='9', font=('Arial', 18))
bn9.place(x=150, y=230, height=60, width=60)
bn0 = tk.Button(root,  command=lambda: add_to_calcu(0), text='0', font=('Arial', 18))
bn0.place(x=80, y=300, height=60, width=60)
dot = tk.Button(root, command=lambda: add_to_calcu("."), text='.', font=('Arial', 18))
dot.place(x=150, y=300, height=60, width=60)
pbn = tk.Button(root,  command=lambda: add_to_calcu("+"), text='+', font=('Arial', 18))
pbn.place(x=220, y=90, height=60, width=60)
sbn = tk.Button(root,  command=lambda: add_to_calcu("-"), text='-', font=('Arial', 18))
sbn.place(x=220, y=160, height=60, width=60)
mbn = tk.Button(root, command=lambda: add_to_calcu("*"), text='X', font=('Arial', 18))
mbn.place(x=220, y=230, height=60, width=60)
dbn = tk.Button(root,  command=lambda: add_to_calcu("/"), text='÷', font=('Arial', 18))
dbn.place(x=220, y=300, height=60, width=60)
ebn = tk.Button(root, command=eval_to_calcu, text='=', font=('Arial', 18))
ebn.place(x=150, y=370, height=60, width=130)
clr = tk.Button(root, command=clear, text='Clear', font=('Arial', 18))
clr.place(x=10, y=300, height=60, width=60)
pr1 = tk.Button(root, command=lambda: add_to_calcu("("), text='(', font=('Arial', 18))
pr1.place(x=10, y=370, height=60, width=60)
pr2 = tk.Button(root, command=lambda: add_to_calcu(")"), text=')', font=('Arial', 18))
pr2.place(x=80, y=370, height=60, width=60)


root.mainloop()
