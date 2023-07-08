from tkinter import *

master = Tk()

counter = 1


def change_text(text=''):
    global counter
    counter += 1
    my_var.set(f"Click {text} {str(counter)}")


def send_file():
    change_text("sending")


send = Button(
    text="Send A File",
    width=25,
    height=5,
    command=send_file
)
send.pack()

my_var = StringVar()
my_var.set("First click")
label = Label(master, textvariable=my_var, fg="red")
button = Button(master, text="Submit", command=change_text)
button.pack()
label.pack()

master.mainloop()
