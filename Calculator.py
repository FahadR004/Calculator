from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Calculator")
entry_box = Entry(root,width=35, borderwidth=10)
entry_box.grid(row=0, column=0, columnspan=4)


def clr_button():
    entry_box.delete(0, END)


def click_button(num):
    current_number = entry_box.get()
    entry_box.delete(0, END)
    entry_box.insert(0, str(current_number) + str(num))


def eql_button():
    try:
        answer = str(entry_box.get())
        if "^2" in answer:
            answer = answer.replace("^2", "**2")
        if "^0.5" in answer:
            answer = answer.replace("^0.5", "**0.5")
        answer = eval(answer)
    except ZeroDivisionError as e:
        icon = messagebox.showerror("Zero Error", "CANNOT DIVIDE BY 0!")
    except SyntaxError:
        icon = messagebox.showerror("Syntax Error", "INVALID SYNTAX")
    except TypeError:
        icon = messagebox.showerror("Type Error", "INVALID SYNTAX")
    else:
        entry_box.delete(0, END)
        entry_box.insert(0, str(answer))


button_1 = Button(root, padx=21, pady=20, text=1, command=lambda: click_button(1))
button_2 = Button(root, padx=23, pady=20, text=2, command=lambda: click_button(2))
button_3 = Button(root, padx=21, pady=20, text=3, command=lambda: click_button(3))
button_4 = Button(root, padx=21, pady=20, text=4, command=lambda: click_button(4))
button_5 = Button(root, padx=23, pady=20, text=5, command=lambda: click_button(5))
button_6 = Button(root, padx=21, pady=20, text=6, command=lambda: click_button(6))
button_7 = Button(root, padx=21, pady=20, text=7, command=lambda: click_button(7))
button_8 = Button(root, padx=23, pady=20, text=8, command=lambda: click_button(8))
button_9 = Button(root, padx=21, pady=20, text=9, command=lambda: click_button(9))
button_0 = Button(root, padx=23, pady=20, text=0, command=lambda: click_button(0))

add_button = Button(root, padx=20, pady=20, text="+", command=lambda: click_button("+"))
subtract_button = Button(root, padx=21, pady=20, text="-", command=lambda: click_button("-"))
multiply_button = Button(root, padx=21, pady=20, text="x", command=lambda: click_button("*"))
divide_button = Button(root, padx=21, pady=20, text="/", command=lambda: click_button("/"))

clear_button = Button(root, padx=20, pady=20, text="C", command=clr_button)
equal_button = Button(root, padx=20, pady=20, text="=", command=eql_button)

sqrt_button = Button(root, padx=20, pady=20, text="√", command=lambda: click_button("^0.5"))
square_button = Button(root, padx=20, pady=20, text="^2", command=lambda: click_button("^2"))
left_bracket_button = Button(root, padx=22, pady=20, text="(", command=lambda: click_button("("))
rt_bracket_button = Button(root, padx=22, pady=20, text=")", command= lambda: click_button(")"))

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
multiply_button.grid(row=4, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
subtract_button.grid(row=3, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
add_button.grid(row=2, column=3)

clear_button.grid(row=5, column=0)
button_0.grid(row=5, column=1)
equal_button.grid(row=5, column=2)
divide_button.grid(row=5, column=3)

sqrt_button.grid(row=1, column=0)
square_button.grid(row=1, column=1)
left_bracket_button.grid(row=1, column=2)
rt_bracket_button.grid(row=1, column=3)

root.mainloop()
