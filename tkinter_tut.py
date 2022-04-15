from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("Calculator")

display = Label(root, text="_")
display.pack()

def correct():
  display["text"] = "✅"

def wrong():
  display["text"] = "❌"


button = Button(root, text="no", command=wrong)
button.pack()
button = Button(root, text="yes", command=correct)
button.pack()

e = Entry(root, width=28, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

frame = LabelFrame(root, text='this is my frame', padx=10, pady=10)
frame.grid()
img = ImageTk.PhotoImage(Image.open("heart.png"))

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_signs(sign):
    first_number = e.get()
    global f_num
    global math
    math = sign
    f_num = int(first_number)
    e.delete(0, END)

def button_clear():
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "add":
        e.insert(0, f_num + int(second_number))
    elif math == "sub":
        e.insert(0, f_num - int(second_number))
    elif math == "mul":
        e.insert(0, f_num * int(second_number))
    elif math == "div":
        e.insert(0, f_num / int(second_number))


button_1 = Button(frame, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(frame, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(frame, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(frame, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(frame, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(frame, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(frame, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(frame, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(frame, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(frame, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(frame, text="+", padx=39, pady=20, command=lambda: button_signs("add"))
button_equal = Button(frame, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(frame, text="Clear", padx=79, pady=20, command=button_clear)

button_subtract = Button(frame, text="-", padx=41, pady=20, command=lambda: button_signs("sub"))
button_multiply = Button(frame, text="*", padx=40, pady=20, command=lambda: button_signs("mul"))
button_divide = Button(frame, text="/", padx=41, pady=20, command=lambda: button_signs("div"))

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

label = Label(image=img)
label.grid(row=7, column=0, columnspan=3)

# r = IntVar()
# r.get()

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Olives", "Olives"),

]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).grid(sticky=W)

def clicked(value):
    lab = Label(root, text=value)
    lab.grid()

# Radiobutton(root, text='option 1', variable=r, value=1, command=lambda: clicked(1)).grid()
# Radiobutton(root, text='option 2', variable=r, value=2, command=lambda: clicked(2)).grid()

# showinfo, showwarning, showerror, askquestion(returns "yes" or "no"), askokcancel(returns 0/1), askyesno(also 0/1)
def popup():
    response = messagebox.askokcancel("This is my popup", "Hello")
    if response ==1:
        Label(root, text="you clicked yes").grid()
    else:
        Label(root, text="you canceled").grid()

    # messagebox.showwarning("This is my popup", "Hello")

Button(root, text='Popup', command=popup).grid()

# ANOTHER WINDOW
def open():
    top = Toplevel()
    Label(top, text="Herro").grid()

Button(root, text='open 2nd window', command=open).grid()

# SLIDERS
def slide(i):
    Label(root, text=horizontal.get()).grid()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


vertical = Scale(root, from_=400, to=800, command=slide)
vertical.grid(row=0, column=4)

horizontal = Scale(root, from_=400, to=800, orient=HORIZONTAL, command=slide)
horizontal.grid()

#CHECKBOXES
var = IntVar()
c = Checkbutton(root, text="check this", variable=var).grid(row=1, column=4)
Label(root, text=var.get()).grid(row=2, column=4)

# DROP DOWN MENUS
def show():
    label = Label(root, text=click.get()).grid(row=5, column=4)

options = ["mon", "tues", "wed", "thurs", "fri"]
click = StringVar()
click.set(options[0])
drop = OptionMenu(root, click, *options).grid(row=3, column=4)
Button(root, text='show', command=show).grid(row=4, column=4)

root.mainloop()

#######

class Example():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("some application")

        # menu left
        self.menu_left = tk.Frame(self.root, width=150, bg="#ababab")
        self.menu_left_upper = tk.Frame(self.menu_left, width=150, height=150, bg="red")
        self.menu_left_lower = tk.Frame(self.menu_left, width=150, bg="blue")

        self.menu_left_upper.pack(side='top', fill="both", expand=True)
        self.menu_left_lower.pack(side='bottom', fill="both", expand=True)

        # right area
        self.some_title_frame = tk.Frame(self.root, bg="#dfdfdf")

        self.some_title = tk.Label(self.some_title_frame, text="some title", bg="#dfdfdf")
        self.some_title.pack()

        self.canvas_area = tk.Canvas(self.root, width=500, height=400, background="#ffffff")
        self.canvas_area.grid(row=1, column=1)

        # status bar
        self.status_frame = tk.Frame(self.root)
        self.status = tk.Label(self.status_frame, text="this is the status bar")
        self.status.pack(fill="both", expand=True)

        self.menu_left.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.some_title_frame.grid(row=0, column=1, sticky="ew")
        self.canvas_area.grid(row=1, column=1, sticky="nsew")
        self.status_frame.grid(row=2, column=0, columnspan=2, sticky="ew")

        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        self.root.mainloop()

Example()

####

import csv
import datetime

data = 'data.txt.txt'
showrecomms = 'recoms.txt'
fieldnames = ['name', 'time', 'closed_days', 'type', 'special_info']


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def entering():
    restaurant = []
    enter = True
    while enter:
        name = input('Enter restaurant name: ')
        restaurant.append(name)

        dis = input('How long does it take to get the food?')
        if is_int(dis):
            pass
        else:
            print("None")
            dis = None
        restaurant.append(dis)

        closeday = input('What days is it closed? (0 is sunday, separate with commas)')
        restaurant.append(closeday)

        type = input('What type of food is it?')
        restaurant.append(type)

        special_info = input('Anything special?')
        restaurant.append(special_info)

        writing(restaurant)
        enter = False
    else:
        pass


def writing(rlist):
    with open(data, 'a') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        row = {'name': str(rlist[0]), 'time': str(rlist[1]), 'closed_days': str(rlist[2]),
               'type': str(rlist[3]), 'special_info': str(rlist[4])}
        writer.writerow(row)
        print(row)


def finding():
    timesys = datetime.datetime.now()
    dayofweek = str(timesys.strftime('%w'))  # 0 is sunday
    # dayofweek = str(0)
    recomms = []

    max_time = input("Max Wait Time: ")
    print("finding...")

    with open(data, 'r') as f:
        reader = csv.DictReader(f)

        for line in reader:
            closeday = line['closed_days']
            closedaylist = closeday.split(',')
            if dayofweek in closedaylist:
                pass # not open
            else:
                taketime = line['time']
                if int(taketime) <= int(max_time):
                    recomms.append(line)
                else:
                    pass

    with open(showrecomms, 'w') as f:
        fnames = ['name', 'time', 'special_info']
        writer = csv.DictWriter(f, fieldnames=fnames)
        writer.writeheader()
        for rlist in recomms:
            del rlist['type']
            del rlist['closed_days']
            writer.writerow(rlist)


def print_alldata(text):
    with open(text, 'r') as f:
        csv_reader = csv.DictReader(f)

        for line in csv_reader:  # expecting commas
            print(line)


def clear():
    with open(data, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()


def delete():
    resta = input('which restaurant do you want to delete?')

    keeps = []
    with open(data, 'r') as f:
        csv_reader = csv.DictReader(f)
        for line in csv_reader:  # expecting commas
            if resta != line['name']:
                keeps.append(line)
            else:
                print(resta, "deleted")

    with open(data, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for k in keeps:
            writer.writerow(k)

def main():
    run = True

    while run:
        choice = input('Find restaurant or enter one?')
        string = choice.lower()

        if string == "find":
            finding()
            print_alldata(showrecomms)

        elif string == "enter":
            entering()
            print("entered")

        elif string == "clear":
            really = input("Do you really want to clear?")
            if really == "yes":
                clear()
            else:
                pass

        elif string == "read":
            print_alldata(data)

        elif string == "delete":
            delete()

        elif string == "quit":
            run = False

        else:
            print("Invalid request")


main()

