import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox
root = tk.Tk()
root.geometry('330x650')
root.title("The Jay Walker")
about = Menu(root)
root.config(menu=about)
help_menu = Menu(about,tearoff = 0)
about.add_cascade(label="Info",menu=help_menu)
help_menu.add_command(label="Controls", command=lambda: messagebox.showinfo("Controls","For PC:\n Press W to Move up\n  S to Move down\n  A to Move left \n  D to Move right \n  Space to Jump\n\nFor Mobile:\n Use the on screen buttons"))
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About","The Jaywalker by Richard Grefaldo\nVersion 20240129\n\n Dash across busy streets to meet someone \non the other side. Avoid speeding cars\nand obstacles. Reach the opposite sidewalk\n to advance.Can you navigate the urban \njungle safely?"))
help_menu.add_command(label="Changelog", command=lambda: messagebox.showinfo("Changelog","Version 20240129\n -Added Car,Npc Collision\n -Added Win or Lose Condition\nVersion 20240128\n -Added Moving Cars\n -Added Name Registration\nVersion 20240127\n -Added Collision\n -Added Road Median Strip\n  players now need to jump over \n  the added road median strip \n  in order to cross \nVersion 20240126\n - Initial Release UI only"))
position,car1pos,car2pos,car3pos,car4pos,car5pos = 5,11,23,27,41,55
car6pos,car7pos,car8pos,car9pos,car10pos = 78,85,113,118,110
npcpos = 120


def Start():
    global position,playername,npc,car1pos
    playername = namefield.get().strip()
    npc = npcfield.get().strip()
    if playername == "":
        npc = "Bb"
        playername = "Jhoe"


    def trigger_button(event):
        if event.keysym == "a":  # Check if the pressed key is "a"
            leftbutton.invoke()
        if event.keysym == "d":  # Check if the pressed key is "d"
            rightbutton.invoke()
        if event.keysym == "w":  # Check if the pressed key is "w"
            topbutton.invoke()
        if event.keysym == "s":  # Check if the pressed key is "s"
            downbutton.invoke()
        if event.keysym == "space":  # Check if the pressed key is "space"
            jumpbutton.invoke()

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

        tile = tk.Button(root,bg="gray",text=i, height=1, width=1)
        tile.grid(row=row, column=(i - 1) % 10)
        tiles.append(tile)

    t1, t2, t3, t4, t5, t6, t7, t8, t9, t10 = tiles[0], tiles[1], tiles[2], tiles[3], tiles[4], tiles[5], tiles[6], tiles[7], tiles[8], tiles[9]
    t11, t12, t13, t14, t15, t16, t17, t18, t19, t20 = tiles[10], tiles[11], tiles[12], tiles[13], tiles[14], tiles[15],tiles[16], tiles[17], tiles[18], tiles[19]
    collision = {61:51,62:52,63:53,64:54,65:55,66:56,67:57,68:58,69:59,70:60,131:121,132:122,133:123,134:124,135:125,136:126,137:127,138:128,139:129,140:130} # Handles data for barriers
    Rcollision = {131:130,121:120,111:110,101:100,91:90,81:80,61:60,51:50,41:40,31:30,21:20,11:10}
    Lcollision = {0:1,10:11,20:21,30:31,40:41,50:51,60:61,70:71,80:81,90:91,100:101,110:111,120:121}
    Dcollision = {61:71,62:72,63:73,64:74,65:75,66:76,67:77,68:78,69:79,70:80}
    carloop = {21:11,31:21,51:41,61:51,70:80,80:90,100:110,110:120}


    ###MOVING CARS#####
    def car1():
        global car1pos,car2pos,car3pos,position,npcpos
        if position == car1pos or position == car2pos or position == car3pos:
            messagebox.showinfo('Message', 'Game Over')
            answer = messagebox.askquestion('Message', 'do you want to play again?')
            if answer == "yes":
                position = 5
                npcpos = 121
            else:
                root.quit()

        car1pos = car1pos + 1
        car2pos,car3pos = car2pos + 1,car3pos + 1
        root.after(800, car1)
        if car1pos in carloop:
            car1pos = carloop[car1pos]
        if car2pos in carloop:
            car2pos = carloop[car2pos]
        if car3pos in carloop:
            car3pos = carloop[car3pos]
        for i, tile in enumerate(tiles):
            if car1pos == i + 1 or car2pos == i + 1 or car3pos == i + 1:
                tile.config(bg="blue",text=f"Car")
            elif i == position - 1: # this blocks fixed flickering player's color and name  every time cars move
                tile.config(bg="red", text=f"{playername}")
            elif car4pos == i + 1 or car5pos == i + 1 or car6pos == i + 1 or car7pos == i + 1 or car8pos == i + 1 or car9pos == i + 1 or car10pos == i + 1:
                tile.config(bg="blue", text=f"Car")
            elif npcpos == i + 1:
                tile.config(bg="yellow", text=f"{npc}")
            elif i <= 9:
                tile.config(bg="green", text="")
            elif i == 30:
                tile.config(bg="white", text="")
            elif i > 32 and i < 36:
                tile.config(bg="white", text="")
            elif i > 37 and i < 40:
                tile.config(bg="white", text="")
            elif i > 59 and i < 70:
                tile.config(bg="chocolate")
            elif i == 90:
                tile.config(bg="white", text="")
            elif i > 92 and i < 96:
                tile.config(bg="white", text="")
            elif i > 97 and i < 100:
                tile.config(bg="white", text="")
            elif i >= 120:
                tile.config(bg="green", text="")

            else:
                tile.config(bg="gray", text="")
    def car2():
        global car4pos,car5pos,position,npcpos
        if position == car4pos or position == car5pos:
            messagebox.showinfo('Message', 'Game Over')
            answer = messagebox.askquestion('Message', 'do you want to play again?')
            if answer == "yes":
                position = 5
                npcpos = 121
            else:
                root.quit()
        car4pos,car5pos = car4pos + 1,car5pos + 1
        root.after(150, car2)
        if car4pos in carloop:
            car4pos = carloop[car4pos]
        if car5pos in carloop:
            car5pos = carloop[car5pos]
        for i, tile in enumerate(tiles):
            if car4pos == i + 1 or car5pos == i + 1:
                tile.config(bg="blue",text=f"Car")
            elif i == position - 1: # this blocks fixed flickering player's color and name  every time cars move
                tile.config(bg="red", text=f"{playername}")
            elif car1pos == i + 1 or car2pos == i + 1 or car3pos == i + 1 or car6pos == i + 1 or car7pos == i + 1 or car8pos == i + 1 or car9pos == i + 1 or car10pos == i + 1:
                tile.config(bg="blue",text=f"Car")
            elif npcpos == i + 1:
                tile.config(bg="yellow", text=f"{npc}")
            elif i <= 9:
                tile.config(bg="green", text="")
            elif i == 30:
                tile.config(bg="white", text="")
            elif i > 32 and i < 36:
                tile.config(bg="white", text="")
            elif i > 37 and i < 40:
                tile.config(bg="white", text="")
            elif i > 59 and i < 70:
                tile.config(bg="chocolate")
            elif i == 90:
                tile.config(bg="white", text="")
            elif i > 92 and i < 96:
                tile.config(bg="white", text="")
            elif i > 97 and i < 100:
                tile.config(bg="white", text="")
            elif i >= 120:
                tile.config(bg="green", text="")

            else:
                tile.config(bg="gray", text="")
    def car3():
        global car6pos,car7pos,position,npcpos
        if position == car6pos or position == car7pos:
            messagebox.showinfo('Message', 'Game Over')
            answer = messagebox.askquestion('Message', 'do you want to play again?')
            if answer == "yes":
                position = 5
                npcpos = 121
            else:
                root.quit()
        car6pos,car7pos = car6pos - 1 ,car7pos - 1
        root.after(100, car3)
        if car6pos in carloop:
            car6pos = carloop[car6pos]
        if car7pos in carloop:
            car7pos = carloop[car7pos]
        for i, tile in enumerate(tiles):
            if car6pos == i + 1 or car7pos == i + 1:
                tile.config(bg="blue",text=f"Car")
            elif i == position - 1: # this blocks fixed flickering player's color and name  every time cars move
                tile.config(bg="red", text=f"{playername}")
            elif car1pos == i + 1 or car2pos == i + 1 or car3pos == i + 1 or car4pos == i + 1 or car5pos == i + 1 or car8pos == i + 1 or car9pos == i + 1 or car10pos == i + 1:
                tile.config(bg="blue",text=f"Car")
            elif npcpos == i + 1:
                tile.config(bg="yellow", text=f"{npc}")
            elif i <= 9:
                tile.config(bg="green", text="")
            elif i == 30:
                tile.config(bg="white", text="")
            elif i > 32 and i < 36:
                tile.config(bg="white", text="")
            elif i > 37 and i < 40:
                tile.config(bg="white", text="")
            elif i > 59 and i < 70:
                tile.config(bg="chocolate")
            elif i == 90:
                tile.config(bg="white", text="")
            elif i > 92 and i < 96:
                tile.config(bg="white", text="")
            elif i > 97 and i < 100:
                tile.config(bg="white", text="")
            elif i >= 120:
                tile.config(bg="green", text="")

            else:
                tile.config(bg="gray", text="")
    def car4():
        global car8pos,car9pos,car10pos,position,npcpos
        if position == car8pos or position == car9pos or position == car10pos:
            messagebox.showinfo('Message', 'Game Over')
            answer = messagebox.askquestion('Message', 'Do you want to play again?')
            if answer == "yes":
                position = 5
                npcpos = 121
            else:
                root.quit()
        car8pos,car9pos,car10pos = car8pos - 1 ,car9pos - 1, car10pos - 1
        root.after(400, car4)
        if car8pos in carloop:
            car8pos = carloop[car8pos]
        if car9pos in carloop:
            car9pos = carloop[car9pos]
        if car10pos in carloop:
            car10pos = carloop[car10pos]
        for i, tile in enumerate(tiles):
            if car8pos == i + 1 or car9pos == i + 1 or car10pos == i + 1:
                tile.config(bg="blue",text=f"Car")
            elif i == position - 1: # this blocks fixed flickering player's color and name  every time cars move
                tile.config(bg="red", text=f"{playername}")
            elif car1pos == i + 1 or car2pos == i + 1 or car3pos == i + 1 or car4pos == i + 1 or car5pos == i + 1 or car6pos == i + 1 or car7pos == i + 1:
                tile.config(bg="blue",text=f"Car")
            elif npcpos == i + 1:
                tile.config(bg="yellow", text=f"{npc}")
            elif i <= 9:
                tile.config(bg="green", text="")
            elif i == 30:
                tile.config(bg="white", text="")
            elif i > 32 and i < 36:
                tile.config(bg="white", text="")
            elif i > 37 and i < 40:
                tile.config(bg="white", text="")
            elif i > 59 and i < 70:
                tile.config(bg="chocolate")
            elif i == 90:
                tile.config(bg="white", text="")
            elif i > 92 and i < 96:
                tile.config(bg="white", text="")
            elif i > 97 and i < 100:
                tile.config(bg="white", text="")
            elif i >= 120:
                tile.config(bg="green", text="")

            else:
                tile.config(bg="gray", text="")
    def npc1():
        global npcpos,position
        if position == npcpos:
            messagebox.showinfo('Richard', 'Bat ka nagjaywalk ha?!!\nAlam mo ba na delikado yun?!!\n........\n......\n anyway')
            answer = messagebox.askquestion('Richard', 'Happy Motmot \nMiss mo na ba ako?')
            if answer == "yes":
                answer = messagebox.showinfo('Richard', 'Miss din kita\n Mwaa lab u')
                position = 5
                npcpos = 121
            else:
                root.quit()
        npcpos = npcpos + 1
        root.after(1200, npc1)
        if npcpos in carloop:
            npcpos = carloop[npcpos]

        for i, tile in enumerate(tiles):
            if npcpos == i + 1 :
                tile.config(bg="yellow",text=f"{npc}")
            elif i == position - 1: # this blocks fixed flickering player's color and name  every time cars move
                tile.config(bg="red", text=f"{playername}")
            elif car1pos == i + 1 or car2pos == i + 1 or car3pos == i + 1 or car4pos == i + 1 or car5pos == i + 1 or car6pos == i + 1 or car7pos == i + 1 or car8pos == i + 1 or car9pos == i + 1 or car10pos == i + 1:
                tile.config(bg="blue",text=f"Car")
            elif i <= 9:
                tile.config(bg="green", text="")
            elif i == 30:
                tile.config(bg="white", text="")
            elif i > 32 and i < 36:
                tile.config(bg="white", text="")
            elif i > 37 and i < 40:
                tile.config(bg="white", text="")
            elif i > 59 and i < 70:
                tile.config(bg="chocolate")
            elif i == 90:
                tile.config(bg="white", text="")
            elif i > 92 and i < 96:
                tile.config(bg="white", text="")
            elif i > 97 and i < 100:
                tile.config(bg="white", text="")
            elif i >= 120:
                tile.config(bg="green", text="")

            else:
                tile.config(bg="gray", text="")



    car1()
    car2()
    car3()
    car4()
    npc1()




    for i, tile in enumerate(tiles):
        if i <= 9:
            tile.config(bg="green")
        if i == 30:
            tile.config(bg="white")
        if i > 32 and i <36:
            tile.config(bg="white")
        if i > 37 and i <40:
            tile.config(bg="white") # color for road lane separator
        if i > 59 and i <70:
            tile.config(bg="chocolate") # color for road barrier
        if i == 90:
            tile.config(bg="white")
        if i > 92 and i <96:
            tile.config(bg="white")
        if i > 97 and i <100:
            tile.config(bg="white")
        if i >= 120:
            tile.config(bg="green",text=i)

    def left(): #function for moving left
        global position
        position = position - 1
        for i, tile in enumerate(tiles):
            if position in Lcollision:
                position = Lcollision[position]
            if position == i + 1:
                tile.config(bg="red",text=f"{playername}")
            # fix for flickering cars everytime player moves left
            elif i == car1pos-1 or i == car2pos-1 or i == car3pos -1 or i == car4pos-1 or i == car5pos -1 or car6pos == i + 1 or car7pos == i + 1 or car8pos == i + 1 or car9pos == i + 1 or car10pos == i + 1:
                tile.config(bg="blue", text="Car")
            elif i == npcpos - 1:
                tile.config(bg="yellow", text=f"{npc}")
            elif i <= 9:        # This part will retain the color green/Grass
                tile.config(bg="green",text="")
            elif i == 30:
                tile.config(bg="white",text="")
            elif i > 32 and i < 36:
                tile.config(bg="white",text="")
            elif i > 37 and i < 40:
                tile.config(bg="white",text="")  # color for road lane separator
            elif i > 59 and i < 70:
                tile.config(bg="chocolate")
            elif i == 90:
                tile.config(bg="white",text="")
            elif i > 92 and i < 96:
                tile.config(bg="white",text="")
            elif i > 97 and i < 100:
                tile.config(bg="white",text="")
            elif i >= 120:
                tile.config(bg="green",text="")

            else:
                tile.config(bg="gray",text="")

    def right():
        global position
        position = position + 1
        for i, tile in enumerate(tiles):
            if position in Rcollision:
                position = Rcollision[position]  # creates invisible barrier on the right sides
            if position == i + 1:
                tile.config(bg="red",text=f"{playername}")
            elif i == car1pos - 1 or i == car2pos - 1 or i == car3pos - 1 or i == car4pos - 1 or i == car5pos - 1 or car6pos == i + 1 or car7pos == i + 1 or car8pos == i + 1 or car9pos == i + 1 or car10pos == i + 1:
                tile.config(bg="blue", text="Car")
            elif i == npcpos - 1:
                tile.config(bg="yellow", text=f"{npc}")
            elif i <= 9:
                tile.config(bg="green",text="")
            elif i == 30:
                tile.config(bg="white",text="")
            elif i > 32 and i < 36:
                tile.config(bg="white",text="")
            elif i > 37 and i < 40:
                tile.config(bg="white",text="")
            elif i > 59 and i < 70:
                tile.config(bg="chocolate")
            elif i == 90:
                tile.config(bg="white",text="")
            elif i > 92 and i < 96:
                tile.config(bg="white",text="")
            elif i > 97 and i < 100:
                tile.config(bg="white",text="")
            elif i >= 120:
                tile.config(bg="green",text="")
            else:
                tile.config(bg="gray",text="")
            # if position > 60 and position < 71: # Old method
            # position = position - 1
    def up():
        global position
        position = position + 10
        for i, tile in enumerate(tiles):
            if position == i + 1:
                tile.config(bg="red",text=f"{playername}")
            elif i == car1pos-1 or i == car2pos-1 or i == car3pos-1 or i == car4pos-1 or i == car5pos-1 or car6pos == i + 1 or car7pos == i + 1 or car8pos == i + 1 or car9pos == i + 1 or car10pos == i + 1:
                tile.config(bg="blue", text="Car")
            elif i == npcpos - 1:
                tile.config(bg="yellow", text=f"{npc}")
            elif i <= 9:
                tile.config(bg="green",text="")
            elif i == 30:
                tile.config(bg="white",text="")
            elif i > 32 and i < 36:
                tile.config(bg="white",text="")
            elif i > 37 and i < 40:
                tile.config(bg="white",text="")
            elif i > 59 and i < 70:
                tile.config(bg="chocolate")
            elif i == 90:
                tile.config(bg="white",text="")
            elif i > 92 and i < 96:
                tile.config(bg="white",text="")
            elif i > 97 and i < 100:
                tile.config(bg="white",text="")
            elif i >= 120:
                tile.config(bg="green",text="")
            else:
                tile.config(bg="gray",text="")
            if position in collision: # creates barrier  (new method)
                position = collision[position]
           # if position > 60 and position < 71:# old method
               # position = position - 10

    def down():
        global position
        position = position - 10
        for i, tile in enumerate(tiles):
            if position < 1 :  # This will block the player from moving downwards off the game screen
                position = position + 10
            if position == i + 1:
                tile.config(bg="red",text=f"{playername}")
            elif i == car1pos - 1 or i == car2pos - 1 or i == car3pos - 1 or i == car4pos - 1 or i == car5pos - 1 or car6pos == i + 1 or car7pos == i + 1 or car8pos == i + 1 or car9pos == i + 1 or car10pos == i + 1:
                tile.config(bg="blue", text="Car")
            elif i == npcpos - 1:
                tile.config(bg="yellow", text=f"{npc}")
            elif i <= 9:
                tile.config(bg="green",text="")
            elif i == 30:
                tile.config(bg="white",text="")
            elif i > 32 and i < 36:
                tile.config(bg="white",text="")
            elif i > 37 and i < 40:
                tile.config(bg="white",text="")
            elif i > 59 and i < 70:
                tile.config(bg="chocolate")
            elif i == 90:
                tile.config(bg="white",text="")
            elif i > 92 and i < 96:
                tile.config(bg="white",text="")
            elif i > 97 and i < 100:
                tile.config(bg="white",text="")
            elif i >= 120:
                tile.config(bg="green",text="")
            else:
                tile.config(bg="gray",text="")
            if position in Dcollision:
                position = Dcollision[position]
    def jump():
        global position
        if position < 51 or position > 70:
            position = position
        else:
            position = position + 20

        for i, tile in enumerate(tiles):

            if position == i + 1:
                tile.config(bg="red",text=f"{playername}")
            elif i == car1pos - 1 or i == car2pos - 1 or i == car3pos - 1 or i == car4pos - 1 or i == car5pos - 1 or car6pos == i + 1 or car7pos == i + 1 or car8pos == i + 1 or car9pos == i + 1 or car10pos == i + 1:
                tile.config(bg="blue", text="Car")
            elif i == npcpos - 1:
                tile.config(bg="yellow", text=f"{npc}")
            elif i <= 9:
                tile.config(bg="green",text="")
            elif i == 30:
                tile.config(bg="white",text="")
            elif i > 32 and i < 36:
                tile.config(bg="white",text="")
            elif i > 37 and i < 40:
                tile.config(bg="white",text="")
            elif i > 59 and i < 70:
                tile.config(bg="chocolate",text="")
            elif i == 90:
                tile.config(bg="white",text="")
            elif i > 92 and i < 96:
                tile.config(bg="white",text="")
            elif i > 97 and i < 100:
                tile.config(bg="white",text="")
            elif i >= 120:
                tile.config(bg="green",text="")
            else:
                tile.config(bg="gray",text="")




    leftbutton = tk.Button(root, command=left, text="Left")
    leftbutton.place(x=100, y=1570, height=150, width=250)
    rightbutton = tk.Button(root,command=right, text="Right")
    rightbutton.place(x=600, y=1570, height=150, width=250)
    topbutton = tk.Button(root, command=up,text="Up")
    topbutton.place(x=350, y=1340, height=150, width=250)
    downbutton = tk.Button(root,command=down, text="Down")
    downbutton.place(x=350, y=1800, height=150, width=250)
    jumpbutton = tk.Button(root,command=jump,text="Jump")
    jumpbutton.place(x=700,y=1800,height=150,width=150)
    root.bind("<a>", trigger_button)
    root.bind("<w>", trigger_button)
    root.bind("<s>", trigger_button)
    root.bind("<d>", trigger_button)
    root.bind("<space>", trigger_button)
    npcfield.destroy()
    namefield.destroy()

style = ttk.Style()
style.configure('Custom.TButton', font=('Arial', 15))
titlelabel = tk.Label(root,text="The Jaywalker",font=('Arial',20))
titlelabel.place(x=200,y=100)
titlelabel2 = tk.Label(root,text="by Richard",font=('Arial',14))
titlelabel2.place(x=350,y=250)
namelabel = tk.Label(root,text="Enter your name:",font=('Arial',10))
namelabel.place(x=290,y=530)
namefield = ttk.Entry(root,font=('Arial',15))
namefield.place(x=300, y =600,height=120,width=350)
npclabel = tk.Label(root,text="Enter npc's name:",font=('Arial',10))
npclabel.place(x=290,y=730)
npcfield = ttk.Entry(root,font=('Arial',15))
npcfield.place(x=300, y =800,height=120,width=450)
startbutton = ttk.Button(root,command=Start,text="Play",style='Custom.TButton')
startbutton.place(x=350,y=1000,height=120,width=350)



root.mainloop()
