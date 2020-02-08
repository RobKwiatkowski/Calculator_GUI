from tkinter import *


def button_click(number):
    current = e.get()
    # checking if there is  a decimal dot already
    if number == ".":
        if number in current:
            return
        else:
            e.delete(0, END)
            e.insert(0, str(current) + number)

    # in normal case type in a digit
    else:
        e.delete(0, END)
        e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "add"
    f_num = float(first_number)
    e.delete(0, END)


def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "sub"
    f_num = float(first_number)
    e.delete(0, END)


def button_mul():
    first_number = e.get()
    global f_num
    global math
    math = "mul"
    f_num = float(first_number)
    e.delete(0, END)


def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "div"
    f_num = float(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "add":
        e.insert(0, str(f_num + int(second_number)))
    if math == "sub":
        e.insert(0, str(f_num - int(second_number)))
    if math == "mul":
        e.insert(0, str(f_num * int(second_number)))
    if math == "div":
        e.insert(0, str(f_num / int(second_number)))


# main window
root = Tk()
root.title("Simple Calculator")

# results field
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# number buttons
button_1 = Button(root, text="1", padx=30, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=30, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=30, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=30, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=30, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=30, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=30, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=30, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=30, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=30, pady=20, command=lambda: button_click(0))
button_dot = Button(root, text=".", padx=30, pady=20, command=lambda: button_click("."))

# functional buttons
button_add = Button(root, text="+", padx=30, pady=20, command=button_add)
button_sub = Button(root, text="-", padx=31, pady=20, command=button_sub)
button_mul = Button(root, text="*", padx=31, pady=20, command=button_mul)
button_div = Button(root, text="/", padx=31, pady=20, command=button_div)
button_equal = Button(root, text="=", padx=30, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=20, pady=20, command=button_clear)

# defining layout
button_clear.grid(row=0, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_dot.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_equal.grid(row=4, column=2)

button_mul.grid(row=1, column=3)
button_div.grid(row=2, column=3)
button_sub.grid(row=3, column=3)
button_add.grid(row=4, column=3)

# main loop
root.mainloop()