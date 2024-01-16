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
        if AA1 == 0 and AA2 == 0 and BB1 == 0 and BB2 == 0:
            a1.config(bg="lightgray")
            a2.config(bg="lightgray")
            b1.config(bg="lightgray")
            b2.config(bg="lightgray")
        elif AA1 == 0 and AA2 == "X" and BB1 == 0 and BB2 == 0:
            a1.config(bg="lightgray")
        elif AA1 == 0 and AA2 == 0 and BB1 == "X" and BB2 == 0:
            a1.config(bg="lightgray")
        elif AA1 == 0 and AA2 == 0 and BB1 == 0 and BB2 == "X":
            a1.config(bg="lightgray")
        elif AA1 == 0 and AA2 == 0 and BB1 == "X" and BB2 == "X":
            a1.config(bg="lightgray")
        elif AA1 == 0 and AA2 == "X" and BB1 == 0 and BB2 == "X":
            a1.config(bg="lightgray")
        elif AA1 == "X" and AA2 == 0 and BB1 == 0 and BB2 == 0:
            a1.config(bg="red")
#tile two
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
    elif symb == 4:
        if AA4 == 0:
            a4.config(bg="lightgray")
        else:
            a4.config(bg="red", text="X")
            print('Game Over')
    elif symb == 5:
        if AA5 == 0:
            a5.config(bg="lightgray")
        else:
            a5.config(bg="red", text="X")
            print('Game Over')
    elif symb == 6:
        if BB1 == 0:
            b1.config(bg="lightgray")
        else:
            b1.config(bg="red", text="X")
            print('Game Over')
    elif symb == 7:
        if BB2 == 0:
            b2.config(bg="lightgray")
        else:
            b2.config(bg="red", text="X")
            print('Game Over')
    elif symb == 8:
        if BB3 == 0:
            b3.config(bg="lightgray")
        else:
            b3.config(bg="red", text="X")
            print('Game Over')
    elif symb == 9:
        if BB4 == 0:
            b4.config(bg="lightgray")
        else:
            b4.config(bg="red", text="X")
            print('Game Over')
    elif symb == 10:
        if BB5 == 0:
            b5.config(bg="lightgray")
        else:
            b5.config(bg="red", text="X")
            print('Game Over')
    elif symb == 11:
        if CC1 == 0:
            c1.config(bg="lightgray")
        else:
            c1.config(bg="red", text="X")
            print('Game Over')
    elif symb == 12:
        if CC2 == 0:
            c2.config(bg="lightgray")
        else:
            c2.config(bg="red", text="X")
            print('Game Over')
    elif symb == 13:
        if CC3 == 0:
            c3.config(bg="lightgray")
        else:
            c3.config(bg="red", text="X")
            print('Game Over')
    elif symb == 14:
        if CC4 == 0:
            c4.config(bg="lightgray")
        else:
            c4.config(bg="red", text="X")
            print('Game Over')
    elif symb == 15:
        if CC5 == 0:
            c5.config(bg="lightgray")
        else:
            c5.config(bg="red", text="X")
            print('Game Over')
    elif symb == 16:
        if DD1 == 0:
            d1.config(bg="lightgray")
        else:
            d1.config(bg="red", text="X")
    elif symb == 17:
        if DD2 == 0:
            d2.config(bg="lightgray")
        else:
            d2.config(bg="red", text="X")
    elif symb == 18:
        if DD3 == 0:
            d3.config(bg="lightgray")
        else:
            d3.config(bg="red", text="X")
    elif symb == 19:
        if DD4 == 0:
            d4.config(bg="lightgray")
        else:
            d4.config(bg="red", text="X")
    elif symb == 20:
        if DD5 == 0:
            d5.config(bg="lightgray")
        else:
            d5.config(bg="red", text="X")
    elif symb == 21:
        if EE1 == 0:
            e1.config(bg="lightgray")
        else:
            e1.config(bg="red", text="X")
    elif symb == 22:
        if EE2 == 0:
            e2.config(bg="lightgray")
        else:
            e2.config(bg="red", text="X")
    elif symb == 23:
        if EE3 == 0:
            e3.config(bg="lightgray")
        else:
            e3.config(bg="red", text="X")
    elif symb == 24:
        if EE4 == 0:
            e4.config(bg="lightgray")
        else:
            e4.config(bg="red", text="X")
    elif symb == 25:
        if EE5 == 0:
            e5.config(bg="lightgray")
        else:
            e5.config(bg="red", text="X")


def start():
    startbt.config(text="Play Again")
    startbt.place(x=100,y=250)
    global a1,a2,a3,a4,a5,b1,b2,b3,b4,b5,c1,c2,c3,c4,c5,d1,d2,d3,d4,d5,e1,e2,e3,e4,e5
    a1 = tk.Button(root, command=lambda: paint(1))
    a1.place(x=50, y=20, height=40, width=40)
    a2 = tk.Button(root, command=lambda: paint(2))
    a2.place(x=50, y=60, height=40, width=40)
    a3 = tk.Button(root, command=lambda: paint(3))
    a3.place(x=50, y=100, height=40, width=40)
    a4 = tk.Button(root, command=lambda: paint(4))
    a4.place(x=50, y=140, height=40, width=40)
    a5 = tk.Button(root, command=lambda: paint(5))
    a5.place(x=50, y=180, height=40, width=40)
    b1 = tk.Button(root, command=lambda: paint(6))
    b1.place(x=90, y=20, height=40, width=40)
    b2 = tk.Button(root, command=lambda: paint(7))
    b2.place(x=90, y=60, height=40, width=40)
    b3 = tk.Button(root, command=lambda: paint(8))
    b3.place(x=90, y=100, height=40, width=40)
    b4 = tk.Button(root, command=lambda: paint(9))
    b4.place(x=90, y=140, height=40, width=40)
    b5 = tk.Button(root, command=lambda: paint(10))
    b5.place(x=90, y=180, height=40, width=40)
    c1 = tk.Button(root, command=lambda: paint(11))
    c1.place(x=130, y=20, height=40, width=40)
    c2 = tk.Button(root, command=lambda: paint(12))
    c2.place(x=130, y=60, height=40, width=40)
    c3 = tk.Button(root, command=lambda: paint(13))
    c3.place(x=130, y=100, height=40, width=40)
    c4 = tk.Button(root, command=lambda: paint(14))
    c4.place(x=130, y=140, height=40, width=40)
    c5 = tk.Button(root, command=lambda: paint(15))
    c5.place(x=130, y=180, height=40, width=40)
    d1 = tk.Button(root, command=lambda: paint(16))
    d1.place(x=170, y=20, height=40, width=40)
    d2 = tk.Button(root, command=lambda: paint(17))
    d2.place(x=170, y=60, height=40, width=40)
    d3 = tk.Button(root, command=lambda: paint(18))
    d3.place(x=170, y=100, height=40, width=40)
    d4 = tk.Button(root, command=lambda: paint(19))
    d4.place(x=170, y=140, height=40, width=40)
    d5 = tk.Button(root, command=lambda: paint(20))
    d5.place(x=170, y=180, height=40, width=40)
    e1 = tk.Button(root,command=lambda: paint(21))
    e1.place(x=210, y=20, height=40, width=40)
    e2 = tk.Button(root, command=lambda: paint(22))
    e2.place(x=210, y=60, height=40, width=40)
    e3 = tk.Button(root, command=lambda: paint(23))
    e3.place(x=210, y=100, height=40, width=40)
    e4 = tk.Button(root, command=lambda: paint(24))
    e4.place(x=210, y=140, height=40, width=40)
    e5 = tk.Button(root, command=lambda: paint(25))
    e5.place(x=210, y=180, height=40, width=40)
    goodluck = random.randint(1, 6)
    goodluck2 = random.randint(7, 12)
    goodluck3 = random.randint(13, 19)
    goodluck4 = random.randint(20, 25)
    global AA1, AA2,AA3,AA4,AA5,BB1,BB2,BB3,BB4,BB5,CC1,CC2,CC3,CC4,CC5,DD1,DD2,DD3,DD4,DD5,EE1,EE2,EE3,EE4,EE5
    AA1,AA2,AA3,AA4,AA5,BB1,BB2,BB3,BB4,BB5,CC1,CC2,CC3,CC4,CC5,DD1,DD2,DD3,DD4,DD5,EE1,EE2,EE3,EE4,EE5 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    print(goodluck)
    if goodluck == 1:
        a1.config(text="X")
        AA1 = "X"
        print(AA1)
    if goodluck == 2:
        a2.config(text="X")
        AA2 = "X"
        print(AA2)
    if goodluck == 3:
        a3.config(text="X")
        AA3 = "X"
        print(AA2)
    if goodluck == 4:
        a4.config(text="X")
        AA4 = "X"
    if goodluck == 5:
        a5.config(text="X")
        AA5 = "X"
    if goodluck == 6:
        b1.config(text="X")
        BB1 = "X"
    if goodluck2 == 7:
        b2.config(text="X")
        BB2 = "X"
    if goodluck2 == 8:
        b3.config(text="X")
        BB3 = "X"
    if goodluck2 == 9:
        b4.config(text="X")
        BB4 = "X"
    if goodluck2 == 10:
        b5.config(text="X")
        BB5 = "X"
    if goodluck2 == 11:
        c1.config(text="X")
        CC1 = "X"
    if goodluck2 == 12:
        c2.config(text="X")
        CC2 = "X"
    if goodluck3 == 13:
        c3.config(text="X")
        CC3 = "X"
    if goodluck3 == 14:
        c4.config(text="X")
        CC4 = "X"
    if goodluck3 == 15:
        c5.config(text="X")
        CC5 = "X"
    if goodluck3 == 16:
        d1.config(text="X")
        DD1 = "X"
    if goodluck3 == 17:
        d2.config(text="X")
        DD2 = "X"
    if goodluck3 == 18:
        d3.config(text="X")
        DD3 = "X"
    if goodluck3 == 19:
        d4.config(text="X")
        DD4 = "X"
    if goodluck4 == 20:
        d5.config(text="X")
        DD5 = "X"
    if goodluck4 == 21:
        e1.config(text="X")
        EE1 = "X"
    if goodluck4 == 22:
        e2.config(text="X")
        EE2 = "X"
    if goodluck4 == 23:
        e3.config(text="X")
        EE3 = "X"
    if goodluck4 == 24:
        e4.config(text="X")
        EE4 = "X"
    if goodluck4 == 25:
        e5.config(text="X")
        EE5 = "X"
    print(f"goodluck 2 is{goodluck2}")

startbt = tk.Button(root, command=start, text="Start")
startbt.place(x=100, y=100, height=40, width=100)



root.mainloop()