import tkinter as tk
from tkinter import messagebox
import random
from tkinter import Menu
import json
root = tk.Tk()
root.geometry('300x400')
root.title('Guess the Number')
root.configure(bg="pink")
rounds = 1
money = 100
menu_bar = Menu(root)
root.config(menu=menu_bar)
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Help", command=lambda: messagebox.showinfo("Help", "Prize = Balance - (rounds * 100).\n If your prize is negative, it means you owe me that amount; otherwise, I'll pay you"))
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Guessing Game by Richard B. Grefaldo \n Version Vortex 20240106.1\n337 lines of code"))
help_menu.add_separator()
help_menu.add_command(label="Changelog", command=lambda: messagebox.showinfo("Version Vortex 20240106.1", "\nVortex 20240106.1(Bug Fix)\nFixed bug: 'Hall of Blunder' data not resetting with the reset button\n-3 lines of code added\nVortex 20240106\n -Added Blunder's Hall\n -48 lines of coded added \nRosas 20231009\n -Added bgcolor,\n -dark and light modes\n -leaderboard\n -honorifics for VIPs\n -added admin access\n -minor text change and bug fixes\n -127 lines of code added\nSorbetes 20231004\n -Added some tricks\n -28 lines of code added\nMotmot 20230929\n -Added name and age registration\n -centered text in the display box\n -text and font adjustment\n -bug fixes"))

regbox = tk.Entry(root, font=('Arial', 18))
regbox.place(x=80, y=40, height=30, width=150)
regbox2 = tk.Entry(root, font=('Arial', 18))
regbox2.place(x=80, y=100, height=30, width=150)
reglabel = tk.Label(root, text='Name', font=('Arial', 10))
reglabel.place(x=80, y=10)
reglabel2 = tk.Label(root, text='Age', font=('Arial', 10))
reglabel2.place(x=80, y=70)
umaga = "white"
gabi = "black"
fcolor = "white"
bcolor = "pink"


def load_leaderboard_data():
    try:
        with open("leaderboard.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def load_lowerboard_data():
    try:
        with open("lowerboard.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def show_top_5_lowerboard():
    lowerboard_data = load_lowerboard_data()
    top_5_window = tk.Toplevel(root)
    top_5_window.title("Loser")
    top_5_label = tk.Label(top_5_window, text="Top 10 Loser:")
    top_5_label.pack()
    top_5_text = tk.Text(top_5_window, height=10, width=30)
    top_5_text.pack()

    # Display the top 10 leaderboard data in the text widget
    for idx, entry in enumerate(lowerboard_data[:10], start=1):
        top_5_text.insert(tk.END, f"{idx}. {entry['name']} - PHP {entry['score']} \n")
    top_5_text.config(state=tk.DISABLED)  # Make the text widget read-only

def show_top_5_leaderboard():
    leaderboard_data = load_leaderboard_data()
    top_5_window = tk.Toplevel(root)
    top_5_window.title("Leaderboard")
    top_5_label = tk.Label(top_5_window, text="Top 10 Winners:")
    top_5_label.pack()
    top_5_text = tk.Text(top_5_window, height=10, width=30)
    top_5_text.pack()

    # Display the top 10 leaderboard data in the text widget
    for idx, entry in enumerate(leaderboard_data[:10], start=1):
        top_5_text.insert(tk.END, f"{idx}. {entry['name']} - PHP {entry['score']} \n")
    top_5_text.config(state=tk.DISABLED)  # Make the text widget read-only


   # Page two of the UI
def secondframe():
    name1 = regbox.get().strip()  # strip will remove leading or trailing white spaces
    age = regbox2.get().strip()
    if name1 == "Jhoebelyn":
        namelabel = tk.Label(root, bg="pink", text=f'Welcome Beybee {name1}', font=('Arial', 12))
        namelabel.place(x=60, y=5)

    elif name1 == "Richard" and float(age) == 52918:
        namelabel = tk.Label(root, bg="pink", text=f'Welcome Boss {name1}', font=('Arial', 12))
        namelabel.place(x=60, y=5)
    else:
        namelabel = tk.Label(root, bg="pink", text=f'Welcome {name1}', font=('Arial', 12))
        namelabel.place(x=60, y=5)

    def claim_prize():
        cash_out()
        money1 = moneybox.get("1.0", "2.0")
        money1 = int(money1) - (rounds * 100)
        if money1 >= 25:  # This condition will determine whether the score belongs in the Hall of Fame or the Hall of Blunder
            add_to_leaderboard()
        else:
            add_to_lowerboard()

    if age == "":
        messagebox.showinfo('Warning', 'Invalid Age Value')
        root.destroy()
    if 1 <= float(age) < 18:
        messagebox.showinfo('Warning', 'You must be a legal age to register')
        root.destroy()
    if 100 <= float(age) <= 1000:
        messagebox.showinfo('O_O', 'Enrile is that U?')

    name2 = "Jhoebelyn"
    name3 = name2
    if name1 == name3:
        messagebox.showinfo('Psst', 'Happy 5 years and 4 months !!!\nI Love You Beybee')
    reglabel2.destroy()
    fbtn.destroy()
    regbox.place_forget()
    regbox2.place_forget()
    reglabel.destroy()

    # Generate random numbers
    def bet():
        lucky = random.randint(1, 30)
        global money, rounds, umaga, gabi
        box4.replace("1.0", "3.0", str(lucky))
        money = money - 25
        moneybox.replace("1.0", "3.0", str(money))
        moneybox.delete("4.0", tk.END)
        num1 = box1.get("1.0", "2.0")
        num2 = box2.get("1.0", "2.0")
        num3 = box3.get("1.0", "2.0")
        lucky = box4.get("1.0", "2.0")

        if num1 == lucky:
            messagebox.showinfo('Popup', f'You won 200PHP')
            money = money + 200
            moneybox.replace("1.0", "3.0", str(money))
        elif num2 == lucky:
            messagebox.showinfo('Popup', f'You won 200PHP')
            money = money + 200
            moneybox.replace("1.0", "3.0", str(money))
        elif num3 == lucky:
            messagebox.showinfo('Popup', f'You won 200PHP')
            money = money + 200
            moneybox.replace("1.0", "3.0", str(money))
        else:
            messagebox.showinfo('Popup', f'You lose')

        if money <= 0:
            messagebox.showinfo('Popup', 'WALA KA NG PERA')
            answer = messagebox.askquestion('Message', 'do you want to play again?')
            if answer == "yes":
                money = money + 100
                rounds = rounds + 1
                moneybox.replace("1.0", "3.0", str(money))
                print(rounds)
                round1box.replace("1.0", "3.0", str(rounds))

            else:
                root.destroy()

    def cash_out():
        money1 = moneybox.get("1.0", "2.0")
        money1 = int(money1) - (rounds * 100)
        messagebox.showinfo('Popup', f'Total Prize is :₱{money1}')

    def save_leaderboard_data(data):
        with open("leaderboard.json", "w") as file:
            json.dump(data, file)
    def save_lowerboard_data(data):
        with open("lowerboard.json", "w") as file:
            json.dump(data, file)

    def add_to_leaderboard():
        name = regbox.get()
        money1 = moneybox.get("1.0", "2.0")
        money1 = int(money1) - (rounds * 100)
        score = money1
        leaderboard_data = load_leaderboard_data()
        leaderboard_data.append({"name": name, "score": score})  # Add the new entry to the leaderboard
        leaderboard_data.sort(key=lambda x: x["score"], reverse=True)   # Sort
        leaderboard_data = leaderboard_data[:10]  # only top 10 will be registered
        save_leaderboard_data(leaderboard_data)

        # Clear the input fields
        regbox.delete(0, tk.END)
        regbox2.delete(0, tk.END)

    def add_to_lowerboard():
        name = regbox.get()
        money1 = moneybox.get("1.0", "2.0")
        money1 = int(money1) - (rounds * 100)
        score = money1
        lowerboard_data = load_lowerboard_data()
        lowerboard_data.append({"name": name, "score": score})  # Add the new entry to the leaderboard
        lowerboard_data.sort(key=lambda x: x["score"], reverse=True)   # Sort
        lowerboard_data = lowerboard_data[:10]  # only top 10 lowest core will be registered
        save_lowerboard_data(lowerboard_data)

        # Clear the input fields
        regbox.delete(0, tk.END)
        regbox2.delete(0, tk.END)

    def resethall():  # It will clear the leaderboard  data
        leaderboard_data = load_leaderboard_data()
        leaderboard_data = leaderboard_data[:0]
        save_leaderboard_data(leaderboard_data)
        lowerboard_data = load_lowerboard_data()
        lowerboard_data = lowerboard_data[:0]
        save_lowerboard_data(lowerboard_data)
        messagebox.showinfo('Warning', 'Leaderboard successfully cleared')

    if float(age) == 52918 and name1 == "Richard":
        messagebox.showinfo('Welcome Admin', 'Admin Access Granted')
        resbtn = tk.Button(root, text='Clear', command=resethall, font=('Arial', 7))
        resbtn.place(x=250, y=165, height=40, width=40)

    box1 = tk.Text(root, font=('Arial', 18))
    box1.place(x=20, y=170, height=30, width=90)
    box2 = tk.Text(root, font=('Arial', 18))
    box2.place(x=20, y=230, height=30, width=90)
    box3 = tk.Text(root, font=('Arial', 18))
    box3.place(x=20, y=290, height=30, width=90)
    box4 = tk.Text(root, wrap=tk.WORD, font=('Arial', 30))
    box4.place(x=70, y=60, height=70, width=160)
    btn1 = tk.Button(root, command=bet, text='Guess', font=('Arial', 10))
    btn1.place(x=50, y=330, height=30, width=80)
    btn2 = tk.Button(root, command=claim_prize, text='Claim Prize', font=('Arial', 10))
    btn2.place(x=160, y=330, height=30, width=80)
    moneylabel = tk.Label(root, bg="pink", text='Balance', font=('Arial', 12))
    moneylabel.place(x=180, y=200)
    moneybox = tk.Text(root, wrap=tk.WORD, state=tk.NORMAL, font=('Arial', 18))
    moneybox.insert("1.0", str(money))
    moneybox.place(x=180, y=230, height=30, width=100)
    rlabel = tk.Label(root, bg="pink", text='Rounds', font=('Arial', 12))
    rlabel.place(x=180, y=140)
    round1box = tk.Text(root, font=('Arial', 18))
    round1box.place(x=180, y=170, height=30, width=40)
    label1 = tk.Label(root, bg="pink", text='Guess the Number 1 to 30', font=('Arial', 15))
    label1.place(x=35, y=25)
    label2 = tk.Label(root, bg="pink", text='₱', font=('Arial', 15))
    label2.place(x=150, y=230)
    label3 = tk.Label(root, bg="pink", text='Stake ₱25 with a chance to earn ₱200', font=('Arial', 10))
    label3.place(x=10, y=370)
    label4 = tk.Label(root, bg="pink", text='Enter your number below', font=('Arial', 10))
    label4.place(x=20, y=140)

    def toggle():
        if toggle_var.get() == 1:
            toggle_label.config(text="Dark Mode")
            fcolor1 = "white"
            bcolor = "black"
            label1.config(fg=fcolor1, bg=bcolor)
            label2.config(fg=fcolor1, bg=bcolor)
            label3.config(fg=fcolor1, bg=bcolor)
            label4.config(fg=fcolor1, bg=bcolor)
            rlabel.config(fg=fcolor1, bg=bcolor)
            toggle_label.config(fg=fcolor1, bg=bcolor)
            btn1.config(bg="pink")
            btn2.config(bg="pink")
            moneylabel.config(fg=fcolor1, bg=bcolor)
            namelabel.config(fg=fcolor1, bg=bcolor)
            root.configure(bg=gabi)
        else:
            fcolor1 = "black"
            bcolor = "pink"
            toggle_label.config(text="Light Mode")
            label1.config(fg=fcolor1, bg=bcolor)
            label2.config(fg=fcolor1, bg=bcolor)
            label3.config(fg=fcolor1, bg=bcolor)
            label4.config(fg=fcolor1, bg=bcolor)
            rlabel.config(fg=fcolor1, bg=bcolor)
            toggle_label.config(fg=fcolor1, bg=bcolor)
            btn1.config(bg="white")
            btn2.config(bg="white")
            namelabel.config(fg=fcolor1, bg=bcolor)
            moneylabel.config(fg=fcolor1, bg=bcolor)

            root.configure(bg=bcolor)

    toggle_var = tk.IntVar()
    toggle_button = tk.Checkbutton(root, variable=toggle_var, command=toggle)
    toggle_button.place(x=160, y=300)
    toggle_label = tk.Label(root, text="Dark/Light Mode", bg="pink")
    toggle_label.place(x=160, y=280)


max_move_distance = 50


def move_button(event):  # button will move if the age value is less than 18
    age_text = regbox2.get()
    try:
        age2 = int(age_text)
        if age2 < 18:
            new_x = event.x_root - root.winfo_rootx() - fbtn_width // 2 + random.randint(-max_move_distance,
                                                                                         max_move_distance)
            new_y = event.y_root - root.winfo_rooty() - fbtn_height // 2 + random.randint(-max_move_distance,
                                                                                          max_move_distance)
            fbtn.place(x=new_x, y=new_y)
            fbtn.configure(text="Adults only", font=('Arial', 12))
        else:
            fbtn.place(x=100, y=250)
            fbtn.configure(text="Register", font=('Arial', 10))
    except ValueError:# Handle the case where age_text is not a valid integer
        pass


fbtn_width = 100
fbtn_height = 30


def on_hover(event):
    # Move the button when hovered
    move_button(event)


def on_leave(event):
    # Move the button back when leaving
    move_button(event)


# Bind the <FocusOut> event to the move_button function
regbox2.bind('<FocusOut>', move_button)
# Bind the <Enter> and <Leave> events for the button
fbtn = tk.Button(root, command=secondframe, text='Register', font=('Arial', 10))
fbtn.place(x=100, y=250, width=fbtn_width, height=fbtn_height)
fbtn.bind('<Enter>', on_hover)
fbtn.bind('<Leave>', on_leave)
menu_bar2 = Menu(root)
help_menu2 = Menu(menu_bar2, tearoff=0)
menu_bar.add_cascade(label="Leaderboard", menu=help_menu2)
help_menu2.add_command(label="Hall of Fame", command=show_top_5_leaderboard)
help_menu2.add_command(label="Blunder's Hall", command=show_top_5_lowerboard)
root.mainloop()
