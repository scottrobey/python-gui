import tkinter as tk
from time import sleep
from tkinter import *
from tkinter import BOTH
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

main_window = Tk()

# global textvars
status_text = StringVar()

# global frames we will be updating
instruction_frame = Frame(main_window)
status_frame = Frame(main_window)
go_frame = Frame(main_window)

# global vars - prob better ways of doing this
file_to_send = 'no file chosen'
location_to_receive = ''
wormhole_code = StringVar()
wormhole_code.set('')


def reset():
    global instruction_frame
    global status_frame
    global go_frame

    instruction_frame.destroy()
    status_frame.destroy()
    go_frame.destroy()


def new_instruction(text):
    global instruction_frame

    instruction_frame.destroy()

    instruction_frame = Frame(main_window)
    instruction_frame.pack(expand=TRUE, fill=BOTH)
    instruction_label = Label(instruction_frame, text=text)
    instruction_label.pack()


def update_status(text):
    global status_frame

    status_frame.destroy()

    status_frame = Frame(main_window)
    status_frame.pack(expand=TRUE, fill=BOTH)
    status_label = Label(status_frame, text=text)
    status_label.pack()


def update_go(text, callback):
    global go_frame

    go_frame.destroy()

    go_frame = Frame(main_window)
    go_button = Button(go_frame, text=text, command=callback)
    go_frame.pack()
    go_button.pack()


def go_send_file():
    global go_frame
    go_frame.destroy()
    print(f"Sending file: {file_to_send} to Wormhole...")
    update_status(f"Sending file: {file_to_send} to Wormhole...")

    # TODO: call wormhole here
    wormhole_send_code = 'yoyoma'

    update_status(f"Sending file: {file_to_send} to Wormhole...COMPLETE\n Wormhole Code: {wormhole_send_code}")


def go_receive_file():
    global go_frame
    global wormhole_code

    go_frame.destroy()

    print(f"Receiving file using Wormhole code: {wormhole_code.get()} to location: {location_to_receive}")
    update_status(f"Receiving file using Wormhole code: {wormhole_code.get()} \nDestination location: {location_to_receive}")

    # TODO: call wormhole here


def choose_file():
    global main_window
    global file_to_send
    file_to_send = askopenfilename()

    print(f"File chosen: {file_to_send}")

    update_status(f"File to send: {file_to_send}")

    update_go("Send File Go!", go_send_file)


def choose_location():
    global main_window
    global location_to_receive

    location_to_receive = askdirectory()

    update_status(f"Location where file will be stored: {location_to_receive}")

    update_go("Receive File Go!", go_receive_file)


# top-most buttons
def send_file():
    global instruction_frame
    reset()

    new_instruction('Sending file using wormhole')

    file_path_btn = Button(instruction_frame, text='Select file to send', command=choose_file)
    file_path_btn.pack(side=LEFT)


def receive_file():
    global instruction_frame
    reset()

    new_instruction('Receiving file using wormhole')

    file_path_btn = Button(instruction_frame, text='Select location to place received file', command=choose_location)
    file_path_btn.pack(side=LEFT)

    enter_code_label = Label(instruction_frame, text='Enter the Wormhole Code Here:')
    enter_code_label.pack()
    wormhole_code_box = Entry(instruction_frame, textvariable=wormhole_code)
    wormhole_code_box.pack()


main_window.title("Wormhole UI")
greeting = Label(text="Welcome to Wormhole UI, the quick and easy way to transfer files across the internet using the Magic "
                      "Wormhole protocol")
greeting.pack()

send = Button(
    text="Send A File",
    width=25,
    height=5,
    command=send_file
)
send.pack()

receive = Button(
    text="Receive A File",
    width=25,
    height=5,
    command=receive_file
)
receive.pack()

main_window.mainloop()
