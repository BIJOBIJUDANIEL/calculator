import tkinter
from tkinter import *

window = Tk()
window.title("BIJO B DANIEL")
window.geometry("470x530")
window.resizable(False, False)
window['background'] = '#544C46'
text = StringVar()
exp = ""


def click_button(num):
    global exp
    exp = exp + str(num)
    text.set(exp)


def equal():
    try:
        global exp
        total = str(eval(exp))
        text.set(total)

    except ZeroDivisionError:
        text.set("Undefined")
        exp = ""


def clear():
    global exp
    exp = ""
    text.set("")


def backspace():
    global exp
    exp = ""
    numLen = len(label.get())
    label.delete(numLen - 1, "end")
    if numLen == 1:
        label.insert(0, "0")


# widgets
label = Entry(window, font=("Arial", 30), width=90, bd=10, justify=RIGHT, bg="white", textvariable=text)
label.pack()

btn1 = Button(window, text="7", width=8, height=2, bg="black", fg="yellow", activebackground="red",
              command=lambda: click_button("7"))
btn1.place(x=30, y=180)
btn2 = Button(window, text="8", width=8, height=2, bg="black", fg="yellow", activebackground="red",
              command=lambda: click_button("8"))
btn2.place(x=140, y=180)
btn3 = Button(window, text="9", width=8, height=2, bg="black", fg="yellow", activebackground="red",
              command=lambda: click_button("9"))
btn3.place(x=250, y=180)
btn4 = Button(window, text="*", width=6, height=2, bg="black", fg="blue", activebackground="yellow", font=1,
              command=lambda: click_button("*"))
btn4.place(x=360, y=100)
btn5 = Button(window, text="4", width=8, height=2, bg="black", fg="yellow", activebackground="red",
              command=lambda: click_button("4"))
btn5.place(x=30, y=260)
btn6 = Button(window, text="5", width=8, height=2, bg="black", fg="yellow", activebackground="red",
              command=lambda: click_button("4"))
btn6.place(x=140, y=260)
btn7 = Button(window, text="6", width=8, height=2, bg="black", fg="yellow", activebackground="red",
              command=lambda: click_button("6"))
btn7.place(x=250, y=260)
btn8 = Button(window, text="-", width=6, height=2, bg="black", fg="blue", activebackground="yellow", font=1,
              command=lambda: click_button("-"))
btn8.place(x=360, y=180)
btn9 = Button(window, text="1", width=8, height=2, bg="black", fg="yellow", activebackground="red",
              command=lambda: click_button("1"))
btn9.place(x=30, y=340)
btn10 = Button(window, text="2", width=8, height=2, bg="black", fg="yellow", activebackground="red",
               command=lambda: click_button("2"))
btn10.place(x=140, y=340)
btn11 = Button(window, text="3", width=8, height=2, bg="black", fg="yellow", activebackground="red",
               command=lambda: click_button("3"))
btn11.place(x=250, y=340)
btn12 = Button(window, text="+", width=6, height=2, bg="black", fg="blue", activebackground="yellow", font=1,
               command=lambda: click_button("+"))
btn12.place(x=360, y=260)
btn13 = Button(window, text="0", width=8, height=2, bg="black", fg="yellow", activebackground="red",
               command=lambda: click_button("0"))
btn13.place(x=30, y=420)
btn14 = Button(window, text=".", width=8, height=2, bg="black", fg="yellow", activebackground="red",
               command=lambda: click_button("."))
btn14.place(x=140, y=420)
btn15 = Button(window, text="C", width=8, height=2, bg="black", fg="yellow", activebackground="orange",
               command=lambda: clear())
btn15.place(x=250, y=420)
btn16 = Button(window, text="/", width=6, height=2, bg="black", fg="blue", font=1, activebackground="red",
               command=lambda: click_button("/"))
btn16.place(x=360, y=340)
btn17 = Button(window, text="<", width=6, height=2, bg="black", fg="green", font=1, activebackground="orange",
               command=lambda: backspace())
btn17.place(x=245, y=100)
btn18 = Button(window, text="=", width=6, height=2, bg="black", fg="blue", font=1, activebackground="indigo",
               command=lambda: equal())
btn18.place(x=360, y=420)

window.mainloop()
