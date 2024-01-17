import tkinter as tk
import random
from tkinter import Menu
from tkinter import messagebox
import winsound

root = tk.Tk()
root.geometry('300x400')
root.title("MineSweeper")
about = Menu(root)
root.config(menu=about)
help_menu = Menu(about, tearoff=0)
about.add_cascade(label="Info", menu=help_menu)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About","MineSweeper by Richard\nVersion 20240116"))
help_menu.add_command(label="Changelog", command=lambda: messagebox.showinfo("Changelog","Version 20240116\n- Added 'Clear Expansion' tiles will\n now uncover adjacent safe tiles\n -Added Sound Effect\nVersion 20240115\n -Initial Release"))
title = tk.Label(root,text ="MineSweeper",font=('Arial',20))
title.place(x=70, y=20)
title2 = tk.Label(root,text ="by Richard",font=('Arial',12))
title2.place(x=110, y=55)
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
        elif AA1 == "X":
            a1.config(bg="red", text="X")
            winsound.Beep(250, 300)
        else:
            a1.config(bg="lightgray")
#tile two
    elif symb == 2:
        if AA2 == 0 and AA1 == 0 and BB1 == 0 and BB2 == 0 and AA3 == 0 and BB3 == 0:
            a1.config(bg="lightgray")
            a2.config(bg="lightgray")
            a3.config(bg="lightgray")
            b1.config(bg="lightgray")
            b2.config(bg="lightgray")
            b3.config(bg="lightgray")
        elif AA1 == "X" and AA2 == 0 and BB1 == 0 and BB2 == 0 and AA3 == 0 and BB3 == 0:
            a2.config(bg="lightgray")
        elif AA1 == 0 and AA2 == 0 and BB1 == 0 and BB2 == 0 and AA3 == "X" and BB3 == 0:
            a2.config(bg="lightgray")
        elif AA1 == 0 and AA2 == 0 and BB1 == "X" and BB2 == 0 and AA3 == 0 and BB3 == 0:
            a2.config(bg="lightgray")
        elif AA1 == 0 and AA2 == 0 and BB1 == 0 and BB2 == "X" and AA3 == 0 and BB3 == 1:
            a2.config(bg="lightgray")
        elif AA1 == 0 and AA2 == 0 and BB1 == 0 and BB2 == 0 and AA3 == 0 and BB3 == "X":
            a2.config(bg="lightgray")
        elif AA2 == "X":
            a2.config(bg="red", text="X")
            winsound.Beep(250, 300)
        else:
            a2.config(bg="lightgray")

    elif symb == 3:
        if AA3 == 0 and AA2 == 0 and AA4 == 0 and BB2 == 0 and BB3 == 0 and BB4 == 0:
            a2.config(bg="lightgray")
            a3.config(bg="lightgray")
            a4.config(bg="lightgray")
            b2.config(bg="lightgray")
            b3.config(bg="lightgray")
            b4.config(bg="lightgray")
        elif AA3 == 0 and AA2 == "X" and AA4 == 0 and BB2 == 0 and BB3 == 0 and BB4 == 0:
            a3.config(bg="lightgray")
        elif AA3 == 0 and AA2 == 0 and AA4 == "X" and BB2 == 0 and BB3 == 0 and BB4 == 0:
            a3.config(bg="lightgray")
        elif AA3 == 0 and AA2 == 0 and AA4 == 0 and BB2 == "X" and BB3 == 0 and BB4 == 0:
            a3.config(bg="lightgray")
        elif AA3 == 0 and AA2 == 0 and AA4 == 0 and BB2 == 0 and BB3 == "X" and BB4 == 0:
            a3.config(bg="lightgray")
        elif AA3 == 0 and AA2 == 0 and AA4 == 0 and BB2 == 0 and BB3 == 0 and BB4 == "X":
            a3.config(bg="lightgray")
        elif AA3 == "X":
            a3.config(bg="red", text="X")
            winsound.Beep(250, 300)
        else:
            a3.config(bg="lightgray")
    elif symb == 4:
        if AA4 == 0 and AA3 == 0 and AA5 == 0 and BB3 == 0 and BB4 == 0 and BB5 == 0:
            a3.config(bg="lightgray")
            a4.config(bg="lightgray")
            a5.config(bg="lightgray")
            b3.config(bg="lightgray")
            b4.config(bg="lightgray")
            b5.config(bg="lightgray")
        elif AA4 == 0 and AA3 == "X" and AA5 == 0 and BB3 == 0 and BB4 == 0 and BB5 == 0:
            a4.config(bg="lightgray")
        elif AA4 == 0 and AA3 == 0 and AA5 == "X" and BB3 == 0 and BB4 == 0 and BB5 == 0:
            a4.config(bg="lightgray")
        elif AA4 == 0 and AA3 == 0 and AA5 == 0 and BB3 == "X" and BB4 == 0 and BB5 == 0:
            a4.config(bg="lightgray")
        elif AA4 == 0 and AA3 == 0 and AA5 == 0 and BB3 == 0 and BB4 == "X" and BB5 == 0:
            a4.config(bg="lightgray")
        elif AA4 == 0 and AA3 == 0 and AA5 == 0 and BB3 == 0 and BB4 == 0 and BB5 == "X":
            a4.config(bg="lightgray")
        elif AA4 == "X":
            a4.config(bg="red", text="X")
            winsound.Beep(250, 300)
        else:
            a4.config(bg="lightgray")
    elif symb == 5:
        if AA5 == 0 and AA4 == 0 and BB4 == 0 and BB5 == 0:
            a4.config(bg="lightgray")
            a5.config(bg="lightgray")
            b4.config(bg="lightgray")
            b5.config(bg="lightgray")
        elif AA5 == 0 and AA4 == "X" and BB4 == 0 and BB5 == 0:
            a5.config(bg="lightgray")
        elif AA5 == 0 and AA4 == 0 and BB4 == "X" and BB5 == 0:
            a5.config(bg="lightgray")
        elif AA5 == 0 and AA4 == 0 and BB4 == 0 and BB5 == "X":
            a5.config(bg="lightgray")
        elif AA5 == "X":
            a5.config(bg="red", text="X")
            winsound.Beep(250, 300)
        else:
            a5.config(bg="lightgray")
    elif symb == 6:
        if BB1 == 0 and AA1 == 0 and CC1 == 0 and AA2 == 0 and BB2 == 0 and CC2 == 0:
            a1.config(bg="lightgray")
            a2.config(bg="lightgray")
            b1.config(bg="lightgray")
            b2.config(bg="lightgray")
            c1.config(bg="lightgray")
            c2.config(bg="lightgray")
        elif BB1 == 0 and AA1 == "X" and CC1 == 0 and AA2 == 0 and BB2 == 0 and CC2 == 0:
            b1.config(bg="lightgray")
        elif BB1 == 0 and AA1 == 0 and CC1 == "X" and AA2 == 0 and BB2 == 0 and CC2 == 0:
            b1.config(bg="lightgray")
        elif BB1 == 0 and AA1 == 0 and CC1 == 0 and AA2 == "X" and BB2 == 0 and CC2 == 0:
            b1.config(bg="lightgray")
        elif BB1 == 0 and AA1 == 0 and CC1 == 0 and AA2 == 0 and BB2 == "X" and CC2 == 0:
            b1.config(bg="lightgray")
        elif BB1 == 0 and AA1 == 0 and CC1 == 0 and AA2 == 0 and BB2 == 0 and CC2 == "X":
            b1.config(bg="lightgray")
        elif BB1 == "X":
            b1.config(bg="red", text="X")
            winsound.Beep(250, 300)
        else:
            b1.config(bg="lightgray")

    elif symb == 7:
        if BB2 == 0 and BB1 == 0 and AA1 == 0 and AA2 == 0 and AA3 == 0 and BB3 == 0 and CC1 == 0 and CC2 == 0 and CC3 ==0:
            a1.config(bg="lightgray")
            a2.config(bg="lightgray")
            a3.config(bg="lightgray")
            b1.config(bg="lightgray")
            b2.config(bg="lightgray")
            b3.config(bg="lightgray")
            c1.config(bg="lightgray")
            c2.config(bg="lightgray")
            c3.config(bg="lightgray")
        elif BB2 == 0 and BB1 == "X" and AA1 == 0 and AA2 == 0 and AA3 == 0 and BB3 == 0 and CC1 == 0 and CC2 == 0 and CC3 == 0:
            b2.config(bg="lightgray")
        elif BB2 == 0 and BB1 == 0 and AA1 == "X" and AA2 == 0 and AA3 == 0 and BB3 == 0 and CC1 == 0 and CC2 == 0 and CC3 == 0:
            b2.config(bg="lightgray")
        elif BB2 == 0 and BB1 == 0 and AA1 == 0 and AA2 == "X" and AA3 == 0 and BB3 == 0 and CC1 == 0 and CC2 == 0 and CC3 == 0:
            b2.config(bg="lightgray")
        elif BB2 == 0 and BB1 == 0 and AA1 == 0 and AA2 == 0 and AA3 == "X" and BB3 == 0 and CC1 == 0 and CC2 == 0 and CC3 == 0:
            b2.config(bg="lightgray")
        elif BB2 == 0 and BB1 == 0 and AA1 == 0 and AA2 == 0 and AA3 == 0 and BB3 == "X" and CC1 == 0 and CC2 == 0 and CC3 == 0:
            b2.config(bg="lightgray")
        elif BB2 == 0 and BB1 == 0 and AA1 == 0 and AA2 == 0 and AA3 == 0 and BB3 == 0 and CC1 == "X" and CC2 == 0 and CC3 == 0:
            b2.config(bg="lightgray")
        elif BB2 == 0 and BB1 == 0 and AA1 == 0 and AA2 == 0 and AA3 == 0 and BB3 == 0 and CC1 == 0 and CC2 == "X" and CC3 == 0:
            b2.config(bg="lightgray")
        elif BB2 == 0 and BB1 == 0 and AA1 == 0 and AA2 == 0 and AA3 == 0 and BB3 == 0 and CC1 == 0 and CC2 == 0 and CC3 == "X":
            b2.config(bg="lightgray")
        elif BB2 == "X":
            b2.config(bg="red", text="X")
            winsound.Beep(250, 300)
        else:
            b2.config(bg="lightgray")

    elif symb == 8:
        if BB3 == 0 and BB2 == 0 and BB4 == 0 and AA2 == 0 and AA3 == 0 and AA4 == 0 and CC2 == 0 and CC3 == 0 and CC4 == 0:
            b2.config(bg="lightgray")
            b3.config(bg="lightgray")
            b4.config(bg="lightgray")
            a2.config(bg="lightgray")
            a3.config(bg="lightgray")
            a4.config(bg="lightgray")
            c2.config(bg="lightgray")
            c3.config(bg="lightgray")
            c4.config(bg="lightgray")
        elif BB3 == 0 and BB2 == "X" and BB4 == 0 and AA2 == 0 and AA3 == 0 and AA4 == 0 and CC2 == 0 and CC3 == 0 and CC4 == 0:
            b3.config(bg="lightgray")
        elif BB3 == 0 and BB2 == 0 and BB4 == "X" and AA2 == 0 and AA3 == 0 and AA4 == 0 and CC2 == 0 and CC3 == 0 and CC4 == 0:
            b3.config(bg="lightgray")
        elif BB3 == 0 and BB2 == 0 and BB4 == 0 and AA2 == "X" and AA3 == 0 and AA4 == 0 and CC2 == 0 and CC3 == 0 and CC4 == 0:
            b3.config(bg="lightgray")
        elif BB3 == 0 and BB2 == 0 and BB4 == 0 and AA2 == 0 and AA3 == "X" and AA4 == 0 and CC2 == 0 and CC3 == 0 and CC4 == 0:
            b3.config(bg="lightgray")
        elif BB3 == 0 and BB2 == 0 and BB4 == 0 and AA2 == 0 and AA3 == 0 and AA4 == "X" and CC2 == 0 and CC3 == 0 and CC4 == 0:
            b3.config(bg="lightgray")
        elif BB3 == 0 and BB2 == 0 and BB4 == 0 and AA2 == 0 and AA3 == 0 and AA4 == 0 and CC2 == "X" and CC3 == 0 and CC4 == 0:
            b3.config(bg="lightgray")
        elif BB3 == 0 and BB2 == 0 and BB4 == 0 and AA2 == 0 and AA3 == 0 and AA4 == 0 and CC2 == 0 and CC3 == "X" and CC4 == 0:
            b3.config(bg="lightgray")
        elif BB3 == 0 and BB2 == 0 and BB4 == 0 and AA2 == 0 and AA3 == 0 and AA4 == 0 and CC2 == 0 and CC3 == 0 and CC4 == "X":
            b3.config(bg="lightgray")
        elif BB3 == "X":
            b3.config(bg="red", text="X")
            winsound.Beep(250, 300)
        else:
            b3.config(bg="lightgray")
    elif symb == 9:
        if BB4 == 0 and BB3 == 0 and BB5 == 0 and AA3 == 0 and AA4 == 0 and AA5 == 0 and CC3 == 0 and CC4 == 0 and CC5 == 0:
            b3.config(bg="lightgray")
            b4.config(bg="lightgray")
            b5.config(bg="lightgray")
            a3.config(bg="lightgray")
            a4.config(bg="lightgray")
            a5.config(bg="lightgray")
            c3.config(bg="lightgray")
            c4.config(bg="lightgray")
            c5.config(bg="lightgray")
        elif BB4 == 0 and BB3 == "X" and BB5 == 0 and AA3 == 0 and AA4 == 0 and AA5 == 0 and CC3 == 0 and CC4 == 0 and CC5 == 0:
            b4.config(bg="lightgray")
        elif BB4 == 0 and BB3 == 0 and BB5 == "X" and AA3 == 0 and AA4 == 0 and AA5 == 0 and CC3 == 0 and CC4 == 0 and CC5 == 0:
            b4.config(bg="lightgray")
        elif BB4 == 0 and BB3 == 0 and BB5 == 0 and AA3 == "X" and AA4 == 0 and AA5 == 0 and CC3 == 0 and CC4 == 0 and CC5 == 0:
            b4.config(bg="lightgray")
        elif BB4 == 0 and BB3 == 0 and BB5 == 0 and AA3 == 0 and AA4 == "X" and AA5 == 0 and CC3 == 0 and CC4 == 0 and CC5 == 0:
            b4.config(bg="lightgray")
        elif BB4 == 0 and BB3 == 0 and BB5 == 0 and AA3 == 0 and AA4 == 0 and AA5 == "X" and CC3 == 0 and CC4 == 0 and CC5 == 0:
            b4.config(bg="lightgray")
        elif BB4 == 0 and BB3 == 0 and BB5 == 0 and AA3 == 0 and AA4 == 0 and AA5 == 0 and CC3 == "X" and CC4 == 0 and CC5 == 0:
            b4.config(bg="lightgray")
        elif BB4 == 0 and BB3 == 0 and BB5 == 0 and AA3 == 0 and AA4 == 0 and AA5 == 0 and CC3 == 0 and CC4 == "X" and CC5 == 0:
            b4.config(bg="lightgray")
        elif BB4 == 0 and BB3 == 0 and BB5 == 0 and AA3 == 0 and AA4 == 0 and AA5 == 0 and CC3 == 0 and CC4 == 0 and CC5 == "X":
            b4.config(bg="lightgray")
        elif BB4 == "X":
            b4.config(bg="red", text="X")
            winsound.Beep(250, 300)
        else:
            b4.config(bg="lightgray")
    elif symb == 10:
        if BB5 == 0 and BB4 == 0 and AA4 == 0 and AA5 == 0 and CC4 == 0 and CC5 == 0:
            b4.config(bg="lightgray")
            b5.config(bg="lightgray")
            a4.config(bg="lightgray")
            a5.config(bg="lightgray")
            c4.config(bg="lightgray")
            c5.config(bg="lightgray")
        elif BB5 == 0 and BB4 == "X" and AA4 == 0 and AA5 == 0 and CC4 == 0 and CC5 == 0:
            b5.config(bg="lightgray")
        elif BB5 == 0 and BB4 == 0 and AA4 == "X" and AA5 == 0 and CC4 == 0 and CC5 == 0:
            b5.config(bg="lightgray")
        elif BB5 == 0 and BB4 == 0 and AA4 == 0 and AA5 == "X" and CC4 == 0 and CC5 == 0:
            b5.config(bg="lightgray")
        elif BB5 == 0 and BB4 == 0 and AA4 == 0 and AA5 == 0 and CC4 == "X" and CC5 == 0:
            b5.config(bg="lightgray")
        elif BB5 == 0 and BB4 == 0 and AA4 == 0 and AA5 == 0 and CC4 == 0 and CC5 == "X":
            b5.config(bg="lightgray")
        elif BB5 == "X":
            b5.config(bg="red", text="X")
            winsound.Beep(250, 300)
        else:
            b5.config(bg="lightgray")
    elif symb == 11:
        if CC1 == 0 and BB1 == 0 and BB2 == 0 and CC2 == 0 and DD1 == 0 and DD2 == 0:
            b1.config(bg="lightgray")
            b2.config(bg="lightgray")
            c1.config(bg="lightgray")
            c2.config(bg="lightgray")
            d1.config(bg="lightgray")
            d2.config(bg="lightgray")
        elif CC1 == 0 and BB1 == "X" and BB2 == 0 and CC2 == 0 and DD1 == 0 and DD2 == 0:
            c1.config(bg="lightgray")
        elif CC1 == 0 and BB1 == 0 and BB2 == "X" and CC2 == 0 and DD1 == 0 and DD2 == 0:
            c1.config(bg="lightgray")
        elif CC1 == 0 and BB1 == 0 and BB2 == 0 and CC2 == "X" and DD1 == 0 and DD2 == 0:
            c1.config(bg="lightgray")
        elif CC1 == 0 and BB1 == 0 and BB2 == 0 and CC2 == 0 and DD1 == "X" and DD2 == 0:
            c1.config(bg="lightgray")
        elif CC1 == 0 and BB1 == 0 and BB2 == 0 and CC2 == 0 and DD1 == 0 and DD2 == "X":
            c1.config(bg="lightgray")
        elif CC1 == "X":
            c1.config(bg="red", text="X")
            winsound.Beep(250, 300)
        else:
            c1.config(bg="lightgray")
    elif symb == 12:
        if CC2 == 0 and CC1 == 0 and CC3 == 0 and BB1 == 0 and BB2 == 0 and BB3 == 0 and DD1 == 0 and DD2 == 0 and DD3 == 0:
            c1.config(bg="lightgray")
            c2.config(bg="lightgray")
            c3.config(bg="lightgray")
            b1.config(bg="lightgray")
            b2.config(bg="lightgray")
            b3.config(bg="lightgray")
            d1.config(bg="lightgray")
            d2.config(bg="lightgray")
            d3.config(bg="lightgray")
        elif CC2 == 0 and CC1 == "X" and CC3 == 0 and BB1 == 0 and BB2 == 0 and BB3 == 0 and DD1 == 0 and DD2 == 0 and DD3 == 0:
            c2.config(bg="lightgray")
        elif CC2 == 0 and CC1 == 0 and CC3 == "X" and BB1 == 0 and BB2 == 0 and BB3 == 0 and DD1 == 0 and DD2 == 0 and DD3 == 0:
            c2.config(bg="lightgray")
        elif CC2 == 0 and CC1 == 0 and CC3 == 0 and BB1 == "X" and BB2 == 0 and BB3 == 0 and DD1 == 0 and DD2 == 0 and DD3 == 0:
            c2.config(bg="lightgray")
        elif CC2 == 0 and CC1 == 0 and CC3 == 0 and BB1 == 0 and BB2 == "X" and BB3 == 0 and DD1 == 0 and DD2 == 0 and DD3 == 0:
            c2.config(bg="lightgray")
        elif CC2 == 0 and CC1 == 0 and CC3 == 0 and BB1 == 0 and BB2 == 0 and BB3 == "X" and DD1 == 0 and DD2 == 0 and DD3 == 0:
            c2.config(bg="lightgray")
        elif CC2 == 0 and CC1 == 0 and CC3 == 0 and BB1 == 0 and BB2 == 0 and BB3 == 0 and DD1 == "X" and DD2 == 0 and DD3 == 0:
            c2.config(bg="lightgray")
        elif CC2 == 0 and CC1 == "X" and CC3 == 0 and BB1 == 0 and BB2 == 0 and BB3 == 0 and DD1 == 0 and DD2 == "X" and DD3 == 0:
            c2.config(bg="lightgray")
        elif CC2 == 0 and CC1 == "X" and CC3 == 0 and BB1 == 0 and BB2 == 0 and BB3 == 0 and DD1 == 0 and DD2 == 0 and DD3 == "X":
            c2.config(bg="lightgray")
        elif CC2 == "X":
            c2.config(bg="red", text="X")
            winsound.Beep(250, 300)
        else:
            c2.config(bg="lightgray")
    elif symb == 13:
        if CC3 == 0 and CC2 == 0 and CC4 == 0 and BB2 == 0 and BB3 == 0 and BB4 == 0 and DD2 == 0 and DD3 == 0 and DD4 ==0:
            b2.config(bg="lightgray")
            b3.config(bg="lightgray")
            b4.config(bg="lightgray")
            c2.config(bg="lightgray")
            c3.config(bg="lightgray")
            c4.config(bg="lightgray")
            d2.config(bg="lightgray")
            d3.config(bg="lightgray")
            d4.config(bg="lightgray")
        elif CC3 == 0 and CC2 == "X" and CC4 == 0 and BB2 == 0 and BB3 == 0 and BB4 == 0 and DD2 == 0 and DD3 == 0 and DD4 ==0:
            c3.config(bg="lightgray")
        elif CC3 == 0 and CC2 == 0 and CC4 == "X" and BB2 == 0 and BB3 == 0 and BB4 == 0 and DD2 == 0 and DD3 == 0 and DD4 ==0:
            c3.config(bg="lightgray")
        elif CC3 == 0 and CC2 == 0 and CC4 == 0 and BB2 == "X" and BB3 == 0 and BB4 == 0 and DD2 == 0 and DD3 == 0 and DD4 ==0:
            c3.config(bg="lightgray")
        elif CC3 == 0 and CC2 == 0 and CC4 == 0 and BB2 == 0 and BB3 == "X" and BB4 == 0 and DD2 == 0 and DD3 == 0 and DD4 ==0:
            c3.config(bg="lightgray")
        elif CC3 == 0 and CC2 == 0 and CC4 == 0 and BB2 == 0 and BB3 == 0 and BB4 == "X" and DD2 == 0 and DD3 == 0 and DD4 ==0:
            c3.config(bg="lightgray")
        elif CC3 == 0 and CC2 == 0 and CC4 == 0 and BB2 == 0 and BB3 == 0 and BB4 == 0 and DD2 == "X" and DD3 == 0 and DD4 ==0:
            c3.config(bg="lightgray")
        elif CC3 == 0 and CC2 == 0 and CC4 == 0 and BB2 == 0 and BB3 == 0 and BB4 == 0 and DD2 == 0 and DD3 == "X" and DD4 ==0:
            c3.config(bg="lightgray")
        elif CC3 == 0 and CC2 == 0 and CC4 == 0 and BB2 == 0 and BB3 == 0 and BB4 == 0 and DD2 == 0 and DD3 == 0 and DD4 =="X":
            c3.config(bg="lightgray")
        elif CC3 == "X":
            c3.config(bg="red", text="X")
            winsound.Beep(250, 300)
        else:
            c3.config(bg="lightgray")
    elif symb == 14:
        if CC4 == 0 and CC3 == 0 and CC5 == 0 and BB3 == 0 and BB4 == 0 and BB5 == 0 and DD3 == 0 and DD4 == 0 and DD5 == 0:
            b3.config(bg="lightgray")
            b4.config(bg="lightgray")
            b5.config(bg="lightgray")
            c3.config(bg="lightgray")
            c4.config(bg="lightgray")
            c5.config(bg="lightgray")
            d3.config(bg="lightgray")
            d4.config(bg="lightgray")
            d5.config(bg="lightgray")
        elif CC4 == 0 and CC3 == "X" and CC5 == 0 and BB3 == 0 and BB4 == 0 and BB5 == 0 and DD3 == 0 and DD4 == 0 and DD5 == 0:
            c4.config(bg="lightgray")
        elif CC4 == 0 and CC3 == 0 and CC5 == "X" and BB3 == 0 and BB4 == 0 and BB5 == 0 and DD3 == 0 and DD4 == 0 and DD5 == 0:
            c4.config(bg="lightgray")
        elif CC4 == 0 and CC3 == 0 and CC5 == 0 and BB3 == "X" and BB4 == 0 and BB5 == 0 and DD3 == 0 and DD4 == 0 and DD5 == 0:
            c4.config(bg="lightgray")
        elif CC4 == 0 and CC3 == 0 and CC5 == 0 and BB3 == 0 and BB4 == "X" and BB5 == 0 and DD3 == 0 and DD4 == 0 and DD5 == 0:
            c4.config(bg="lightgray")
        elif CC4 == 0 and CC3 == 0 and CC5 == 0 and BB3 == 0 and BB4 == 0 and BB5 == "X" and DD3 == 0 and DD4 == 0 and DD5 == 0:
            c4.config(bg="lightgray")
        elif CC4 == 0 and CC3 == 0 and CC5 == 0 and BB3 == 0 and BB4 == 0 and BB5 == 0 and DD3 == "X" and DD4 == 0 and DD5 == 0:
            c4.config(bg="lightgray")
        elif CC4 == 0 and CC3 == 0 and CC5 == 0 and BB3 == 0 and BB4 == 0 and BB5 == 0 and DD3 == 0 and DD4 == "X" and DD5 == 0:
            c4.config(bg="lightgray")
        elif CC4 == 0 and CC3 == 0 and CC5 == 0 and BB3 == 0 and BB4 == 0 and BB5 == 0 and DD3 == 0 and DD4 == 0 and DD5 == "X":
            c4.config(bg="lightgray")
        elif CC4 == "X":
            c4.config(bg="red", text="X")
            winsound.Beep(250, 300)
        else:
            c4.config(bg="lightgray")
    elif symb == 15:
        if CC5 == 0 and CC4 == 0 and BB4 == 0 and BB5 == 0 and DD4 == 0 and DD5 == 0:
            b4.config(bg="lightgray")
            b5.config(bg="lightgray")
            c4.config(bg="lightgray")
            c5.config(bg="lightgray")
            d4.config(bg="lightgray")
            d5.config(bg="lightgray")
        elif CC5 == 0 and CC4 == "X" and BB4 == 0 and BB5 == 0 and DD4 == 0 and DD5 == 0:
            c5.config(bg="lightgray")
        elif CC5 == 0 and CC4 == 0 and BB4 == "X" and BB5 == 0 and DD4 == 0 and DD5 == 0:
            c5.config(bg="lightgray")
        elif CC5 == 0 and CC4 == 0 and BB4 == 0 and BB5 == "X" and DD4 == 0 and DD5 == 0:
            c5.config(bg="lightgray")
        elif CC5 == 0 and CC4 == 0 and BB4 == 0 and BB5 == 0 and DD4 == "X" and DD5 == 0:
            c5.config(bg="lightgray")
        elif CC5 == 0 and CC4 == 0 and BB4 == 0 and BB5 == 0 and DD4 == 0 and DD5 == "X":
            c5.config(bg="lightgray")
        elif CC5 == "X":
            c5.config(bg="red", text="X")
            winsound.Beep(250, 300)
        else:
            c5.config(bg="lightgray")
    elif symb == 16:
        if DD1 == 0 and DD2 == 0 and CC1 == 0 and CC2 == 0 and EE1 == 0 and EE2 == 0:
            c1.config(bg="lightgray")
            c2.config(bg="lightgray")
            d1.config(bg="lightgray")
            d2.config(bg="lightgray")
            e1.config(bg="lightgray")
            e2.config(bg="lightgray")
        elif DD1 == 0 and DD2 == "X" and CC1 == 0 and CC2 == 0 and EE1 == 0 and EE2 == 0:
            d1.config(bg="lightgray")
        elif DD1 == 0 and DD2 == 0 and CC1 == "X" and CC2 == 0 and EE1 == 0 and EE2 == 0:
            d1.config(bg="lightgray")
        elif DD1 == 0 and DD2 == 0 and CC1 == 0 and CC2 == "X" and EE1 == 0 and EE2 == 0:
            d1.config(bg="lightgray")
        elif DD1 == 0 and DD2 == 0 and CC1 == 0 and CC2 == 0 and EE1 == "X" and EE2 == 0:
            d1.config(bg="lightgray")
        elif DD1 == 0 and DD2 == 0 and CC1 == 0 and CC2 == 0 and EE1 == 0 and EE2 == "X":
            d1.config(bg="lightgray")
        elif DD1 == "X":
            d1.config(bg="red", text="X")
            winsound.Beep(250, 300)
        else:
            d1.config(bg="lightgray")

    elif symb == 17:
        if DD2 == 0 and DD3 == 0 and DD1 == 0 and CC1 == 0 and CC2 == 0 and CC3 == 0 and EE1 == 0 and EE2 == 0 and EE3 == 0:
            c1.config(bg="lightgray")
            c2.config(bg="lightgray")
            c3.config(bg="lightgray")
            d1.config(bg="lightgray")
            d2.config(bg="lightgray")
            d3.config(bg="lightgray")
            e1.config(bg="lightgray")
            e2.config(bg="lightgray")
            e3.config(bg="lightgray")
        elif DD2 == 0 and DD3 == "X" and DD1 == 0 and CC1 == 0 and CC2 == 0 and CC3 == 0 and EE1 == 0 and EE2 == 0 and EE3 == 0:
            d2.config(bg="lightgray")
        elif DD2 == 0 and DD3 == 0 and DD1 == "X" and CC1 == 0 and CC2 == 0 and CC3 == 0 and EE1 == 0 and EE2 == 0 and EE3 == 0:
            d2.config(bg="lightgray")
        elif DD2 == 0 and DD3 == 0 and DD1 == 0 and CC1 == "X" and CC2 == 0 and CC3 == 0 and EE1 == 0 and EE2 == 0 and EE3 == 0:
            d2.config(bg="lightgray")
        elif DD2 == 0 and DD3 == 0 and DD1 == 0 and CC1 == 0 and CC2 == "X" and CC3 == 0 and EE1 == 0 and EE2 == 0 and EE3 == 0:
            d2.config(bg="lightgray")
        elif DD2 == 0 and DD3 == 0 and DD1 == 0 and CC1 == 0 and CC2 == 0 and CC3 == "X" and EE1 == 0 and EE2 == 0 and EE3 == 0:
            d2.config(bg="lightgray")
        elif DD2 == 0 and DD3 == 0 and DD1 == 0 and CC1 == 0 and CC2 == 0 and CC3 == 0 and EE1 == "X" and EE2 == 0 and EE3 == 0:
            d2.config(bg="lightgray")
        elif DD2 == 0 and DD3 == 0 and DD1 == 0 and CC1 == 0 and CC2 == 0 and CC3 == 0 and EE1 == 0 and EE2 == "X" and EE3 == 0:
            d2.config(bg="lightgray")
        elif DD2 == 0 and DD3 == 0 and DD1 == 0 and CC1 == 0 and CC2 == 0 and CC3 == 0 and EE1 == 0 and EE2 == 0 and EE3 == "X":
            d2.config(bg="lightgray")
        elif DD2 == "X":
            d2.config(bg="red", text="X")
            winsound.Beep(250, 300)
        else:
            d2.config(bg="lightgray")
    elif symb == 18:
        if DD3 == 0 and DD2 == 0 and DD4 == 0 and CC2 == 0 and CC3 == 0 and CC4 == 0 and EE2 == 0 and EE3 == 0 and EE4 == 0:
            c2.config(bg="lightgray")
            c3.config(bg="lightgray")
            c4.config(bg="lightgray")
            d2.config(bg="lightgray")
            d3.config(bg="lightgray")
            d4.config(bg="lightgray")
            e2.config(bg="lightgray")
            e3.config(bg="lightgray")
            e4.config(bg="lightgray")
        elif DD3 == 0 and DD2 == "X" and DD4 == 0 and CC2 == 0 and CC3 == 0 and CC4 == 0 and EE2 == 0 and EE3 == 0 and EE4 == 0:
            d3.config(bg="lightgray")
        elif DD3 == 0 and DD2 == 0 and DD4 == "X" and CC2 == 0 and CC3 == 0 and CC4 == 0 and EE2 == 0 and EE3 == 0 and EE4 == 0:
            d3.config(bg="lightgray")
        elif DD3 == 0 and DD2 == 0 and DD4 == 0 and CC2 == "X" and CC3 == 0 and CC4 == 0 and EE2 == 0 and EE3 == 0 and EE4 == 0:
            d3.config(bg="lightgray")
        elif DD3 == 0 and DD2 == 0 and DD4 == 0 and CC2 == 0 and CC3 == "X" and CC4 == 0 and EE2 == 0 and EE3 == 0 and EE4 == 0:
            d3.config(bg="lightgray")
        elif DD3 == 0 and DD2 == 0 and DD4 == 0 and CC2 == 0 and CC3 == 0 and CC4 == "X" and EE2 == 0 and EE3 == 0 and EE4 == 0:
            d3.config(bg="lightgray")
        elif DD3 == 0 and DD2 == 0 and DD4 == 0 and CC2 == 0 and CC3 == 0 and CC4 == 0 and EE2 == "X" and EE3 == 0 and EE4 == 0:
            d3.config(bg="lightgray")
        elif DD3 == 0 and DD2 == 0 and DD4 == 0 and CC2 == 0 and CC3 == 0 and CC4 == 0 and EE2 == 0 and EE3 == "X" and EE4 == 0:
            d3.config(bg="lightgray")
        elif DD3 == 0 and DD2 == 0 and DD4 == 0 and CC2 == 0 and CC3 == 0 and CC4 == 0 and EE2 == 0 and EE3 == 0 and EE4 == "X":
            d3.config(bg="lightgray")
        elif DD3 == "X":
            d3.config(bg="red", text="X")
            winsound.Beep(250, 300)
        else:
            d3.config(bg="lightgray")

    elif symb == 19:
        if DD4 == 0 and DD3 == 0 and DD5 == 0 and CC3 == 0 and CC4 == 0 and CC5 == 0 and EE3 == 0 and EE4 == 0 and EE5 == 0:
            c3.config(bg="lightgray")
            c4.config(bg="lightgray")
            c5.config(bg="lightgray")
            d3.config(bg="lightgray")
            d4.config(bg="lightgray")
            d5.config(bg="lightgray")
            e3.config(bg="lightgray")
            e4.config(bg="lightgray")
            e5.config(bg="lightgray")
        elif DD4 == 0 and DD3 == "X" and DD5 == 0 and CC3 == 0 and CC4 == 0 and CC5 == 0 and EE3 == 0 and EE4 == 0 and EE5 == 0:
            d4.config(bg="lightgray")
        elif DD4 == 0 and DD3 == 0 and DD5 == "X" and CC3 == 0 and CC4 == 0 and CC5 == 0 and EE3 == 0 and EE4 == 0 and EE5 == 0:
            d4.config(bg="lightgray")
        elif DD4 == 0 and DD3 == 0 and DD5 == 0 and CC3 == "X" and CC4 == 0 and CC5 == 0 and EE3 == 0 and EE4 == 0 and EE5 == 0:
            d4.config(bg="lightgray")
        elif DD4 == 0 and DD3 == 0 and DD5 == 0 and CC3 == 0 and CC4 == "X" and CC5 == 0 and EE3 == 0 and EE4 == 0 and EE5 == 0:
            d4.config(bg="lightgray")
        elif DD4 == 0 and DD3 == 0 and DD5 == 0 and CC3 == 0 and CC4 == 0 and CC5 == "X" and EE3 == 0 and EE4 == 0 and EE5 == 0:
            d4.config(bg="lightgray")
        elif DD4 == 0 and DD3 == 0 and DD5 == 0 and CC3 == 0 and CC4 == 0 and CC5 == 0 and EE3 == "X" and EE4 == 0 and EE5 == 0:
            d4.config(bg="lightgray")
        elif DD4 == 0 and DD3 == 0 and DD5 == 0 and CC3 == 0 and CC4 == 0 and CC5 == 0 and EE3 == 0 and EE4 == "X" and EE5 == 0:
            d4.config(bg="lightgray")
        elif DD4 == 0 and DD3 == 0 and DD5 == 0 and CC3 == 0 and CC4 == 0 and CC5 == 0 and EE3 == 0 and EE4 == 0 and EE5 == "X":
            d4.config(bg="lightgray")
        elif DD4 == "X":
            d4.config(bg="red", text="X")
            winsound.Beep(250, 300)
        else:
            d4.config(bg="lightgray")

    elif symb == 20:
        if DD5 == 0 and DD4 == 0 and CC4 == 0 and CC5 == 0 and EE4 == 0 and EE5 == 0:
            c4.config(bg="lightgray")
            c5.config(bg="lightgray")
            d4.config(bg="lightgray")
            d5.config(bg="lightgray")
            e4.config(bg="lightgray")
            e5.config(bg="lightgray")
        elif DD5 == 0 and DD4 == "X" and CC4 == 0 and CC5 == 0 and EE4 == 0 and EE5 == 0:
            d5.config(bg="lightgray")
        elif DD5 == 0 and DD4 == 0 and CC4 == "X" and CC5 == 0 and EE4 == 0 and EE5 == 0:
            d5.config(bg="lightgray")
        elif DD5 == 0 and DD4 == 0 and CC4 == 0 and CC5 == "X" and EE4 == 0 and EE5 == 0:
            d5.config(bg="lightgray")
        elif DD5 == 0 and DD4 == 0 and CC4 == 0 and CC5 == 0 and EE4 == "X" and EE5 == 0:
            d5.config(bg="lightgray")
        elif DD5 == 0 and DD4 == 0 and CC4 == 0 and CC5 == 0 and EE4 == 0 and EE5 == "X":
            d5.config(bg="lightgray")
        elif DD5 == "X":
            d5.config(bg="red", text="X")
            winsound.Beep(250, 300)
        else:
            d5.config(bg="lightgray")
    elif symb == 21:
        if EE1 == 0 and EE2 == 0 and DD1 == 0 and DD2 == 0:
            d1.config(bg="lightgray")
            d2.config(bg="lightgray")
            e1.config(bg="lightgray")
            e2.config(bg="lightgray")
        elif EE1 == 0 and EE2 == "X" and DD1 == 0 and DD2 == 0:
            e1.config(bg="lightgray")
        elif EE1 == 0 and EE2 == 0 and DD1 == "X" and DD2 == 0:
            e1.config(bg="lightgray")
        elif EE1 == 0 and EE2 == 0 and DD1 == 0 and DD2 == "X":
            e1.config(bg="lightgray")
        elif EE1 == "X":
            e1.config(bg="red", text="X")
            winsound.Beep(250, 300)
        else:
            e1.config(bg="lightgray")
    elif symb == 22:
        if EE2 == 0 and EE1 == 0 and EE3 == 0 and DD1 == 0 and DD2 == 0 and DD3 == 0:
            e1.config(bg="lightgray")
            e2.config(bg="lightgray")
            e3.config(bg="lightgray")
            d1.config(bg="lightgray")
            d2.config(bg="lightgray")
            d3.config(bg="lightgray")
        elif EE2 == 0 and EE1 == "X" and EE3 == 0 and DD1 == 0 and DD2 == 0 and DD3 == 0:
            e2.config(bg="lightgray")
        elif EE2 == 0 and EE1 == 0 and EE3 == "X" and DD1 == 0 and DD2 == 0 and DD3 == 0:
            e2.config(bg="lightgray")
        elif EE2 == 0 and EE1 == 0 and EE3 == 0 and DD1 == "X" and DD2 == 0 and DD3 == 0:
            e2.config(bg="lightgray")
        elif EE2 == 0 and EE1 == 0 and EE3 == 0 and DD1 == 0 and DD2 == "X" and DD3 == 0:
            e2.config(bg="lightgray")
        elif EE2 == 0 and EE1 == 0 and EE3 == 0 and DD1 == 0 and DD2 == 0 and DD3 == "X":
            e2.config(bg="lightgray")
        elif EE2 == "X":
            e2.config(bg="red", text="X")
            winsound.Beep(250, 300)
        else:
            e2.config(bg="lightgray")

    elif symb == 23:
        if EE3 == 0 and EE2 == 0 and EE4 == 0 and DD2 == 0 and DD3 == 0 and DD4 == 0:
            e2.config(bg="lightgray")
            e3.config(bg="lightgray")
            e4.config(bg="lightgray")
            d2.config(bg="lightgray")
            d3.config(bg="lightgray")
            d4.config(bg="lightgray")
        elif EE3 == 0 and EE2 == "X" and EE4 == 0 and DD2 == 0 and DD3 == 0 and DD4 == 0:
            e3.config(bg="lightgray")
        elif EE3 == 0 and EE2 == 0 and EE4 == "X" and DD2 == 0 and DD3 == 0 and DD4 == 0:
            e3.config(bg="lightgray")
        elif EE3 == 0 and EE2 == 0 and EE4 == 0 and DD2 == "X" and DD3 == 0 and DD4 == 0:
            e3.config(bg="lightgray")
        elif EE3 == 0 and EE2 == 0 and EE4 == 0 and DD2 == 0 and DD3 == "X" and DD4 == 0:
            e3.config(bg="lightgray")
        elif EE3 == 0 and EE2 == 0 and EE4 == 0 and DD2 == 0 and DD3 == 0 and DD4 == "X":
            e3.config(bg="lightgray")
        elif EE3 == "X":
            e3.config(bg="red", text="X")
            winsound.Beep(250, 300)
        else:
            e3.config(bg="lightgray")
    elif symb == 24:
        if EE4 == 0 and EE3 == 0 and EE5 == 0 and DD3 == 0 and DD4 ==0 and DD5 == 0:
            d3.config(bg="lightgray")
            d4.config(bg="lightgray")
            d5.config(bg="lightgray")
            e3.config(bg="lightgray")
            e4.config(bg="lightgray")
            e5.config(bg="lightgray")
        elif EE4 == 0 and EE3 == "X" and EE5 == 0 and DD3 == 0 and DD4 == 0 and DD5 == 0:
            e4.config(bg="lightgray")
        elif EE4 == 0 and EE3 == 0 and EE5 == "X" and DD3 == 0 and DD4 == 0 and DD5 == 0:
            e4.config(bg="lightgray")
        elif EE4 == 0 and EE3 == 0 and EE5 == 0 and DD3 == "X" and DD4 == 0 and DD5 == 0:
            e4.config(bg="lightgray")
        elif EE4 == 0 and EE3 == 0 and EE5 == 0 and DD3 == 0 and DD4 == "X" and DD5 == 0:
            e4.config(bg="lightgray")
        elif EE4 == 0 and EE3 == 0 and EE5 == 0 and DD3 == 0 and DD4 == 0 and DD5 == "X":
            e4.config(bg="lightgray")
        elif EE4 == "X":
            e4.config(bg="red", text="X")
            winsound.Beep(250, 300)
        else:
            e4.config(bg="lightgray")
    elif symb == 25:
        if EE5 == 0 and EE4 == 0 and DD4 == 0 and DD5 == 0:
            d4.config(bg="lightgray")
            d5.config(bg="lightgray")
            e4.config(bg="lightgray")
            e5.config(bg="lightgray")
        elif EE5 == 0 and EE4 == "X" and DD4 == 0 and DD5 == 0:
            e5.config(bg="lightgray")
        elif EE5 == 0 and EE4 == 0 and DD4 == "X" and DD5 == 0:
            e5.config(bg="lightgray")
        elif EE5 == 0 and EE4 == 0 and DD4 == 0 and DD5 == "X":
            e5.config(bg="lightgray")
        elif EE5 == "X":
            e5.config(bg="red", text="X")
            winsound.Beep(250, 300)
        else:
            e5.config(bg="lightgray")

def start():
    root.config(bg="gray")
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
    if goodluck == 1:
        AA1 = "X"
    if goodluck == 2:
        AA2 = "X"
    if goodluck == 3:
        AA3 = "X"
    if goodluck == 4:
        AA4 = "X"
    if goodluck == 5:
        AA5 = "X"
    if goodluck == 6:
        BB1 = "X"
    if goodluck2 == 7:
        BB2 = "X"
    if goodluck2 == 8:
        BB3 = "X"
    if goodluck2 == 9:
        BB4 = "X"
    if goodluck2 == 10:
        BB5 = "X"
    if goodluck2 == 11:
        CC1 = "X"
    if goodluck2 == 12:
        CC2 = "X"
    if goodluck3 == 13:
        CC3 = "X"
    if goodluck3 == 14:
        CC4 = "X"
    if goodluck3 == 15:
        CC5 = "X"
    if goodluck3 == 16:
        DD1 = "X"
    if goodluck3 == 17:
        DD2 = "X"
    if goodluck3 == 18:
        DD3 = "X"
    if goodluck3 == 19:
        DD4 = "X"
    if goodluck4 == 20:
        DD5 = "X"
    if goodluck4 == 21:
        EE1 = "X"
    if goodluck4 == 22:
        EE2 = "X"
    if goodluck4 == 23:
        EE3 = "X"
    if goodluck4 == 24:
        EE4 = "X"
    if goodluck4 == 25:
        EE5 = "X"


startbt = tk.Button(root, command=start, text="Start")
startbt.place(x=100, y=100, height=40, width=100)


root.mainloop()