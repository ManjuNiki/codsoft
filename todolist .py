import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("To-Do List Application")

# Create a list to store tasks
tasks = []

# Define functions for task management
def add_task():
    task = task_entry.get("1.0", tk.END).strip()  # Get all text from the Text widget
    if task != "":
        print("task1",task)
        tasks_listbox.insert(tk.END, task)  # Add to the Listbox
        tasks.append(task)  # Add to the list of tasks
        task_entry.delete("1.0", tk.END)  # Clear the Text widget
    else:
        print("task",task)
        messagebox.showwarning("Warning", "You must enter a task.")

def view_task():
    try:
        selected_index = tasks_listbox.curselection()[0]  # Get selected task index
        selected_task = tasks[selected_index]  # Get the task from the list
        messagebox.showinfo("View Task", f"Task: {selected_task}")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to view.")

def delete_task():
    try:
        selected_index = tasks_listbox.curselection()[0]  # Get selected task index
        tasks_listbox.delete(selected_index)  # Remove from Listbox
        tasks.pop(selected_index)  # Remove from list of tasks
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# UI Elements

# Multi-line text box for entering tasks
task_entry = tk.Text(root, width=50, height=5)
task_entry.pack(pady=10)

# Buttons for task operations
add_button = tk.Button(root, text="Add Task", width=12, command=add_task)
add_button.pack(pady=5)

view_button = tk.Button(root, text="View Task", width=12, command=view_task)
view_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=12, command=delete_task)
delete_button.pack(pady=5)

# Listbox to display tasks
tasks_listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
tasks_listbox.pack(pady=10)

# Run the application
root.mainloop()