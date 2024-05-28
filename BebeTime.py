import tkinter as tk
from tkinter import messagebox
from tkinter import Menu
root = tk.Tk()
root.geometry('300x480')
root.title('BebeTime')
about = Menu(root)
root.config(menu=about)
help_menu = Menu(about,tearoff = 0)
about.add_cascade(label="Info",menu=help_menu)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About","BebeTime by Richard Grefaldo\nVersion 20240528"))
help_menu.add_command(label="Changelog", command=lambda: messagebox.showinfo("Changelog","Version 20240528"))


wcounter = 1
rcounter = 1
setcounter = 1
prepcounter = 6
working = 1
setcounter2 = 0
cdcounter = 1
execounter = 1


def exep():
    global execounter,execount
    execounter = execounter + 1
    execount.config(text=execounter)
def exem():
    global execounter,execount
    if execounter <= 1:
        execounter = execounter
    else:
        execounter = execounter - 1
    execount.config(text=execounter)

def setp():
    global setcounter,setcount
    setcounter = setcounter + 1
    setcount.config(text=setcounter)

def setm():
    global setcounter,setcount
    if setcounter <= 1:
        setcounter = setcounter
    else:
        setcounter = setcounter - 1
    setcount.config(text=setcounter)

def workp():
    global wcounter,workcount
    wcounter = wcounter + 1
    workcount.config(text=wcounter)

def workm():
    global wcounter,workcount

    if wcounter <= 1:
        wcounter = wcounter
    else:
        wcounter = wcounter - 1
    workcount.config(text=wcounter)
def restm():
    global rcounter,restcount

    if rcounter <= 1:
        rcounter = rcounter
    else:
        rcounter = rcounter - 1
    restcount.config(text=rcounter)
def restp():
    global rcounter,restcount
    rcounter = rcounter + 1
    restcount.config(text=rcounter)
def cdp():
    global cdcounter,cdcount
    cdcounter = cdcounter + 1
    cdcount.config(text=cdcounter)
def cdm():
    global cdcounter,cdcount
    if cdcounter <= 1:
        cdcounter = cdcounter
    else:
        cdcounter = cdcounter - 1
    cdcount.config(text=cdcounter)



def start():
    global setcount,workcount,restcount,running
    running = True
    prepcount = tk.Label(root, text=prepcounter,font=('Arial', 75))
    prepcount.place(x=120, y=80)

    def resume():
        global running
        running = True
        if running:
            pbutton.config(text='Pause',command=pause)
        print(running)
        countdown()
    def pause():
        global running
        running = False
        print(running)
        if not running:
            pbutton.config(text='Resume',command=resume)
        countdown()



    def countdown():
        global prepcounter,wcounter,setcounter,working,rcounter
        setcountlabel = tk.Label(root,text='SET',font=('Arial',30))
        setcountlabel.place(x=90, y=20)
        setcountlabel2 = tk.Label(root, text=setcounter,font=('Arial', 30))
        setcountlabel2.place(x=180, y=20)
        if running and prepcounter >= 1 and setcounter >= 1:
            prepcounter = prepcounter - 1
            root.after(1000, countdown)
            print(prepcounter)
            prepcount.config(text=prepcounter)
            if working and prepcounter == 0:
                working = False
                prepcounter = rcounter
                prepcount.config(text=rcounter)
                preplabel.config(text='REST', font=('Arial', 40))
                preplabel.place(x=80, y=200)
                setcounter = setcounter - 1
            elif prepcounter == 0:
                prepcounter = wcounter
                prepcount.config(text=wcounter)
                preplabel.config(text='WORK', font=('Arial', 40))
                preplabel.place(x=80, y=200)
                print(f'setcounter is{setcounter}')
                working = True
                print(f'working is {working}')
        else:
            preplabel.place_forget()
            prepcount.place_forget()
            endlabel = tk.Label(root,text='TAPOS NA BEYBEE',font=('Arial',20))
            endlabel.place(x=30,y=100)








    countdown()



    widgets = [
        setlabel, setminus, setplus, worklabel,workplus,
        workminus,restplus, restminus, restlabel,startbutton,
        restcount,workcount,setcount,cdlabel,cdplus,cdminus,cdcount,
        exelabel,exeplus,exeminus,execount

    ]

    for widget in widgets:
        widget.place_forget()
    preplabel = tk.Label(root,text='PREPARE',font=('Arial',40))
    preplabel.place(x=20,y=200)

    pbutton = tk.Button(root,command=pause,text='Pause')
    pbutton.place(x=245,y=340,height=40,width=40)


exelabel = tk.Label(root,text='EXERCISES',font=('Arial',12))
exelabel.place(x=110, y=25)
exeplus = tk.Button(root,command=exep,text ='+',font=('Arial',20))
exeplus.place(x=210,y=60,height=25,width=25)
exeminus = tk.Button(root,command=exem,text ='-',font=('Arial',20))
exeminus.place(x=60,y=60,height=25,width=25)
execount = tk.Label(root, text=execounter, font=('Arial', 12))
execount.place(x=145, y=60)

setlabel = tk.Label(root,text='SETS',font =('Arial',12))
setlabel.place(x=130, y= 100)
setminus = tk.Button(root,command=setm,text ='-',font=('Arial',20))
setminus.place(x=60,y=135,height=25,width=25)
setplus = tk.Button(root,command=setp,text ='+',font=('Arial',20))
setplus.place(x=210,y=135,height=25,width=25)
setcount = tk.Label(root, text=setcounter, font=('Arial', 12))
setcount.place(x=145, y=135)


worklabel = tk.Label(root,text='WORK',font =('Arial',12))
worklabel.place(x=130, y= 175)
workminus = tk.Button(root,command=workm,text ='-',font=('Arial',20))
workminus.place(x=60,y=210,height=25,width=25)
workplus = tk.Button(root,command=workp,text ='+',font=('Arial',20))
workplus.place(x=210,y=210,height=25,width=25)
workcount = tk.Label(root, text=wcounter, font=('Arial', 12))
workcount.place(x=145, y=210)

restlabel = tk.Label(root,text='REST',font =('Arial',12))
restlabel.place(x=130, y= 250)
restminus = tk.Button(root,command=restm,text ='-',font=('Arial',20))
restminus.place(x=60,y=285,height=25,width=25)

restplus = tk.Button(root,command=restp,text ='+',font=('Arial',20))
restplus.place(x=210,y=285,height=25,width=25)
restcount = tk.Label(root, text=rcounter, font=('Arial', 12))
restcount.place(x=145, y=285)

cdlabel = tk.Label(root,text='COOLDOWN',font =('Arial',12))
cdlabel.place(x=100, y= 325)
cdminus = tk.Button(root,command=cdm,text ='-',font=('Arial',20))
cdminus.place(x=60,y=360,height=25,width=25)
cdplus = tk.Button(root,command=cdp,text ='+',font=('Arial',20))
cdplus.place(x=210,y=360,height=25,width=25)
cdcount = tk.Label(root, text=cdcounter, font=('Arial', 12))
cdcount.place(x=145, y=360)
startbutton = tk.Button(root,command=start,text='START',font=('Arial',12))
startbutton.place(x=120,y=425,height=30,width=60)

root.mainloop()