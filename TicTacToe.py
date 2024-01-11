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
            a1.place(x=30, y=50, height=80, width=80)
        else:
            a1 = tk.Button(root, text="O")
            a1.place(x=30, y=50, height=80, width=80)
    elif symb == 2:
        if data == 1:
            a2 = tk.Button(root, text="X")
            a2.place(x=30, y=130, height=80, width=80)
        else:
            a2 = tk.Button(root, text="O")
            a2.place(x=30, y=130, height=80, width=80)
    elif symb == 3:
        if data == 1:
            a3 = tk.Button(root, text="X")
            a3.place(x=30, y=210, height=80, width=80)
        else:
            a3 = tk.Button(root, text="O")
            a3.place(x=30, y=210, height=80, width=80)
    elif symb == 4:
        if data == 1 :
            b1 = tk.Button(root, text="X")
            b1.place(x=110, y=50, height=80, width=80)
        else:
            b1 = tk.Button(root, text="O")
            b1.place(x=110, y=50, height=80, width=80)
    elif symb == 5:
        if data == 1:
            b2 = tk.Button(root, text="X")
            b2.place(x=110, y=130, height=80, width=80)
        else:
            b2 = tk.Button(root, text="O")
            b2.place(x=110, y=130, height=80, width=80)
    elif symb == 6:
        if data == 1:
            b3 = tk.Button(root, text="X")
            b3.place(x=110, y=210, height=80, width=80)
        else:
            b3 = tk.Button(root, text="O")
            b3.place(x=110, y=210, height=80, width=80)
    elif symb == 7:
        if data == 1:
            c1 = tk.Button(root, text="X")
            c1.place(x=190, y=50, height=80, width=80)
        else:
            c1 = tk.Button(root, text="O")
            c1.place(x=190, y=50, height=80, width=80)
    elif symb == 8:
        if data == 1:
            c2 = tk.Button(root, text="X")
            c2.place(x=190, y=130, height=80, width=80)
        else:
            c2 = tk.Button(root, text="O")
            c2.place(x=190, y=130, height=80, width=80)
    elif symb == 9:
        if data == 1:
            c3 = tk.Button(root,  text="X")
            c3.place(x=190, y=210, height=80, width=80)
        else:
            c3 = tk.Button(root, text="O")
            c3.place(x=190, y=210, height=80, width=80)


a1 = tk.Button(root, command=lambda: paint(1), text="")
a1.place(x=30, y=50, height=80, width=80)
a2 = tk.Button(root, command=lambda: paint(2), text="")
a2.place(x=30, y=130, height=80, width=80)
a3 = tk.Button(root, command=lambda: paint(3), text="")
a3.place(x=30, y=210, height=80, width=80)
b1 = tk.Button(root, command=lambda: paint(4), text="")
b1.place(x=110, y=50, height=80, width=80)
b2 = tk.Button(root, command=lambda: paint(5),  text="")
b2.place(x=110, y=130, height=80, width=80)
b3 = tk.Button(root, command=lambda: paint(6), text="")
b3.place(x=110, y=210, height=80, width=80)
c1 = tk.Button(root, command=lambda: paint(7), text="")
c1.place(x=190, y=50, height=80, width=80)
c2 = tk.Button(root, command=lambda: paint(8), text="")
c2.place(x=190, y=130, height=80, width=80)
c3 = tk.Button(root, command=lambda: paint(9), text="")
c3.place(x=190, y=210, height=80, width=80)
root.mainloop()