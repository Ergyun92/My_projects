from tkinter import *


def pressing_buttons(number):
    global equation_text
    equation_text = equation_text + str(number)
    equation_label.set(equation_text)


def equals():
    global equation_text
    try:

        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set("Zero Division Error")
        equation_text = ""
    except SyntaxError:
        equation_label.set("Syntax error")
        equation_text = ""


def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""



window = Tk()
window.title("My calculator")
window.geometry("600x600")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=("Arial Black", 20), bg="white", width=25, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35, command= lambda: pressing_buttons(1))
button1.grid(row=0, column=0)
button2 = Button(frame, text=2, height=4, width=9, font=35, command= lambda: pressing_buttons(2))
button2.grid(row=0, column=1)
button3 = Button(frame, text=3, height=4, width=9, font=35, command= lambda: pressing_buttons(3))
button3.grid(row=0, column=2)
button4 = Button(frame, text=4, height=4, width=9, font=35, command= lambda: pressing_buttons(4))
button4.grid(row=1, column=0)
button5 = Button(frame, text=5, height=4, width=9, font=35, command= lambda: pressing_buttons(5))
button5.grid(row=1, column=1)
button6 = Button(frame, text=6, height=4, width=9, font=35, command= lambda: pressing_buttons(6))
button6.grid(row=1, column=2)
button7 = Button(frame, text=7, height=4, width=9, font=35, command= lambda: pressing_buttons(7))
button7.grid(row=2, column=0)
button8 = Button(frame, text=8, height=4, width=9, font=35, command= lambda: pressing_buttons(8))
button8.grid(row=2, column=1)
button9 = Button(frame, text=9, height=4, width=9, font=35, command= lambda: pressing_buttons(9))
button9.grid(row=2, column=2)
button0 = Button(frame, text=0, height=4, width=9, font=35, command= lambda: pressing_buttons(0))
button0.grid(row=3, column=0)
add = Button(frame, text="+", height=4, width=9, font=35, command= lambda: pressing_buttons('+'))
add.grid(row=0, column=3)
subtract = Button(frame, text="-", height=4, width=9, font=35, command= lambda: pressing_buttons('-'))
subtract.grid(row=1, column=3)
multiply = Button(frame, text="*", height=4, width=9, font=35, command= lambda: pressing_buttons('*'))
multiply.grid(row=2, column=3)
divide = Button(frame, text="/", height=4, width=9, font=35, command= lambda: pressing_buttons('/'))
divide.grid(row=3, column=3)
equal = Button(frame, text="=", height=4, width=9, font=35, command= lambda: equals())
equal.grid(row=3, column=2)
decimal = Button(frame, text=".", height=4, width=9, font=35, command= lambda: pressing_buttons('.'))
decimal.grid(row=3, column=1)
clear = Button(window, text="clear", height=4, width=18, font=35, command=clear)
clear.pack()
window.mainloop()