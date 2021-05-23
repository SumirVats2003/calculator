from tkinter import *


def click(event):
    global scvalue
    text = event.widget.cget("text")

    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(scvalue.get())

            except Exception as e:
                print(e)
                value = "Error"

        scvalue.set(value)
        window.update()

    elif text == "C":
        scvalue.set("")
        window.update()

    elif text == "^2":
        c = float(scvalue.get())
        scvalue.set(c**2)
        window.update()

    elif text == "|x|":
        if float(scvalue.get()) >= 0:
            scvalue.set(scvalue.get())
            window.update()

        else:
            v = float(scvalue.get())
            scvalue.set(str(v*(-1)))
            window.update()

    else:
        scvalue.set(scvalue.get() + text)
        window.update()


root = Tk()
root.title("Calculator")
root.resizable(width=False, height=False)
root.configure(background="grey")

scvalue = StringVar()

winFrame = Frame(root, bg="black")
winFrame.pack(side=TOP)

window = Entry(winFrame, border=3, borderwidth=10, font="arial 20 bold", justify=RIGHT, relief=SUNKEN, bg="grey",
               fg="black", textvar=scvalue)
window.pack(padx=5, pady=5)

butFrame = Frame(root, bg="grey")
butFrame.pack(side=BOTTOM, padx=5, pady=5)

butC = Button(butFrame, text="C", height=3, width=9, bg="light grey", relief=RAISED, font="arial 10 bold")
butC.bind("<Button-1>", click)
butC.grid(row=0, column=0, padx=2, pady=2)
butSQR = Button(butFrame, text="^2", height=3, width=9, bg="light grey", relief=RAISED, font="arial 10 bold")
butSQR.bind("<Button-1>", click)
butSQR.grid(row=0, column=1, padx=2, pady=2)
butMOD = Button(butFrame, text="|x|", height=3, width=9, bg="light grey", relief=RAISED, font="arial 10 bold")
butMOD.bind("<Button-1>", click)
butMOD.grid(row=0, column=2, padx=2, pady=2)
butPLUS = Button(butFrame, text="+", height=3, width=9, bg="light grey", relief=RAISED, font="arial 10 bold")
butPLUS.bind("<Button-1>", click)
butPLUS.grid(row=0, column=3, padx=2, pady=2)

but7 = Button(butFrame, text="7", height=3, width=9, bg="aquamarine", relief=RAISED, font="arial 10 bold")
but7.bind("<Button-1>", click)
but7.grid(row=1, column=0, padx=2, pady=2)
but8 = Button(butFrame, text="8", height=3, width=9, bg="aquamarine", relief=RAISED, font="arial 10 bold")
but8.bind("<Button-1>", click)
but8.grid(row=1, column=1, padx=2, pady=2)
but9 = Button(butFrame, text="9", height=3, width=9, bg="aquamarine", relief=RAISED, font="arial 10 bold")
but9.bind("<Button-1>", click)
but9.grid(row=1, column=2, padx=2, pady=2)
butminus = Button(butFrame, text="-", height=3, width=9, bg="light grey", relief=RAISED, font="arial 10 bold")
butminus.bind("<Button-1>", click)
butminus.grid(row=1, column=3, padx=2, pady=2)

but4 = Button(butFrame, text="4", height=3, width=9, bg="aquamarine", relief=RAISED, font="arial 10 bold")
but4.bind("<Button-1>", click)
but4.grid(row=2, column=0, padx=2, pady=2)
but5 = Button(butFrame, text="5", height=3, width=9, bg="aquamarine", relief=RAISED, font="arial 10 bold")
but5.bind("<Button-1>", click)
but5.grid(row=2, column=1, padx=2, pady=2)
but6 = Button(butFrame, text="6", height=3, width=9, bg="aquamarine", relief=RAISED, font="arial 10 bold")
but6.bind("<Button-1>", click)
but6.grid(row=2, column=2, padx=2, pady=2)
butmul = Button(butFrame, text="*", height=3, width=9, bg="light grey", relief=RAISED, font="arial 10 bold")
butmul.bind("<Button-1>", click)
butmul.grid(row=2, column=3, padx=2, pady=2)

but1 = Button(butFrame, text="1", height=3, width=9, bg="aquamarine", relief=RAISED, font="arial 10 bold")
but1.bind("<Button-1>", click)
but1.grid(row=3, column=0, padx=2, pady=2)
but2 = Button(butFrame, text="2", height=3, width=9, bg="aquamarine", relief=RAISED, font="arial 10 bold")
but2.bind("<Button-1>", click)
but2.grid(row=3, column=1, padx=2, pady=2)
but3 = Button(butFrame, text="3", height=3, width=9, bg="aquamarine", relief=RAISED, font="arial 10 bold")
but3.bind("<Button-1>", click)
but3.grid(row=3, column=2, padx=2, pady=2)
butdiv = Button(butFrame, text="/", height=3, width=9, bg="light grey", relief=RAISED, font="arial 10 bold")
butdiv.bind("<Button-1>", click)
butdiv.grid(row=3, column=3, padx=2, pady=2)

but0 = Button(butFrame, text="0", height=3, width=9, bg="light grey", relief=RAISED, font="arial 10 bold")
but0.bind("<Button-1>", click)
but0.grid(row=4, column=0, padx=2, pady=2)
butpoint = Button(butFrame, text=".", height=3, width=9, bg="light grey", relief=RAISED, font="arial 10 bold")
butpoint.bind("<Button-1>", click)
butpoint.grid(row=4, column=1, padx=2, pady=2)
but00 = Button(butFrame, text="00", height=3, width=9, bg="light grey", relief=RAISED, font="arial 10 bold")
but00.bind("<Button-1>", click)
but00.grid(row=4, column=2, padx=2, pady=2)
butequal = Button(butFrame, text="=", height=3, width=9, bg="aquamarine", relief=RAISED, font="arial 10 bold")
butequal.bind("<Button-1>", click)
butequal.grid(row=4, column=3, padx=2, pady=2)

root.mainloop()
