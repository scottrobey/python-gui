import subprocess
import tkinter as tk
from time import sleep
import os
from tkinter import *
from tkinter import BOTH
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
from subprocess import Popen, PIPE
import re as regex

main_window = Tk()

# global textvars, TODO: figure out why textvar didn't update
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


def human_readable_size(size, decimal_places=2):
    for unit in ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB']:
        if size < 1024.0 or unit == 'PiB':
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f} {unit}"


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


def check_if_wormhole_exists():
    completed = subprocess.run(['which', 'wormhole'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if completed.returncode == 0:
        return True
    else:
        update_status("wormhole command line not present or is not configured in PATH. Install Magic Wormhole from: "
                      "https://github.com/magic-wormhole/magic-wormhole and try again")
        return False


def go_send_file():
    global go_frame
    go_frame.destroy()
    print(f"Sending file: {file_to_send} to Wormhole...")
    update_status(f"(Please Wait) Sending file: {file_to_send} to Wormhole...")

    pattern = regex.compile('Wormhole code is:.*')

    if check_if_wormhole_exists():
        # call wormhole here -  see: https://stackoverflow.com/a/17698359
        #  Example:  wormhole send <file_to_send>
        #  TODO: Implement a cancel button since we may want the ability to cancel a file being sent. The send should prob
        #        be done in a separate window so the UX related to cancel is cleaner
        output_buff = ''
        with Popen(["wormhole", "send", f"{file_to_send}"], stdout=PIPE, stderr=subprocess.STDOUT, bufsize=1,
                   universal_newlines=True) as p:
            for line in p.stdout:
                print(line, end='')
                output_buff += line
                if pattern.match(line):
                    update_status(f"File has been sent to wormhole, waiting for file to be received - {line}")
                    main_window.update_idletasks()

        if p.returncode != 0:
            print(f"Process Failed with exit code: {p.returncode}")
            update_status(f"** Send file failed** \n {output_buff}")
        else:
            update_status(f"File sent successfully")

        main_window.update_idletasks()


def go_receive_file():
    global go_frame
    global wormhole_code

    go_frame.destroy()

    print(f"Receiving file using Wormhole code: {wormhole_code.get()} to location: {location_to_receive}")

    update_status(f"Receiving file using Wormhole code: {wormhole_code.get()} \nDestination location: {location_to_receive}")

    # TODO: call wormhole here -
    # Example: wormhole receive --accept-file <wormhole_code>
    # Call will block 'Waiting for sender...'  so need to implement a cancel feature
    # Should prob put the send and receive into it's own window so the cancel makes more UX sense
    # Note: need to switch the working directory to location_to_receive
    # Afterwards stat the file to ensure it was received
    # Note if the file already exists the wormhole receive command will fail -
    # TODO: add a feature to override files received. Implement this by creating a temp dir to receive the file then moving it
    #       back to the location_to_receive


def choose_file():
    global main_window
    global file_to_send
    file_to_send = askopenfilename(parent=main_window, initialdir=r'.', title='Choose File to Send')

    if file_to_send != '':
        print(f"File chosen: {file_to_send}")

        if os.path.isfile(file_to_send):
            file_size = human_readable_size(os.path.getsize(file_to_send))
            update_status(f"File to send: {file_to_send}, size: {file_size}")
            update_go("Send File Go!", go_send_file)
        else:
            print(f"Not a file: {file_to_send}")
    else:
        print("No file selected")


def choose_location():
    global main_window
    global location_to_receive

    location_to_receive = askdirectory(parent=main_window, initialdir=r'.', title='Choose Location to Store Received File')

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
greeting = Label(text=
                 "Welcome to Wormhole UI, the quick and easy way to transfer files across the internet using the Magic "
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
