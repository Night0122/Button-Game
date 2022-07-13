from tkinter import *

Window = Tk()
Window.title("Button Game")

count = 0

def click():
    global count
    count+=1
    print(count)
    label.config(text = "You have " + str(count))

label = Label(
    Window,
    text="You have " + str(count),
    font=("Comic Sans", 30)
)

label.pack()


button = Button(Window,
    text="Button!",
    command=click,
    font=("Comic Sans", 50),
    fg="#00FF00",
    bg="#000000",
    activeforeground="#00FF00",
    activebackground="#000000",
    state=ACTIVE,
    ).pack()

Window.mainloop()
