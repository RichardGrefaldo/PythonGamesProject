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
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About","MineSweeper by Richard\nVersion 20240119"))
help_menu.add_command(label="Changelog", command=lambda: messagebox.showinfo("Changelog","Version 20240119\n -Added Win or Lose condition\n -Added Score Counter\nVersion 20240116\n- Added 'Clear Expansion' tiles will\n now uncover adjacent safe tiles\n -Added Sound Effect\nVersion 20240115\n -Initial Release"))
title = tk.Label(root,text ="MineSweeper",font=('Arial',20))
title.place(x=70, y=20)
title2 = tk.Label(root,text ="by Richard",font=('Arial',12))
title2.place(x=110, y=55)
message1 = tk.Label()
message1.place()
def event():
    global message1
    if score > 20:
        message1 = tk.Label(root, text="You Win", bg="gray", font=('Arial', 18))
        message1.place(x=88, y=10)
    else:
        message1 = tk.Label(root, text="Game Over", bg="gray", font=('Arial', 18))
        message1.place(x=88, y=10)
    a1.config(state="disabled");a2.config(state="disabled");a3.config(state="disabled");a4.config(state="disabled");a5.config(state="disabled")
    b1.config(state="disabled");b2.config(state="disabled");b3.config(state="disabled");b4.config(state="disabled");b5.config(state="disabled")
    c1.config(state="disabled");c2.config(state="disabled");c3.config(state="disabled");c4.config(state="disabled");c5.config(state="disabled")
    d1.config(state="disabled");d2.config(state="disabled");d3.config(state="disabled");d4.config(state="disabled");d5.config(state="disabled")
    e1.config(state="disabled");e2.config(state="disabled");e3.config(state="disabled");e4.config(state="disabled");e5.config(state="disabled")

def paint(symb):
    global score, mine, AA1V,AA2V,AA3V,AA4V,AA5V,BB1V,BB2V,BB3V,BB4V,BB5V,CC1V,CC2V,CC3V,CC4V,CC5V,DD1V,DD2V,DD3V,DD4V,DD5V,EE1V,EE2V,EE3V,EE4V,EE5V
    if symb == 1:
        AA1V = 1
        if AA1 == 0 and AA2 == 0 and BB1 == 0 and BB2 == 0:
            a1.config(bg="lightgray",state="disabled")
            a2.config(bg="lightgray",state="disabled")
            b1.config(bg="lightgray",state="disabled")
            b2.config(bg="lightgray",state="disabled")
            score = score + 4 - AA2V - BB2V - BB1V
            AA2V,BB2V,BB1V = 1,1,1,
        elif AA1 == "X":
            a1.config(bg="red", text="X",state="disabled")
            winsound.Beep(250, 300)
            mine = + 1
        else:
            a1.config(bg="lightgray",state="disabled")
            score =  score + 1

#tile two
    elif symb == 2:
        AA2V = 1
        if AA2 == 0 and AA1 == 0 and BB1 == 0 and BB2 == 0 and AA3 == 0 and BB3 == 0:
            a1.config(bg="lightgray",state="disabled")
            a2.config(bg="lightgray",state="disabled")
            a3.config(bg="lightgray",state="disabled")
            b1.config(bg="lightgray",state="disabled")
            b2.config(bg="lightgray",state="disabled")
            b3.config(bg="lightgray",state="disabled")
            score = score + 6 - AA1V - AA3V - BB1V - BB2V -BB3V
            AA1V,AA3V,BB1V,BB2V,BB3V = 1,1,1,1,1,
        elif AA2 == "X":
            a2.config(bg="red", text="X",state="disabled")
            winsound.Beep(250, 300)
            mine = + 1
        else:
            a2.config(bg="lightgray",state="disabled")
            score = score + 1

    elif symb == 3:
        AA3V = 1
        if AA3 == 0 and AA2 == 0 and AA4 == 0 and BB2 == 0 and BB3 == 0 and BB4 == 0:
            a2.config(bg="lightgray",state="disabled")
            a3.config(bg="lightgray",state="disabled")
            a4.config(bg="lightgray",state="disabled")
            b2.config(bg="lightgray",state="disabled")
            b3.config(bg="lightgray",state="disabled")
            b4.config(bg="lightgray",state="disabled")
            score = score + 6 - AA2V - AA4V - BB2V - BB3V - BB4V
            AA2V,AA4V,BB2V,BB3V,BB4V = 1,1,1,1,1
        elif AA3 == "X":
            a3.config(bg="red", text="X",state="disabled")
            winsound.Beep(250, 300)
            mine = + 1
        else:
            a3.config(bg="lightgray",state="disabled")
            score = score + 1
    elif symb == 4:
        AA4V = 1
        if AA4 == 0 and AA3 == 0 and AA5 == 0 and BB3 == 0 and BB4 == 0 and BB5 == 0:
            a3.config(bg="lightgray",state="disabled")
            a4.config(bg="lightgray",state="disabled")
            a5.config(bg="lightgray",state="disabled")
            b3.config(bg="lightgray",state="disabled")
            b4.config(bg="lightgray",state="disabled")
            b5.config(bg="lightgray",state="disabled")
            score = score + 6 - AA3V - AA5V - BB3V - BB4V - BB5V
            AA3V,AA5V,BB3V,BB4V,BB5V = 1,1,1,1,1
        elif AA4 == "X":
            a4.config(bg="red", text="X",state="disabled")
            winsound.Beep(250, 300)
            mine = + 1
        else:
            a4.config(bg="lightgray",state="disabled")
            score = score + 1
    elif symb == 5:
        AA5V = 1
        if AA5 == 0 and AA4 == 0 and BB4 == 0 and BB5 == 0:
            a4.config(bg="lightgray",state="disabled")
            a5.config(bg="lightgray",state="disabled")
            b4.config(bg="lightgray",state="disabled")
            b5.config(bg="lightgray",state="disabled")
            score = score + 4 - AA4V - BB4V - BB5V
            AA4V,BB4V,BB5V = 1,1,1
        elif AA5 == "X":
            a5.config(bg="red", text="X",state="disabled")
            winsound.Beep(250, 300)
            mine = + 1
        else:
            a5.config(bg="lightgray",state="disabled")
            score = score + 1
    elif symb == 6:
        BB1V = 1
        if BB1 == 0 and AA1 == 0 and CC1 == 0 and AA2 == 0 and BB2 == 0 and CC2 == 0:
            a1.config(bg="lightgray",state="disabled")
            a2.config(bg="lightgray",state="disabled")
            b1.config(bg="lightgray",state="disabled")
            b2.config(bg="lightgray",state="disabled")
            c1.config(bg="lightgray",state="disabled")
            c2.config(bg="lightgray",state="disabled")
            score = score + 6 - BB2V - AA1V - AA2V - CC1V - CC2V
            BB2V,AA1V,AA2V,CC1V,CC2V = 1,1,1,1,1
        elif BB1 == "X":
            b1.config(bg="red", text="X",state="disabled")
            winsound.Beep(250, 300)
            mine = + 1
        else:
            b1.config(bg="lightgray",state="disabled")
            score = score + 1

    elif symb == 7:
        BB2V = 1
        if BB2 == 0 and BB1 == 0 and AA1 == 0 and AA2 == 0 and AA3 == 0 and BB3 == 0 and CC1 == 0 and CC2 == 0 and CC3 ==0:
            a1.config(bg="lightgray",state="disabled")
            a2.config(bg="lightgray",state="disabled")
            a3.config(bg="lightgray",state="disabled")
            b1.config(bg="lightgray",state="disabled")
            b2.config(bg="lightgray",state="disabled")
            b3.config(bg="lightgray",state="disabled")
            c1.config(bg="lightgray",state="disabled")
            c2.config(bg="lightgray",state="disabled")
            c3.config(bg="lightgray",state="disabled")
            score = score + 9 - BB1V - BB3V - AA1V - AA2V -AA3V - CC1V - CC2V - CC3V
            BB1V,BB3V,AA1V,AA2V,AA3V,CC1V,CC2V,CC3V = 1,1,1,1,1,1,1,1
        elif BB2 == "X":
            b2.config(bg="red", text="X",state="disabled")
            winsound.Beep(250, 300)
            mine = + 1
        else:
            b2.config(bg="lightgray",state="disabled")
            score = score + 1

    elif symb == 8:
        BB3V = 1
        if BB3 == 0 and BB2 == 0 and BB4 == 0 and AA2 == 0 and AA3 == 0 and AA4 == 0 and CC2 == 0 and CC3 == 0 and CC4 == 0:
            b2.config(bg="lightgray",state="disabled")
            b3.config(bg="lightgray",state="disabled")
            b4.config(bg="lightgray",state="disabled")
            a2.config(bg="lightgray",state="disabled")
            a3.config(bg="lightgray",state="disabled")
            a4.config(bg="lightgray",state="disabled")
            c2.config(bg="lightgray",state="disabled")
            c3.config(bg="lightgray",state="disabled")
            c4.config(bg="lightgray",state="disabled")
            score = score + 9 - BB2V - BB4V - AA2V - AA3V - AA4V - CC2V - CC3V - CC4V
            BB2V,BB4V,AA2V,AA3V,AA4V,CC2V,CC3V,CC4V = 1,1,1,1,1,1,1,1
        elif BB3 == "X":
            b3.config(bg="red", text="X",state="disabled")
            winsound.Beep(250, 300)
            mine = + 1
        else:
            b3.config(bg="lightgray",state="disabled")
            score = score + 1
    elif symb == 9:
        BB4V = 1
        if BB4 == 0 and BB3 == 0 and BB5 == 0 and AA3 == 0 and AA4 == 0 and AA5 == 0 and CC3 == 0 and CC4 == 0 and CC5 == 0:
            b3.config(bg="lightgray",state="disabled")
            b4.config(bg="lightgray",state="disabled")
            b5.config(bg="lightgray",state="disabled")
            a3.config(bg="lightgray",state="disabled")
            a4.config(bg="lightgray",state="disabled")
            a5.config(bg="lightgray",state="disabled")
            c3.config(bg="lightgray",state="disabled")
            c4.config(bg="lightgray",state="disabled")
            c5.config(bg="lightgray",state="disabled")
            score = score + 9 - BB3V - BB5V - AA3V - AA4V - AA5V - CC3V - CC4V - CC5V
            BB3V,BB5V,AA3V,AA4V,AA5V,CC3V,CC4V,CC5V = 1,1,1,1,1,1,1,1
        elif BB4 == "X":
            b4.config(bg="red", text="X",state="disabled")
            winsound.Beep(250, 300)
            mine = + 1
        else:
            b4.config(bg="lightgray",state="disabled")
            score = score + 1
    elif symb == 10:
        BB5V = 1
        if BB5 == 0 and BB4 == 0 and AA4 == 0 and AA5 == 0 and CC4 == 0 and CC5 == 0:
            b4.config(bg="lightgray",state="disabled")
            b5.config(bg="lightgray",state="disabled")
            a4.config(bg="lightgray",state="disabled")
            a5.config(bg="lightgray",state="disabled")
            c4.config(bg="lightgray",state="disabled")
            c5.config(bg="lightgray",state="disabled")
            score = score + 6 - BB4V - AA4V - AA5V - CC4V - CC5V
            BB4V,AA4V,AA5V,CC4V,CC5V = 1,1,1,1,1
        elif BB5 == "X":
            b5.config(bg="red", text="X",state="disabled")
            winsound.Beep(250, 300)
            mine = + 1
        else:
            b5.config(bg="lightgray",state="disabled")
            score = score + 1
    elif symb == 11:
        CC1V = 1
        if CC1 == 0 and BB1 == 0 and BB2 == 0 and CC2 == 0 and DD1 == 0 and DD2 == 0:
            b1.config(bg="lightgray",state="disabled")
            b2.config(bg="lightgray",state="disabled")
            c1.config(bg="lightgray",state="disabled")
            c2.config(bg="lightgray",state="disabled")
            d1.config(bg="lightgray",state="disabled")
            d2.config(bg="lightgray",state="disabled")
            score = score + 6 - BB1V - BB2V - CC2V - DD1V - DD2V
            BB1V,BB2V,CC2V,DD1V,DD2V = 1,1,1,1,1
        elif CC1 == "X":
            c1.config(bg="red", text="X",state="disabled")
            winsound.Beep(250, 300)
            mine = + 1
        else:
            c1.config(bg="lightgray",state="disabled")
            score = score + 1
    elif symb == 12:
        CC2V = 1
        if CC2 == 0 and CC1 == 0 and CC3 == 0 and BB1 == 0 and BB2 == 0 and BB3 == 0 and DD1 == 0 and DD2 == 0 and DD3 == 0:
            c1.config(bg="lightgray",state="disabled")
            c2.config(bg="lightgray",state="disabled")
            c3.config(bg="lightgray",state="disabled")
            b1.config(bg="lightgray",state="disabled")
            b2.config(bg="lightgray",state="disabled")
            b3.config(bg="lightgray",state="disabled")
            d1.config(bg="lightgray",state="disabled")
            d2.config(bg="lightgray",state="disabled")
            d3.config(bg="lightgray",state="disabled")
            score = score + 9 - CC1V - CC3V -BB1V - BB2V - BB3V - DD1V - DD2V - DD3V
            CC1V,CC3V,BB1V,BB2V,BB3V,DD1V,DD2V,DD3V = 1,1,1,1,1,1,1,1
        elif CC2 == "X":
            c2.config(bg="red", text="X",state="disabled")
            winsound.Beep(250, 300)
            mine = + 1
        else:
            c2.config(bg="lightgray",state="disabled")
            score = score + 1
    elif symb == 13:
        CC3V = 1
        if CC3 == 0 and CC2 == 0 and CC4 == 0 and BB2 == 0 and BB3 == 0 and BB4 == 0 and DD2 == 0 and DD3 == 0 and DD4 ==0:
            b2.config(bg="lightgray",state="disabled")
            b3.config(bg="lightgray",state="disabled")
            b4.config(bg="lightgray",state="disabled")
            c2.config(bg="lightgray",state="disabled")
            c3.config(bg="lightgray",state="disabled")
            c4.config(bg="lightgray",state="disabled")
            d2.config(bg="lightgray",state="disabled")
            d3.config(bg="lightgray",state="disabled")
            d4.config(bg="lightgray",state="disabled")
            score = score + 9 - CC2V - CC4V - BB2V - BB3V - BB4V - DD2V - DD3V - DD4V
            CC2V,CC4V,BB2V,BB3V,BB4V,DD2V,DD3V,DD4V = 1,1,1,1,1,1,1,1
        elif CC3 == "X":
            c3.config(bg="red", text="X",state="disabled")
            winsound.Beep(250, 300)
            mine = + 1
        else:
            c3.config(bg="lightgray",state="disabled")
            score = score + 1
    elif symb == 14:
        CC4V = 1
        if CC4 == 0 and CC3 == 0 and CC5 == 0 and BB3 == 0 and BB4 == 0 and BB5 == 0 and DD3 == 0 and DD4 == 0 and DD5 == 0:
            b3.config(bg="lightgray",state="disabled")
            b4.config(bg="lightgray", state="disabled")
            b5.config(bg="lightgray", state="disabled")
            c3.config(bg="lightgray", state="disabled")
            c4.config(bg="lightgray", state="disabled")
            c5.config(bg="lightgray", state="disabled")
            d3.config(bg="lightgray", state="disabled")
            d4.config(bg="lightgray", state="disabled")
            d5.config(bg="lightgray", state="disabled")
            score = score + 9 - CC3V - CC5V - BB3V - BB4V - BB5V - DD3V - DD4V - DD5V
            CC3V,CC5V,BB3V,BB4V,BB5V,DD3V,DD4V,DD5V = 1,1,1,1,1,1,1,1
        elif CC4 == "X":
            c4.config(bg="red", text="X", state="disabled")
            winsound.Beep(250, 300)
            mine = + 1
        else:
            c4.config(bg="lightgray", state="disabled")
            score = score + 1
    elif symb == 15:
        CC5V = 1
        if CC5 == 0 and CC4 == 0 and BB4 == 0 and BB5 == 0 and DD4 == 0 and DD5 == 0:
            b4.config(bg="lightgray",state="disabled")
            b5.config(bg="lightgray",state="disabled")
            c4.config(bg="lightgray",state="disabled")
            c5.config(bg="lightgray",state="disabled")
            d4.config(bg="lightgray",state="disabled")
            d5.config(bg="lightgray",state="disabled")
            score = score + 6 - CC4V - BB4V -BB5V - DD4V -DD5V
            CC4V,BB4V,BB5V,DD4V,DD5V = 1,1,1,1,1
        elif CC5 == "X":
            c5.config(bg="red", text="X",state="disabled")
            winsound.Beep(250, 300)
            mine = + 1
        else:
            c5.config(bg="lightgray",state="disabled")
            score = score + 1
    elif symb == 16:
        DD1V = 1
        if DD1 == 0 and DD2 == 0 and CC1 == 0 and CC2 == 0 and EE1 == 0 and EE2 == 0:
            c1.config(bg="lightgray",state="disabled")
            c2.config(bg="lightgray",state="disabled")
            d1.config(bg="lightgray",state="disabled")
            d2.config(bg="lightgray",state="disabled")
            e1.config(bg="lightgray",state="disabled")
            e2.config(bg="lightgray",state="disabled")
            score = score + 6 - DD2V - CC1V - CC2V - EE1V - EE2V
            DD2V,CC1V,CC2V,EE1V,EE2V = 1,1,1,1,1
        elif DD1 == "X":
            d1.config(bg="red", text="X",state="disabled")
            winsound.Beep(250, 300)
            mine = + 1
        else:
            d1.config(bg="lightgray",state="disabled")
            score = score + 1
    elif symb == 17:
        DD2V = 1
        if DD2 == 0 and DD3 == 0 and DD1 == 0 and CC1 == 0 and CC2 == 0 and CC3 == 0 and EE1 == 0 and EE2 == 0 and EE3 == 0:
            c1.config(bg="lightgray",state="disabled")
            c2.config(bg="lightgray",state="disabled")
            c3.config(bg="lightgray",state="disabled")
            d1.config(bg="lightgray",state="disabled")
            d2.config(bg="lightgray",state="disabled")
            d3.config(bg="lightgray",state="disabled")
            e1.config(bg="lightgray",state="disabled")
            e2.config(bg="lightgray",state="disabled")
            e3.config(bg="lightgray",state="disabled")
            score = score + 9 - DD3V - DD1V - CC1V - CC2V - CC3V - EE1V - EE2V - EE3V
            DD3V,DD1V,CC1V,CC2V,CC3V,EE1V,EE2V,EE3V = 1,1,1,1,1,1,1,1
        elif DD2 == "X":
            d2.config(bg="red", text="X",state="disabled")
            winsound.Beep(250, 300)
            mine = + 1
        else:
            d2.config(bg="lightgray",state="disabled")
            score = score + 1
    elif symb == 18:
        DD3V = 1
        if DD3 == 0 and DD2 == 0 and DD4 == 0 and CC2 == 0 and CC3 == 0 and CC4 == 0 and EE2 == 0 and EE3 == 0 and EE4 == 0:
            c2.config(bg="lightgray",state="disabled")
            c3.config(bg="lightgray",state="disabled")
            c4.config(bg="lightgray",state="disabled")
            d2.config(bg="lightgray",state="disabled")
            d3.config(bg="lightgray",state="disabled")
            d4.config(bg="lightgray",state="disabled")
            e2.config(bg="lightgray",state="disabled")
            e3.config(bg="lightgray",state="disabled")
            e4.config(bg="lightgray",state="disabled")
            score = score + 9 - DD2V - DD4V - CC2V - CC3V - CC4V - EE2V - EE3V - EE4V
            DD2V,DD4V,CC2V,CC3V,CC4V,EE2V,EE3V,EE4V = 1,1,1,1,1,1,1,1
        elif DD3 == "X":
            d3.config(bg="red", text="X",state="disabled")
            winsound.Beep(250, 300)
            mine = + 1
        else:
            d3.config(bg="lightgray",state="disabled")
            score = score + 1
    elif symb == 19:
        DD4V = 1
        if DD4 == 0 and DD3 == 0 and DD5 == 0 and CC3 == 0 and CC4 == 0 and CC5 == 0 and EE3 == 0 and EE4 == 0 and EE5 == 0:
            c3.config(bg="lightgray",state="disabled")
            c4.config(bg="lightgray",state="disabled")
            c5.config(bg="lightgray",state="disabled")
            d3.config(bg="lightgray",state="disabled")
            d4.config(bg="lightgray",state="disabled")
            d5.config(bg="lightgray",state="disabled")
            e3.config(bg="lightgray",state="disabled")
            e4.config(bg="lightgray",state="disabled")
            e5.config(bg="lightgray",state="disabled")
            score = score + 9 - DD3V - DD5V - CC3V - CC4V - CC5V - EE3V - EE4V - EE5V
            DD3V,DD5V,CC3V,CC4V,CC5V,EE3V,EE4V,EE5V = 1,1,1,1,1,1,1,1
        elif DD4 == "X":
            d4.config(bg="red", text="X",state="disabled")
            winsound.Beep(250, 300)
            mine = + 1
        else:
            d4.config(bg="lightgray",state="disabled")
            score = score + 1
    elif symb == 20:
        DD5V = 1
        if DD5 == 0 and DD4 == 0 and CC4 == 0 and CC5 == 0 and EE4 == 0 and EE5 == 0:
            c4.config(bg="lightgray",state="disabled")
            c5.config(bg="lightgray",state="disabled")
            d4.config(bg="lightgray",state="disabled")
            d5.config(bg="lightgray",state="disabled")
            e4.config(bg="lightgray",state="disabled")
            e5.config(bg="lightgray",state="disabled")
            score = score + 6 - DD4V - CC4V - CC5V - EE4V - EE5V
            DD4V,CC4V,CC5V,EE4V,EE5V = 1,1,1,1,1
        elif DD5 == "X":
            d5.config(bg="red", text="X",state="disabled")
            winsound.Beep(250, 300)
            mine = + 1
        else:
            d5.config(bg="lightgray",state="disabled")
            score = score + 1
    elif symb == 21:
        EE1V = 1
        if EE1 == 0 and EE2 == 0 and DD1 == 0 and DD2 == 0:
            d1.config(bg="lightgray",state="disabled")
            d2.config(bg="lightgray",state="disabled")
            e1.config(bg="lightgray",state="disabled")
            e2.config(bg="lightgray",state="disabled")
            score = score + 4 - EE2V - DD1V - DD2V
            EE2V,DD1V,DD2V = 1,1,1
        elif EE1 == "X":
            e1.config(bg="red", text="X",state="disabled")
            winsound.Beep(250, 300)
            mine = + 1
        else:
            e1.config(bg="lightgray",state="disabled")
            score = score + 1
    elif symb == 22:
        EE2V = 1
        if EE2 == 0 and EE1 == 0 and EE3 == 0 and DD1 == 0 and DD2 == 0 and DD3 == 0:
            e1.config(bg="lightgray",state="disabled")
            e2.config(bg="lightgray",state="disabled")
            e3.config(bg="lightgray",state="disabled")
            d1.config(bg="lightgray",state="disabled")
            d2.config(bg="lightgray",state="disabled")
            d3.config(bg="lightgray",state="disabled")
            score = score + 6 - EE1V - EE3V - DD1V - DD2V - DD3V
            EE1V,EE3V,DD1V,DD2V,DD3V = 1,1,1,1,1
        elif EE2 == "X":
            e2.config(bg="red", text="X",state="disabled")
            winsound.Beep(250, 300)
            mine = + 1
        else:
            e2.config(bg="lightgray",state="disabled")
            score = score + 1
    elif symb == 23:
        EE3V = 1
        if EE3 == 0 and EE2 == 0 and EE4 == 0 and DD2 == 0 and DD3 == 0 and DD4 == 0:
            e2.config(bg="lightgray",state="disabled")
            e3.config(bg="lightgray",state="disabled")
            e4.config(bg="lightgray",state="disabled")
            d2.config(bg="lightgray",state="disabled")
            d3.config(bg="lightgray",state="disabled")
            d4.config(bg="lightgray",state="disabled")
            score = score + 6 - EE2V - EE4V - DD2V - DD3V - DD4V
            EE2V,EE4V,DD2V,DD3V,DD4V = 1,1,1,1,1
        elif EE3 == "X":
            e3.config(bg="red", text="X",state="disabled")
            winsound.Beep(250, 300)
            mine = + 1
        else:
            e3.config(bg="lightgray",state="disabled")
            score = score + 1
    elif symb == 24:
        EE4V = 1
        if EE4 == 0 and EE3 == 0 and EE5 == 0 and DD3 == 0 and DD4 ==0 and DD5 == 0:
            d3.config(bg="lightgray",state="disabled")
            d4.config(bg="lightgray",state="disabled")
            d5.config(bg="lightgray",state="disabled")
            e3.config(bg="lightgray",state="disabled")
            e4.config(bg="lightgray",state="disabled")
            e5.config(bg="lightgray",state="disabled")
            score = score + 6 - EE3V - EE5V - DD3V - DD4V - DD5V
            EE3V,EE5V,DD3V,DD4V,DD5V = 1,1,1,1,1
        elif EE4 == "X":
            e4.config(bg="red", text="X",state="disabled")
            winsound.Beep(250, 300)
            mine = + 1
        else:
            e4.config(bg="lightgray",state="disabled")
            score = score + 1
    elif symb == 25:
        EE5V = 1
        if EE5 == 0 and EE4 == 0 and DD4 == 0 and DD5 == 0:
            d4.config(bg="lightgray",state="disabled")
            d5.config(bg="lightgray",state="disabled")
            e4.config(bg="lightgray",state="disabled")
            e5.config(bg="lightgray",state="disabled")
            score = score + 4 - EE4V - DD4V - DD5V
            EE4V,DD4V,DD5V = 1,1,1
        elif EE5 == "X":
            e5.config(bg="red", text="X",state="disabled")
            winsound.Beep(250, 300)
            mine = + 1
        else:
            e5.config(bg="lightgray",state="disabled")
            score = score + 1
    if mine == 1:
        event()
    if score > 20:
        event()
    scorelabel = tk.Label(root, text=f"Tiles cleared: {score}")
    scorelabel.place(x=0, y=0)
def start():
    title.place_forget()
    title2.place_forget()
    root.config(bg="gray")
    startbt.config(text="Play Again")
    startbt.place(x=100,y=250)
    global a1,a2,a3,a4,a5,b1,b2,b3,b4,b5,c1,c2,c3,c4,c5,d1,d2,d3,d4,d5,e1,e2,e3,e4,e5,score,mine,message1
    global AA1V,AA2V,AA3V,AA4V,AA5V,BB1V,BB2V,BB3V,BB4V,BB5V,CC1V,CC2V,CC3V,CC4V,CC5V,DD1V,DD2V,DD3V,DD4V,DD5V,EE1V,EE2V,EE3V,EE4V,EE5V
    AA1V, AA2V, AA3V, AA4V, AA5V, BB1V,BB2V, BB3V, BB4V, BB5V = 0,0,0,0,0,0,0,0,0,0
    CC1V, CC2V, CC3V, CC4V, CC5V, DD1V, DD2V, DD3V, DD4V, DD5V = 0,0,0,0,0,0,0,0,0,0
    EE1V, EE2V, EE3V, EE4V, EE5V = 0,0,0,0,0
    score = 0
    mine = 0
    message1.place_forget()
    a1 = tk.Button(root, command=lambda: paint(1))
    a1.place(x=50, y=50, height=40, width=40)
    a2 = tk.Button(root, command=lambda: paint(2))
    a2.place(x=50, y=90, height=40, width=40)
    a3 = tk.Button(root, command=lambda: paint(3))
    a3.place(x=50, y=130, height=40, width=40)
    a4 = tk.Button(root, command=lambda: paint(4))
    a4.place(x=50, y=170, height=40, width=40)
    a5 = tk.Button(root, command=lambda: paint(5))
    a5.place(x=50, y=210, height=40, width=40)
    b1 = tk.Button(root, command=lambda: paint(6))
    b1.place(x=90, y=50, height=40, width=40)
    b2 = tk.Button(root, command=lambda: paint(7))
    b2.place(x=90, y=90, height=40, width=40)
    b3 = tk.Button(root, command=lambda: paint(8))
    b3.place(x=90, y=130, height=40, width=40)
    b4 = tk.Button(root, command=lambda: paint(9))
    b4.place(x=90, y=170, height=40, width=40)
    b5 = tk.Button(root, command=lambda: paint(10))
    b5.place(x=90, y=210, height=40, width=40)
    c1 = tk.Button(root, command=lambda: paint(11))
    c1.place(x=130, y=50, height=40, width=40)
    c2 = tk.Button(root, command=lambda: paint(12))
    c2.place(x=130, y=90, height=40, width=40)
    c3 = tk.Button(root, command=lambda: paint(13))
    c3.place(x=130, y=130, height=40, width=40)
    c4 = tk.Button(root, command=lambda: paint(14))
    c4.place(x=130, y=170, height=40, width=40)
    c5 = tk.Button(root, command=lambda: paint(15))
    c5.place(x=130, y=210, height=40, width=40)
    d1 = tk.Button(root, command=lambda: paint(16))
    d1.place(x=170, y=50, height=40, width=40)
    d2 = tk.Button(root, command=lambda: paint(17))
    d2.place(x=170, y=90, height=40, width=40)
    d3 = tk.Button(root, command=lambda: paint(18))
    d3.place(x=170, y=130, height=40, width=40)
    d4 = tk.Button(root, command=lambda: paint(19))
    d4.place(x=170, y=170, height=40, width=40)
    d5 = tk.Button(root, command=lambda: paint(20))
    d5.place(x=170, y=210, height=40, width=40)
    e1 = tk.Button(root,command=lambda: paint(21))
    e1.place(x=210, y=50, height=40, width=40)
    e2 = tk.Button(root, command=lambda: paint(22))
    e2.place(x=210, y=90, height=40, width=40)
    e3 = tk.Button(root, command=lambda: paint(23))
    e3.place(x=210, y=130, height=40, width=40)
    e4 = tk.Button(root, command=lambda: paint(24))
    e4.place(x=210, y=170, height=40, width=40)
    e5 = tk.Button(root, command=lambda: paint(25))
    e5.place(x=210, y=210, height=40, width=40)
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