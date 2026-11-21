import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("My Task Manager")
root.geometry("350x520")
root.config(bg="#e6f2ff")

tasks = []
selected_index = None

# Load tasks
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task = line.strip()
                tasks.append(task)
                listbox.insert(tk.END, task)
    except:
        pass

# Save tasks
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Add task
def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()

# Delete task
def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        tasks.pop(selected)
        save_tasks()
    except:
        pass

# Mark done
def mark_done():
    try:
        selected = listbox.curselection()[0]
        task = tasks[selected]

        if "[Done]" not in task:
            task = task + " [Done]"
            tasks[selected] = task

            listbox.delete(selected)
            listbox.insert(selected, task)
            save_tasks()
    except:
        pass

# Select task for editing
def select_task(event):
    global selected_index
    try:
        selected_index = listbox.curselection()[0]
        entry.delete(0, tk.END)
        entry.insert(0, tasks[selected_index])
    except:
        pass

# Update task
def update_task():
    global selected_index
    try:
        new_task = entry.get()
        if new_task != "" and selected_index is not None:
            tasks[selected_index] = new_task
            listbox.delete(selected_index)
            listbox.insert(selected_index, new_task)
            entry.delete(0, tk.END)
            save_tasks()
    except:
        pass

# Clear all tasks
def clear_all():
    if messagebox.askyesno("Confirm", "Delete all tasks?"):
        tasks.clear()
        listbox.delete(0, tk.END)
        save_tasks()

# UI
title = tk.Label(root, text="Task Manager",
                 font=("Arial", 18, "bold"),
                 bg="#e6f2ff", fg="#003366")
title.pack(pady=10)

entry = tk.Entry(root, width=25,
                 font=("Arial", 12),
                 bd=3, relief="groove")
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task",
                    width=15, bg="#28a745", fg="white",
                    command=add_task)
add_btn.pack(pady=5)

listbox = tk.Listbox(root,
                     width=30, height=10,
                     font=("Arial", 12),
                     selectbackground="#3399ff")
listbox.pack(pady=10)

listbox.bind("<<ListboxSelect>>", select_task)

update_btn = tk.Button(root, text="Update Task",
                       width=15, bg="#ffc107", fg="black",
                       command=update_task)
update_btn.pack(pady=5)

done_btn = tk.Button(root, text="Mark Done",
                     width=15, bg="#007bff", fg="white",
                     command=mark_done)
done_btn.pack(pady=5)

del_btn = tk.Button(root, text="Delete Task",
                    width=15, bg="#dc3545", fg="white",
                    command=delete_task)
del_btn.pack(pady=5)

clear_btn = tk.Button(root, text="Clear All",
                      width=15, bg="#6c757d", fg="white",
                      command=clear_all)
clear_btn.pack(pady=5)

load_tasks()
root.mainloop()