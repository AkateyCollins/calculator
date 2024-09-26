import tkinter as tk
from functools import partial
import math

def add_digit(digit):
    current = display_var.get()
    display_var.set(current + str(digit))

def add_operator(operator):
    current = display_var.get()
    if current and current[-1].isdigit():
        display_var.set(current + operator)

def clear_display():
    display_var.set("")

def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(result)
    except:
        display_var.set("Error")

def square():
    try:
        current = display_var.get()
        result = eval(current + '**2')
        display_var.set(result)
    except:
        display_var.set("Error")

def square_root():
    try:
        current = float(display_var.get())
        result = math.sqrt(current)
        display_var.set(result)
    except:
        display_var.set("Error")
def add_decimal():
    current = display_var.get()
    if '.' not in current:
        display_var.set(current + '.')

root = tk.Tk()
root.title("Calculator")
root.geometry("300x300")

display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, font=("Arial", 18), justify="left", bd=5, relief=tk.GROOVE)
display.grid(row=0, column=0, columnspan=4, sticky="nsew",padx=5, pady=5)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('^2', 1, 4), ('√', 2, 4),('.', 4, 4)
]

for (text, row, col) in buttons:
    if text == 'C':
        command = clear_display
    elif text == '=':
        command = calculate
    elif text == '^2':
        command = square
    elif text == '√':
        command = square_root
    else:
        if text.isdigit():
            command = partial(add_digit, text)
        else:
            command = partial(add_operator, text)
    btn = tk.Button(root, text=text, font=("Arial", 14), command=command, bd=5, relief=tk.RAISED,)
    if text == 'C':
        btn.config(bg="#b2beb5")
    elif text == "=":
        btn.config(bg="#b2beb5")
    btn.grid(row=row, column=col, sticky="nsew")

# Configure row and column to resize proportionally
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(5):
    root.grid_columnconfigure(i, weight=1)
root.mainloop()