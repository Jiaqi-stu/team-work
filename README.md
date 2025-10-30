# team-work
import datetime
import time
import tkinter as tk
from  tkinter import simpledialog, messagebox

#
todo_list = []

def add_todo():
    """
    root = tk.Tk()
    root.withdraw()

    #
    task = simpledialog.askstring(")
    if not time_str:
        retrun

    #
    try:
        remind_time = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M")
        todo_list.append({"task": task, "time": remind_time})
        messagebox.showinfo(")

def check_reminders():
    """
    while True:
        now = datetime.datetime.now()
        #
        for todo in todo_list[:]: #
            if now >= todo["time"]:
                #
                root = tk.Tk()
                root.withdraw()
                messagebox.showwarning(")
                todo_list.remove(todo)
        time.sleep(60)

def main():
    #
    add_todo()
    #
    root = tk.Tk()
    root.withdraw()
    while messagebox.askyesno(")
        add_todo()

    messagebox.askyesno(")
    check_reminders()

if __name__ == "__main__":
    main()