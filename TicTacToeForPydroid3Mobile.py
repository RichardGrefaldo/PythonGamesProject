import tkinter as tk
root = tk.Tk()
root.geometry('300x400')
root.title('TicTacToe')
counter = 0


def paint(symb):
    global data, counter
    counter = counter + 1
    data = counter % 2
    if symb == 1:
        if data == 1:
            a1 = tk.Button(root, text="X")
            a1.place(x=100, y=300, height=250, width=250)
        else:
            a1 = tk.Button(root, text="O")
            a1.place(x=100, y=300, height=250, width=250)
    elif symb == 2:
        if data == 1:
            a2 = tk.Button(root, text="X")
            a2.place(x=100, y=550, height=250, width=250)
        else:
            a2 = tk.Button(root, text="O")
            a2.place(x=100, y=550, height=250, width=250)
    elif symb == 3:
        if data == 1:
            a3 = tk.Button(root, text="X")
            a3.place(x=100, y=800, height=250, width=250)
        else:
            a3 = tk.Button(root, text="O")
            a3.place(x=100, y=800, height=250, width=250)
    elif symb == 4:
        if data == 1 :
            b1 = tk.Button(root, text="X")
            b1.place(x=350, y=300, height=250, width=250)
        else:
            b1 = tk.Button(root, text="O")
            b1.place(x=350, y=300, height=250, width=250)
    elif symb == 5:
        if data == 1:
            b2 = tk.Button(root, text="X")
            b2.place(x=350, y=550, height=250, width=250)
        else:
            b2 = tk.Button(root, text="O")
            b2.place(x=350, y=550, height=250, width=250)
    elif symb == 6:
        if data == 1:
            b3 = tk.Button(root, text="X")
            b3.place(x=350, y=800, height=250, width=250)
        else:
            b3 = tk.Button(root, text="O")
            b3.place(x=350, y=800, height=250, width=250)
    elif symb == 7:
        if data == 1:
            c1 = tk.Button(root, text="X")
            c1.place(x=600, y=300, height=250, width=250)
        else:
            c1 = tk.Button(root, text="O")
            c1.place(x=600, y=300, height=250, width=250)
    elif symb == 8:
        if data == 1:
            c2 = tk.Button(root, text="X")
            c2.place(x=600, y=550, height=250, width=250)
        else:
            c2 = tk.Button(root, text="O")
            c2.place(x=600, y=550, height=250, width=250)
    elif symb == 9:
        if data == 1:
            c3 = tk.Button(root,  text="X")
            c3.place(x=600, y=800, height=80, width=80)
        else:
            c3 = tk.Button(root, text="O")
            c3.place(x=600, y=800, height=80, width=80)


a1 = tk.Button(root, command=lambda: paint(1), text="")
a1.place(x=100, y=300, height=250, width=250)
a2 = tk.Button(root, command=lambda: paint(2), text="")
a2.place(x=100, y=550, height=250, width=250)
a3 = tk.Button(root, command=lambda: paint(3), text="")
a3.place(x=100, y=800, height=250, width=250)
b1 = tk.Button(root, command=lambda: paint(4), text="")
b1.place(x=350, y=300, height=250, width=250)
b2 = tk.Button(root, command=lambda: paint(5),  text="")
b2.place(x=350, y=550, height=250, width=250)
b3 = tk.Button(root, command=lambda: paint(6), text="")
b3.place(x=350, y=800, height=250, width=250)
c1 = tk.Button(root, command=lambda: paint(7), text="")
c1.place(x=600, y=300, height=250, width=250)
c2 = tk.Button(root, command=lambda: paint(8), text="")
c2.place(x=600, y=550, height=250, width=250)
c3 = tk.Button(root, command=lambda: paint(9), text="")
c3.place(x=600, y=800, height=250, width=250)
root.mainloop()