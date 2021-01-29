# import time
# import pyautogui

# time.sleep(10)
# r = open("spamming script.txt", 'r')
# for words in r:
# pyautogui.typewrite(words)
# time.sleep(1)
# pyautogui.press("enter")


# ---------------------------------------------------------------------------------------------------------
#                                         TKINTER APP(INCOMPLETE)
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import time
import pyautogui

root = tk.Tk()
root.title("SP")
root.config(bg='Black')
root.resizable(0, 0)

y = []
address = ''


def load_script():
    global address
    global mylabel
    global y
    address = filedialog.askopenfilename(initialdir="C:/",
                                         filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")),
                                         title="Choose a file."
                                         )
    y.append(address)
    mylabel = Label(root, text=address)
    mylabel.grid(row=4, column=0)
    if address == '':
        btn_execute = ttk.Button(root, text='Execute Script', width=30, command=execute, state=DISABLED)
        btn_execute.grid(row=1, column=0)
    else:
        btn_execute = ttk.Button(root, text='Execute Script', width=30, command=execute)
        btn_execute.grid(row=1, column=0)


def execute():
    global address
    time.sleep(5)
    files = open(address, 'r')
    for i in files:
        pyautogui.typewrite(i)
        time.sleep(0)
        pyautogui.press('enter')


def clear():
    global y
    global address
    btn_execute = ttk.Button(root, text='Execute Script', width=30, command=execute, state=DISABLED)
    btn_execute.grid(row=1, column=0)
    mylabel.grid_forget()
    address = ''


btn_load = ttk.Button(root, text='Open script', width=30, command=load_script)
btn_load.grid(row=0, column=0)

btn_execute = ttk.Button(root, text='Execute Script', width=30, command=execute, state=DISABLED)
btn_execute.grid(row=1, column=0)

btn_exit = ttk.Button(root, text='Exit', width=30, command=root.destroy)
btn_exit.grid(row=2, column=0)

btn_clear = ttk.Button(root, text='Clear', width=30, command=clear)
btn_clear.grid(row=3, column=0)

root.mainloop()
