import tkinter as tk
from tkinter import Menu
from tkinter import messagebox
from tkinter import ttk
root = tk.Tk()
root.geometry('300x400')
root.title('TicTacToe')
about = Menu(root)
root.config(menu=about,bg="lightcyan2")
help_menu = Menu(about, tearoff=0)
about.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Instruction", command=lambda: messagebox.showinfo("Help","1.Objective:\n  The Goal is to get three of\n  your symbols(X or O)in a row,\n  either horizontally, vertically, or diagonally."))
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About","Tic Tac Toe by Richard Grefaldo\nVersion 20240113\n512 lines of code"))
help_menu.add_command(label="Changelog", command=lambda: messagebox.showinfo("Changelog","Version 20240113\n- Added Start or New Game Button\n -Added Win Counter\n -Added Background Color Selection\n -Added 94 lines of code\nVersion 20240112.1\n -Added Winning Condition\n -Added Colors\nVersion 20240112\n -Game Logic added\nVersion 20240111\n -Initial release UI only"))
turn = tk.Label(root, text="Current Turn:X", font=('Arial',20))
turn.place(x=20, y=300)
wincounterx,wincountero,xcheck,ocheck,counter = 0,0,0,0,0 # Initialize Variables
wincount = tk.Label(root, text=f"X Total Wins:{wincounterx}\nOTotal Wins:{wincountero}",font=('Arial',12))
wincount.place(x=10, y=5)
AA1, AA2, AA3, BB1, BB2, BB3, CC1, CC2, CC3 = 0, 0, 0, 0, 0, 0, 0, 0, 0
def newgame(): # Start/New game Button function
    newgamebt.config(text="Play Again")
    global xcheck, ocheck, AA1, AA2, AA3, BB1, BB2, BB3, CC1, CC2, CC3, wincounterx, wincountero
    AA1, AA2, AA3, BB1, BB2, BB3, CC1, CC2, CC3 = 0, 0, 0, 0, 0, 0, 0, 0, 0 # Reset value after pressing new game
    wincounterx = wincounterx + xcheck # counter for win
    wincountero = wincountero + ocheck
    xcheck, ocheck = 0, 0
    wincount = tk.Label(root, text=f"X Total Wins:{wincounterx}\nOTotal Wins:{wincountero}", font=('Arial', 12))
    wincount.place(x=10, y=5)

    def paint(symb):
        global xcheck,ocheck,data,counter,player,player2,AA1,AA2,AA3,BB1,BB2,BB3,CC1,CC2,CC3,a1,a2,a3,b1,b2,b3,c1,c2,c3
        counter = counter + 1
        data = counter % 2 # It determines if data is 1 or 0.
        if data == 1: # if 1 then it's O's turn
            turn = tk.Label(root, text="Current Turn:O", font=('Arial', 20))
            turn.place(x=20, y=300)
        else: # if 0 then it's X's turn
            turn = tk.Label(root, text="Current Turn:X", font=('Arial', 20))
            turn.place(x=20, y=300)
        if symb == 1: # parameter of paint function
            if data == 1:
                a1 = tk.Button(root, text="X", font=('Arial', 40))
                a1.place(x=30, y=50, height=80, width=80)
                AA1 = 'X'
                if AA2 == 'X' and AA3 == 'X': #winning condition
                    winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    xcheck = 1 # Counter for wins
                    a1.config(bg="gold")
                    a2.config(bg="gold")
                    a3.config(bg="gold")
                elif BB1 == 'X' and CC1 == 'X':
                    winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    xcheck = 1
                    a1.config(bg="gold")
                    b1.config(bg="gold")
                    c1.config(bg="gold")
                elif BB2 == 'X' and CC3 == 'X':
                    winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    xcheck = 1
                    a1.config(bg="gold")
                    b2.config(bg="gold")
                    c3.config(bg="gold")
            else:
                a1 = tk.Button(root, text="O", font=('Arial', 40))
                a1.place(x=30, y=50, height=80, width=80)
                AA1 = 'O'
                if AA2 == 'O' and AA3 == 'O':
                    winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    ocheck = 1
                    a1.config(bg="gold")
                    a2.config(bg="gold")
                    a3.config(bg="gold")
                elif BB1 == 'O' and CC1 == 'O':
                    winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    ocheck = 1
                    a1.config(bg="gold")
                    b1.config(bg="gold")
                    c1.config(bg="gold")
                elif BB2 == 'O' and CC3 == 'O':
                    winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    ocheck = 1
                    a1.config(bg="gold")
                    b2.config(bg="gold")
                    c3.config(bg="gold")
        elif symb == 2:
            if data == 1:
                a2 = tk.Button(root, text="X", font=('Arial', 40))
                a2.place(x=30, y=130, height=80, width=80)
                AA2 = 'X'
                if AA1 == 'X' and AA3 == 'X':
                    winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    xcheck = 1
                    a1.config(bg="gold")
                    a2.config(bg="gold")
                    a3.config(bg="gold")
                elif BB2 == 'X' and CC2 == 'X':
                    winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    xcheck = 1
                    a2.config(bg="gold")
                    b2.config(bg="gold")
                    c2.config(bg="gold")
            else:
                a2 = tk.Button(root, text="O", font=('Arial', 40))
                a2.place(x=30, y=130, height=80, width=80)
                AA2 = 'O'
                if AA1 == 'O' and AA3 == 'O':
                    winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    ocheck = 1
                    a1.config(bg="gold")
                    a2.config(bg="gold")
                    a3.config(bg="gold")
                elif BB2 == 'O' and CC2 == 'O':
                    winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    ocheck = 1
                    a2.config(bg="gold")
                    b2.config(bg="gold")
                    c2.config(bg="gold")
        elif symb == 3:
            if data == 1:
                a3 = tk.Button(root, text="X", font=('Arial', 40))
                a3.place(x=30, y=210, height=80, width=80)
                AA3 = 'X'
                if AA1 == 'X' and AA2 == 'X':
                    winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    xcheck = 1
                    a1.config(bg="gold")
                    a2.config(bg="gold")
                    a3.config(bg="gold")
                elif BB3 == 'X' and CC3 == 'X':
                    winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    xcheck = 1
                    a3.config(bg="gold")
                    b3.config(bg="gold")
                    c3.config(bg="gold")
                elif BB2 == 'X' and CC1 == 'X':
                    winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    xcheck = 1
                    a3.config(bg="gold")
                    b2.config(bg="gold")
                    c1.config(bg="gold")
            else:
                a3 = tk.Button(root, text="O", font=('Arial', 40))
                a3.place(x=30, y=210, height=80, width=80)
                AA3 = 'O'
                if AA1 == 'O' and AA2 == 'O':
                    winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    ocheck = 1
                    a1.config(bg="gold")
                    a2.config(bg="gold")
                    a3.config(bg="gold")
                elif BB3 == 'O' and CC3 == 'O':
                    winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    ocheck = 1
                    a3.config(bg="gold")
                    b3.config(bg="gold")
                    c3.config(bg="gold")
                elif BB2 == 'O' and CC1 == 'O':
                    winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    ocheck = 1
                    a3.config(bg="gold")
                    b2.config(bg="gold")
                    c1.config(bg="gold")
        elif symb == 4:
            if data == 1:
                b1 = tk.Button(root, text="X", font=('Arial', 40))
                b1.place(x=110, y=50, height=80, width=80)
                BB1 = 'X'
                if AA1 == 'X' and CC1 == 'X':
                    winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    xcheck = 1
                    a1.config(bg="gold")
                    b1.config(bg="gold")
                    c1.config(bg="gold")
                elif BB2 == 'X' and BB3 == 'X':
                    winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    xcheck = 1
                    b1.config(bg="gold")
                    b2.config(bg="gold")
                    b3.config(bg="gold")
            else:
                b1 = tk.Button(root, text="O", font=('Arial', 40))
                b1.place(x=110, y=50, height=80, width=80)
                BB1 = 'O'
                if AA1 == 'O' and CC1 == 'O':
                    winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    ocheck = 1
                    a1.config(bg="gold")
                    b1.config(bg="gold")
                    c1.config(bg="gold")
                elif BB2 == 'O' and BB3 == 'O':
                    winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    ocheck = 1
                    b1.config(bg="gold")
                    b2.config(bg="gold")
                    b3.config(bg="gold")
        elif symb == 5:
            if data == 1:
                b2 = tk.Button(root, text="X", font=('Arial', 40))
                b2.place(x=110, y=130, height=80, width=80)
                BB2 = 'X'
                if AA1 == 'X' and CC3 == 'X':
                    winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    xcheck = 1
                    a1.config(bg="gold")
                    b2.config(bg="gold")
                    c3.config(bg="gold")
                elif AA2 == 'X' and CC2 == 'X':
                    winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    xcheck = 1
                    a2.config(bg="gold")
                    b2.config(bg="gold")
                    c2.config(bg="gold")
                elif AA3 == 'X' and CC1 == 'X':
                    winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    xcheck = 1
                    a3.config(bg="gold")
                    b2.config(bg="gold")
                    c1.config(bg="gold")
                elif BB1 == 'X' and BB3 == 'X':
                    winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    xcheck = 1
                    b1.config(bg="gold")
                    b2.config(bg="gold")
                    b3.config(bg="gold")
            else:
                b2 = tk.Button(root, text="O", font=('Arial', 40))
                b2.place(x=110, y=130, height=80, width=80)
                BB2 = 'O'
                if AA1 == 'O' and CC3 == 'O':
                    winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    ocheck = 1
                    a1.config(bg="gold")
                    b2.config(bg="gold")
                    c3.config(bg="gold")
                elif AA2 == 'O' and CC2 == 'O':
                    winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    ocheck = 1
                    a2.config(bg="gold")
                    b2.config(bg="gold")
                    c2.config(bg="gold")
                elif AA3 == 'O' and CC1 == 'O':
                    winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    ocheck = 1
                    a3.config(bg="gold")
                    b2.config(bg="gold")
                    c1.config(bg="gold")
                elif BB1 == 'O' and BB3 == 'O':
                    winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    ocheck = 1
                    b1.config(bg="gold")
                    b2.config(bg="gold")
                    b3.config(bg="gold")
        elif symb == 6:
            if data == 1:
                b3 = tk.Button(root, text="X", font=('Arial', 40))
                b3.place(x=110, y=210, height=80, width=80)
                BB3 = 'X'
                if AA3 == 'X' and CC3 == 'X':
                    winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    xcheck = 1
                    a3.config(bg="gold")
                    b3.config(bg="gold")
                    c3.config(bg="gold")
                elif BB1 == 'X' and BB2 == 'X':
                    winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    xcheck = 1
                    b1.config(bg="gold")
                    b2.config(bg="gold")
                    b3.config(bg="gold")
            else:
                b3 = tk.Button(root, text="O", font=('Arial', 40))
                b3.place(x=110, y=210, height=80, width=80)
                BB3 = 'O'
                if AA3 == 'O' and CC3 == 'O':
                    winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    ocheck = 1
                    a3.config(bg="gold")
                    b3.config(bg="gold")
                    c3.config(bg="gold")
                elif BB1 == 'O' and BB2 == 'O':
                    winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    ocheck = 1
                    b1.config(bg="gold")
                    b2.config(bg="gold")
                    b3.config(bg="gold")
        elif symb == 7:
            if data == 1:
                c1 = tk.Button(root, text="X", font=('Arial', 40))
                c1.place(x=190, y=50, height=80, width=80)
                CC1 = 'X'
                if AA1 == 'X' and BB1 == 'X':
                    winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    xcheck = 1
                    a1.config(bg="gold")
                    b1.config(bg="gold")
                    c1.config(bg="gold")
                elif BB2 == 'X' and AA3 == 'X':
                    winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    xcheck = 1
                    a3.config(bg="gold")
                    b2.config(bg="gold")
                    c1.config(bg="gold")
                elif CC2 == 'X' and CC3 == 'X':
                    winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    xcheck = 1
                    c1.config(bg="gold")
                    c2.config(bg="gold")
                    c3.config(bg="gold")
            else:
                c1 = tk.Button(root, text="O", font=('Arial', 40))
                c1.place(x=190, y=50, height=80, width=80)
                CC1 = 'O'
                if AA1 == 'O' and BB1 == 'O':
                    winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    ocheck = 1
                    a1.config(bg="gold")
                    b1.config(bg="gold")
                    c1.config(bg="gold")
                elif BB2 == 'O' and AA3 == 'O':
                    winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    ocheck = 1
                    a3.config(bg="gold")
                    b2.config(bg="gold")
                    c1.config(bg="gold")
                elif CC2 == 'O' and CC3 == 'O':
                    winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    ocheck = 1
                    c1.config(bg="gold")
                    c2.config(bg="gold")
                    c3.config(bg="gold")
        elif symb == 8:
            if data == 1:
                c2 = tk.Button(root, text="X", font=('Arial', 40))
                c2.place(x=190, y=130, height=80, width=80)
                CC2 = 'X'
                if CC1 == 'X' and CC3 == 'X':
                    winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    xcheck = 1
                    c1.config(bg="gold")
                    c2.config(bg="gold")
                    c3.config(bg="gold")
                elif AA2 == 'X' and BB2 == 'X':
                    winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    xcheck = 1
                    a2.config(bg="gold")
                    b2.config(bg="gold")
                    c2.config(bg="gold")
            else:
                c2 = tk.Button(root, text="O", font=('Arial', 40))
                c2.place(x=190, y=130, height=80, width=80)
                CC2 = 'O'
                if CC1 == 'O' and CC3 == 'O':
                    winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    ocheck = 1
                    c1.config(bg="gold")
                    c2.config(bg="gold")
                    c3.config(bg="gold")
                elif AA2 == 'O' and BB2 == 'O':
                    winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    ocheck = 1
                    a2.config(bg="gold")
                    b2.config(bg="gold")
                    c2.config(bg="gold")
        elif symb == 9:
            if data == 1:
                c3 = tk.Button(root, text="X", font=('Arial', 40))
                c3.place(x=190, y=210, height=80, width=80)
                CC3 = 'X'
                if CC1 == 'X' and CC2 == 'X':
                    winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    xcheck = 1
                    c1.config(bg="gold")
                    c2.config(bg="gold")
                    c3.config(bg="gold")
                elif AA1 == 'X' and BB2 == 'X':
                    winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    xcheck = 1
                    a1.config(bg="gold")
                    b2.config(bg="gold")
                    c3.config(bg="gold")
                elif AA3 == 'X' and BB3 == 'X':
                    winner = tk.Label(root, text="Player X wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    xcheck = 1
                    a3.config(bg="gold")
                    b3.config(bg="gold")
                    c3.config(bg="gold")
            else:
                c3 = tk.Button(root, text="O", font=('Arial', 40))
                c3.place(x=190, y=210, height=80, width=80)
                CC3 = 'O'
                if CC1 == 'O' and CC2 == 'O':
                    winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    ocheck = 1
                    c1.config(bg="gold")
                    c2.config(bg="gold")
                    c3.config(bg="gold")
                elif AA1 == 'O' and BB2 == 'O':
                    winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    ocheck = 1
                    a1.config(bg="gold")
                    b2.config(bg="gold")
                    c3.config(bg="gold")
                elif AA3 == 'O' and BB3 == 'O':
                    winner = tk.Label(root, text="Player O wins", font=('Arial', 20))
                    winner.place(x=20, y=340)
                    ocheck = 1
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
    b2 = tk.Button(root, command=lambda: paint(5), text="")
    b2.place(x=110, y=130, height=80, width=80)
    b3 = tk.Button(root, command=lambda: paint(6), text="")
    b3.place(x=110, y=210, height=80, width=80)
    c1 = tk.Button(root, command=lambda: paint(7), text="")
    c1.place(x=190, y=50, height=80, width=80)
    c2 = tk.Button(root, command=lambda: paint(8), text="")
    c2.place(x=190, y=130, height=80, width=80)
    c3 = tk.Button(root, command=lambda: paint(9), text="")
    c3.place(x=190, y=210, height=80, width=80)


newgamebt = ttk.Button(root,command=newgame, text="Start Game") # button for new/start game
newgamebt.place(x=210,y=300, height=40, width=90)

def backgroundcolor(event):
    global selected_value
    selected_value = dropdown.get()
    if selected_value == "Gray":
        root.config(bg="slate gray")
    elif selected_value =="Cyan":
        root.config(bg="cyan")
    elif selected_value =="Blue":
        root.config(bg="skyblue3")
    elif selected_value =="Dark":
        root.config(bg="gray27")
    elif selected_value =="Pink":
        root.config(bg="lightpink1")
    elif selected_value =="Green":
        root.config(bg="palegreen1")
    elif selected_value =="Red":
        root.config(bg="firebrick1")
    elif selected_value =="default":
        root.config(bg="lightcyan2")

options = ["Gray", "Cyan", "Green", "Blue", "Dark","Pink", "Red", "default"]
# Create a StringVar to store the selected value
selected_option = tk.StringVar()
# Create the dropdown list
dropdown = ttk.Combobox(root, textvariable=selected_option, values=options)
dropdown.set("Select a Color")  # Set a default value
# Bind the event handler to the <<ComboboxSelected>> event
dropdown.bind("<<ComboboxSelected>>", backgroundcolor)
# Place the dropdown on the window
dropdown.place(x=200, y=340, height=30, width=100)
root.mainloop()