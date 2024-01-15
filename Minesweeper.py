import tkinter as tk
import random
from tkinter import Menu
from tkinter import messagebox
root = tk.Tk()
root.geometry('300x400')
root.title("MineSweeper")
about = Menu(root)
root.config(menu=about)
help_menu = Menu(about, tearoff=0)
about.add_cascade(label="Info", menu=help_menu)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About","MineSweeper by Richard\nVersion 20240115"))


def paint(symb):
    if symb == 1:
        if AA1 == 0:
            a1.config(bg="lightgray")
        else:
            a1.config(bg="red",text="X")
            print('Game Over')

    elif symb == 2:
        if AA2 == 0:
            a2.config(bg="lightgray")
        else:
            a2.config(bg="red",text="X")
            print('Game Over')
    elif symb == 3:
        if AA3 == 0:
            a3.config(bg="lightgray")
        else:
            a3.config(bg="red", text="X")
            print('Game Over')


def start():
    startbt.config(text="Play Again")
    startbt.place(x=100,y=250)
    global a1,a2,a3,a4
    a1 = tk.Button(root,command=lambda: paint(1))
    a1.place(x=50, y=20, height=40, width=40)
    a2 = tk.Button(root,command=lambda: paint(2))
    a2.place(x=50, y=60, height=40, width=40)
    a3 = tk.Button(root,command=lambda: paint(3))
    a3.place(x=50, y=100, height=40, width=40)
    a4 = tk.Button(root, )
    a4.place(x=50, y=140, height=40, width=40)
    a5 = tk.Button(root, )
    a5.place(x=50, y=180, height=40, width=40)
    b1 = tk.Button(root, )
    b1.place(x=90, y=20, height=40, width=40)
    b2 = tk.Button(root, )
    b2.place(x=90, y=60, height=40, width=40)
    b3 = tk.Button(root, )
    b3.place(x=90, y=100, height=40, width=40)
    b4 = tk.Button(root, )
    b4.place(x=90, y=140, height=40, width=40)
    b5 = tk.Button(root, )
    b5.place(x=90, y=180, height=40, width=40)
    c1 = tk.Button(root, )
    c1.place(x=130, y=20, height=40, width=40)
    c2 = tk.Button(root, )
    c2.place(x=130, y=60, height=40, width=40)
    c3 = tk.Button(root, )
    c3.place(x=130, y=100, height=40, width=40)
    c4 = tk.Button(root, )
    c4.place(x=130, y=140, height=40, width=40)
    c5 = tk.Button(root, )
    c5.place(x=130, y=180, height=40, width=40)
    d1 = tk.Button(root, )
    d1.place(x=170, y=20, height=40, width=40)
    d2 = tk.Button(root, )
    d2.place(x=170, y=60, height=40, width=40)
    d3 = tk.Button(root, )
    d3.place(x=170, y=100, height=40, width=40)
    d4 = tk.Button(root, )
    d4.place(x=170, y=140, height=40, width=40)
    d5 = tk.Button(root, )
    d5.place(x=170, y=180, height=40, width=40)
    e1 = tk.Button(root, )
    e1.place(x=210, y=20, height=40, width=40)
    e2 = tk.Button(root, )
    e2.place(x=210, y=60, height=40, width=40)
    e3 = tk.Button(root, )
    e3.place(x=210, y=100, height=40, width=40)
    e4 = tk.Button(root, )
    e4.place(x=210, y=140, height=40, width=40)
    e5 = tk.Button(root, )
    e5.place(x=210, y=180, height=40, width=40)
    goodluck = random.randint(1, 4)
    global AA1, AA2,AA3
    AA1,AA2,AA3,AA4,AA5,BB1,BB2,BB3,BB4,BB5,CC1,CC2,CC3,CC4,CC5,DD1,DD2,DD3,DD4,DD5,EE1,EE2,EE3,EE4,EE5 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    print(goodluck)
    if goodluck == 1:
        AA1 = "X"
        print(AA1)
    elif goodluck == 2:
        AA2 = "X"
        print(AA2)
    elif goodluck == 3:
        AA3 = "X"
        print(AA2)
    elif goodluck == 4:
        a4.config(text="X")




startbt = tk.Button(root, command=start, text="Start")
startbt.place(x=100, y=100, height=40, width=100)




root.mainloop()