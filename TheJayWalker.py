import tkinter as tk
root = tk.Tk()
root.geometry('330x650')
root.title("The Jay Walker")
position = 3
def start():
    global position
    def trigger_button(event):
        if event.keysym == "a":  # Check if the pressed key is "a"
            leftbutton.invoke()
        if event.keysym == "d":  # Check if the pressed key is "d"
            rightbutton.invoke()
        if event.keysym == "w":  # Check if the pressed key is "w"
            topbutton.invoke()
        if event.keysym == "s":  # Check if the pressed key is "s"
            downbutton.invoke()
    tiles = []

    for i in range(1, 131):
        if i <= 10:
            row = 12  # Buttons 1 to 10 in row 12
        elif 11 <= i <= 20:
            row = 11
        elif 21 <= i <= 30:
            row = 10
        elif 31 <= i <= 40:
            row = 9
        elif 41 <= i <= 50:
            row = 8
        elif 51 <= i <= 60:
            row = 7
        elif 61 <= i <= 70:
            row = 6
        elif 71 <= i <= 80:
            row = 5
        elif 81 <= i <= 90:
            row = 4
        elif 91 <= i <= 100:
            row = 3
        elif 101 <= i <= 110:
            row = 2
        elif 111 <= i <= 120:
            row = 1
        else:
            row = 0

        tile = tk.Button(root,bg="gray", text=i, height=2, width=3)
        tile.grid(row=row, column=(i - 1) % 10)
        tiles.append(tile)
    t1, t2, t3, t4, t5, t6, t7, t8, t9, t10 = tiles[0], tiles[1], tiles[2], tiles[3], tiles[4], tiles[5], tiles[6], tiles[7], tiles[8], tiles[9]
    t11, t12, t13, t14, t15, t16, t17, t18, t19, t20 = tiles[10], tiles[11], tiles[12], tiles[13], tiles[14], tiles[15],tiles[16], tiles[17], tiles[18], tiles[19]
    for i, tile in enumerate(tiles):
        if i <= 9:
            tile.config(bg="green")
        if i > 37 and i <40:
            tile.config(bg="white") # color for road lane separator
        if i == 30:
            tile.config(bg="white")
        if i > 32 and i <36:
            tile.config(bg="white")
        if i > 59 and i <70:
            tile.config(bg="chocolate") # color for barrier
        if i > 92 and i <96:
            tile.config(bg="white")
        if i == 90:
            tile.config(bg="white")
        if i > 97 and i <100:
            tile.config(bg="white")

        if i >= 120:
            tile.config(bg="green")
    def left(): #function for moving left
        global position
        position = position - 1
        for i, tile in enumerate(tiles):
            if position == i + 1:
                tile.config(bg="red")
            elif i <= 9:        # This part will retain the color green/Grass
                tile.config(bg="green")
            elif i >= 120:
                tile.config(bg="green")

            else:
                tile.config(bg="gray")
        print(f'{position}')
    def right():
        global position
        position = position + 1
        for i, tile in enumerate(tiles):
            if position == i + 1:
                tile.config(bg="red")
            elif i <= 9:
                tile.config(bg="green")
                tile.config(bg="green")
            elif i >= 120:
                tile.config(bg="green")
            else:
                tile.config(bg="gray")
        print(f'{position}')
    def up():
        global position
        position = position + 10
        for i, tile in enumerate(tiles):
            if position == i + 1:
                tile.config(bg="red")
            elif i <= 9:
                tile.config(bg="green")
                tile.config(bg="green")
            elif i >= 120:
                tile.config(bg="green")
            else:
                tile.config(bg="gray")
        print(f'{position}')
    def down():
        global position
        position = position - 10
        for i, tile in enumerate(tiles):
            if position == i + 1:
                tile.config(bg="red")
            elif i <= 9:
                tile.config(bg="green")
            elif i >= 120:
                tile.config(bg="green")
            else:
                tile.config(bg="gray")
        print(f'{position}')

    print(f'{position}')





    leftbutton = tk.Button(root, command=left, text="Left")
    leftbutton.place(x=50, y=570, height=20, width=50)
    rightbutton = tk.Button(root,command=right, text="Right")
    rightbutton.place(x=150, y=570, height=20, width=50)
    topbutton = tk.Button(root, command=up,text="Top")
    topbutton.place(x=100, y=540, height=20, width=50)
    downbutton = tk.Button(root,command=down, text="Down")
    downbutton.place(x=100, y=600, height=20, width=50)
    root.bind("<a>", trigger_button)
    root.bind("<w>", trigger_button)
    root.bind("<s>", trigger_button)
    root.bind("<d>", trigger_button)



startbutton = tk.Button(root,command=start,text="Start")
startbutton.place(x=100,y=100,height=30,width=60)


root.mainloop()
