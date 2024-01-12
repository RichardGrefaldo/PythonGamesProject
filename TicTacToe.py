import tkinter as tk
from tkinter import Menu
from tkinter import messagebox
root = tk.Tk()
root.geometry('300x400')
root.title('TicTacToe')
about = Menu(root)
root.config(menu=about)
help_menu = Menu(about, tearoff=0)
about.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Instruction", command=lambda: messagebox.showinfo("Help","1.Objective:\n  The Goal is to get three of\n  your symbols(X or O)in a row,\n  either horizontally, vertically, or diagonally."))
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About","Tic Tac Toe by Richard Grefaldo\nVersion 20240112.1\n418 lines of code"))
help_menu.add_command(label="Changelog", command=lambda: messagebox.showinfo("Changelog","Version 20240112.1\n -Winning Condition Added \n -Colors Added\nVersion 20240112\n -Game Logic added\nVersion 20240111\n -Initial release UI only"))
counter = 0
AA1, AA2, AA3, BB1, BB2, BB3, CC1, CC2, CC3 = 0, 0, 0, 0, 0, 0, 0, 0, 0
turn = tk.Label(root, text="Current Turn:X", font=('Arial',20))
turn.place(x=20, y=300)

def paint(symb):
    global data, counter, player, player2, AA1, AA2, AA3, BB1, BB2, BB3,CC1,CC2,CC3,a1,a2,a3,b1,b2,b3,c1,c2,c3
    counter = counter + 1
    data = counter % 2
    if data == 1:
        turn = tk.Label(root, text="Current Turn:O", font=('Arial', 20))
        turn.place(x=20, y=300)
    else:
        turn = tk.Label(root, text="Current Turn:X", font=('Arial', 20))
        turn.place(x=20, y=300)
    if symb == 1:
        if data == 1:
            a1 = tk.Button(root, text="X", font=('Arial',40))
            a1.place(x=30, y=50, height=80, width=80)
            AA1 = 'X'
            if AA2 == 'X'and AA3=='X':
                winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a1.config(bg="gold")
                a2.config(bg="gold")
                a3.config(bg="gold")
            elif BB1 == 'X' and CC1 == 'X':
                winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a1.config(bg="gold")
                b1.config(bg="gold")
                c1.config(bg="gold")
            elif BB2 == 'X' and CC3 == 'X':
                winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a1.config(bg="gold")
                b2.config(bg="gold")
                c3.config(bg="gold")
        else:
            a1 = tk.Button(root, text="O",font=('Arial',40))
            a1.place(x=30, y=50, height=80, width=80)
            AA1 = 'O'
            if AA2 == 'O'and AA3=='O':
                winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a1.config(bg="gold")
                a2.config(bg="gold")
                a3.config(bg="gold")
            elif BB1 == 'O' and CC1 == 'O':
                winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a1.config(bg="gold")
                b1.config(bg="gold")
                c1.config(bg="gold")
            elif BB2 == 'O' and CC3 == 'O':
                winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a1.config(bg="gold")
                b2.config(bg="gold")
                c3.config(bg="gold")
    elif symb == 2:
        if data == 1:
            a2 = tk.Button(root, text="X",font=('Arial',40))
            a2.place(x=30, y=130, height=80, width=80)
            AA2 = 'X'
            if AA1 == 'X' and AA3 == 'X':
                winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a1.config(bg="gold")
                a2.config(bg="gold")
                a3.config(bg="gold")
            elif BB2 == 'X' and CC2 == 'X':
                winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a2.config(bg="gold")
                b2.config(bg="gold")
                c2.config(bg="gold")
        else:
            a2 = tk.Button(root, text="O",font=('Arial',40))
            a2.place(x=30, y=130, height=80, width=80)
            AA2 = 'O'
            if AA1 == 'O' and AA3 == 'O':
                winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a1.config(bg="gold")
                a2.config(bg="gold")
                a3.config(bg="gold")
            elif BB2 == 'O' and CC2 == 'O':
                winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a2.config(bg="gold")
                b2.config(bg="gold")
                c2.config(bg="gold")
    elif symb == 3:
        if data == 1:
            a3 = tk.Button(root, text="X",font=('Arial',40))
            a3.place(x=30, y=210, height=80, width=80)
            AA3 = 'X'
            if AA1 == 'X' and AA2 == 'X':
                winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a1.config(bg="gold")
                a2.config(bg="gold")
                a3.config(bg="gold")
            elif BB3 == 'X' and CC3 == 'X':
                winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a3.config(bg="gold")
                b3.config(bg="gold")
                c3.config(bg="gold")
            elif BB2 == 'X' and CC1 == 'X':
                winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a3.config(bg="gold")
                b2.config(bg="gold")
                c1.config(bg="gold")
        else:
            a3 = tk.Button(root, text="O",font=('Arial',40))
            a3.place(x=30, y=210, height=80, width=80)
            AA3 = 'O'
            if AA1 == 'O' and AA2 == 'O':
                winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a1.config(bg="gold")
                a2.config(bg="gold")
                a3.config(bg="gold")
            elif BB3 == 'O' and CC3 == 'O':
                winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a3.config(bg="gold")
                b3.config(bg="gold")
                c3.config(bg="gold")
            elif BB2 == 'O' and CC1 == 'O':
                winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a3.config(bg="gold")
                b2.config(bg="gold")
                c1.config(bg="gold")
    elif symb == 4:
        if data == 1 :
            b1 = tk.Button(root, text="X",font=('Arial',40))
            b1.place(x=110, y=50, height=80, width=80)
            BB1 = 'X'
            if AA1 == 'X' and CC1 == 'X':
                winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a1.config(bg="gold")
                b1.config(bg="gold")
                c1.config(bg="gold")
            elif BB2 == 'X' and BB3 == 'X':
                winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                b1.config(bg="gold")
                b2.config(bg="gold")
                b3.config(bg="gold")
        else:
            b1 = tk.Button(root, text="O",font=('Arial',40))
            b1.place(x=110, y=50, height=80, width=80)
            BB1 = 'O'
            if AA1 == 'O' and CC1 == 'O':
                winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a1.config(bg="gold")
                b1.config(bg="gold")
                c1.config(bg="gold")
            elif BB2 == 'O' and BB3 == 'O':
                winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                b1.config(bg="gold")
                b2.config(bg="gold")
                b3.config(bg="gold")
    elif symb == 5:
        if data == 1:
            b2 = tk.Button(root, text="X",font=('Arial',40))
            b2.place(x=110, y=130, height=80, width=80)
            BB2 = 'X'
            if AA1 == 'X' and CC3 == 'X':
                winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a1.config(bg="gold")
                b2.config(bg="gold")
                c3.config(bg="gold")
            elif AA2 == 'X' and CC2 == 'X':
                winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a2.config(bg="gold")
                b2.config(bg="gold")
                c2.config(bg="gold")
            elif AA3 == 'X' and CC1 == 'X':
                winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a3.config(bg="gold")
                b2.config(bg="gold")
                c1.config(bg="gold")
            elif BB1 == 'X' and BB3 == 'X':
                winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                b1.config(bg="gold")
                b2.config(bg="gold")
                b3.config(bg="gold")
        else:
            b2 = tk.Button(root, text="O",font=('Arial',40))
            b2.place(x=110, y=130, height=80, width=80)
            BB2 = 'O'
            if AA1 == 'O' and CC3 == 'O':
                winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a1.config(bg="gold")
                b2.config(bg="gold")
                c3.config(bg="gold")
            elif AA2 == 'O' and CC2 == 'O':
                winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a2.config(bg="gold")
                b2.config(bg="gold")
                c2.config(bg="gold")
            elif AA3 == 'O' and CC1 == 'O':
                winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a3.config(bg="gold")
                b2.config(bg="gold")
                c1.config(bg="gold")
            elif BB1 == 'O' and BB3 == 'O':
                winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                b1.config(bg="gold")
                b2.config(bg="gold")
                b3.config(bg="gold")
    elif symb == 6:
        if data == 1:
            b3 = tk.Button(root, text="X",font=('Arial',40))
            b3.place(x=110, y=210, height=80, width=80)
            BB3 = 'X'
            if AA3 == 'X' and CC3 == 'X':
                winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a3.config(bg="gold")
                b3.config(bg="gold")
                c3.config(bg="gold")
            elif BB1 == 'X' and BB2 == 'X':
                winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                b1.config(bg="gold")
                b2.config(bg="gold")
                b3.config(bg="gold")
        else:
            b3 = tk.Button(root, text="O",font=('Arial',40))
            b3.place(x=110, y=210, height=80, width=80)
            BB3 = 'O'
            if AA3 == 'O' and CC3 == 'O':
                winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a3.config(bg="gold")
                b3.config(bg="gold")
                c3.config(bg="gold")
            elif BB1 == 'O' and BB2 == 'O':
                winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                b1.config(bg="gold")
                b2.config(bg="gold")
                b3.config(bg="gold")
    elif symb == 7:
        if data == 1:
            c1 = tk.Button(root, text="X",font=('Arial',40))
            c1.place(x=190, y=50, height=80, width=80)
            CC1 = 'X'
            if AA1 == 'X' and BB1 == 'X':
                winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a1.config(bg="gold")
                b1.config(bg="gold")
                c1.config(bg="gold")
            elif BB2 == 'X' and AA3 == 'X':
                winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a3.config(bg="gold")
                b2.config(bg="gold")
                c1.config(bg="gold")
            elif CC2 == 'X' and CC3 == 'X':
                winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                c1.config(bg="gold")
                c2.config(bg="gold")
                c3.config(bg="gold")
        else:
            c1 = tk.Button(root, text="O",font=('Arial',40))
            c1.place(x=190, y=50, height=80, width=80)
            CC1 = 'O'
            if AA1 == 'O' and BB1 == 'O':
                winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a1.config(bg="gold")
                b1.config(bg="gold")
                c1.config(bg="gold")
            elif BB2 == 'O' and AA3 == 'O':
                winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a3.config(bg="gold")
                b2.config(bg="gold")
                c1.config(bg="gold")
            elif CC2 == 'O' and CC3 == 'O':
                winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                c1.config(bg="gold")
                c2.config(bg="gold")
                c3.config(bg="gold")
    elif symb == 8:
        if data == 1:
            c2 = tk.Button(root, text="X",font=('Arial',40))
            c2.place(x=190, y=130, height=80, width=80)
            CC2 = 'X'
            if CC1 == 'X' and CC3 == 'X':
                winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                c1.config(bg="gold")
                c2.config(bg="gold")
                c3.config(bg="gold")
            elif AA2 == 'X' and BB2 == 'X':
                winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a2.config(bg="gold")
                b2.config(bg="gold")
                c2.config(bg="gold")
        else:
            c2 = tk.Button(root, text="O",font=('Arial',40))
            c2.place(x=190, y=130, height=80, width=80)
            CC2 = 'O'
            if CC1 == 'O' and CC3 == 'O':
                winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                c1.config(bg="gold")
                c2.config(bg="gold")
                c3.config(bg="gold")
            elif AA2 == 'O' and BB2 == 'O':
                winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a2.config(bg="gold")
                b2.config(bg="gold")
                c2.config(bg="gold")
    elif symb == 9:
        if data == 1:
            c3 = tk.Button(root,  text="X", font=('Arial',40))
            c3.place(x=190, y=210, height=80, width=80)
            CC3 = 'X'
            if CC1 == 'X' and CC2 == 'X':
                winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                c1.config(bg="gold")
                c2.config(bg="gold")
                c3.config(bg="gold")
            elif AA1 == 'X' and BB2 == 'X':
                winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a1.config(bg="gold")
                b2.config(bg="gold")
                c3.config(bg="gold")
            elif AA3 == 'X' and BB3 == 'X':
                winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a3.config(bg="gold")
                b3.config(bg="gold")
                c3.config(bg="gold")
        else:
            c3 = tk.Button(root, text="O", font=('Arial',40))
            c3.place(x=190, y=210, height=80, width=80)
            CC3 = 'O'
            if CC1 == 'O' and CC2 == 'O':
                winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                c1.config(bg="gold")
                c2.config(bg="gold")
                c3.config(bg="gold")
            elif AA1 == 'O' and BB2 == 'O':
                winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a1.config(bg="gold")
                b2.config(bg="gold")
                c3.config(bg="gold")
            elif AA3 == 'O' and BB3 == 'O':
                winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                winner.place(x=20, y=340)
                a3.config(bg="gold")
                b3.config(bg="gold")
                c3.config(bg="gold")


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