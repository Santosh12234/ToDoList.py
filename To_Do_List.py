# ***TO-DO-LIST-PROJECT (TASK-1)*** #

import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})

    def get_tasks(self):
        return self.tasks

    def mark_task_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            return True
        return False

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            return True
        return False

class ToDoApp:
    def __init__(self, root, task_manager):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("700x700")
        self.root.config(bg="#f0f0f0")

        self.task_manager = task_manager

        self.title_label = tk.Label(self.root, text="To-Do List", font=("Helventica", 16, "bold"), bg="#f0f0f0", fg="#333")
        self.title_label.pack(pady=10)

        self.frame = tk.Frame(self.root, bg="#87CEFA")
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, width=100, height=25, selectmode=tk.SINGLE, bg="#87CEFA", fg="#333")
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry_task = tk.Entry(self.root, width=84, bg="#FFFFFF", fg="#333")
        self.entry_task.pack(pady=10)

        self.button_frame = tk.Frame(self.root, bg="#FFFFFF")
        self.button_frame.pack(pady=10)

        self.button_add_task = tk.Button(self.button_frame, text="Add Task", width=30, command=self.add_task, bg="#006400", fg="#ffffff", font=("Helvetica", 10, "bold"))
        self.button_add_task.grid(row=0, column=0, padx=5)

        self.button_mark_done = tk.Button(self.button_frame, text="Mark Task as Done", width=30, command=self.mark_task_done, bg="#00008B", fg="#ffffff", font=("Helvetica", 10, "bold"))
        self.button_mark_done.grid(row=0, column=1, padx=5)

        self.button_delete_task = tk.Button(self.button_frame, text="Delete Task", width=30, command=self.delete_task, bg="#FFA500", fg="#ffffff", font=("Helvetica", 10, "bold"))
        self.button_delete_task.grid(row=1, column=0, padx=5, pady=5)

        self.button_exit = tk.Button(self.button_frame, text="Exit", width=30, command=self.root.quit, bg="#FF0000", fg="#ffffff", font=("Helvetica", 10, "bold"))
        self.button_exit.grid(row=1, column=1, padx=5, pady=5)

        self.update_task_listbox()

    def add_task(self):
        task = self.entry_task.get()
        if task != "":
            self.task_manager.add_task(task)
            self.update_task_listbox()
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def mark_task_done(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            if self.task_manager.mark_task_done(selected_task_index):
                self.update_task_listbox()
                messagebox.showinfo("Info", "Task marked as done!")
            else:
                messagebox.showwarning("Warning", "Invalid task number!")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def delete_task(self):
        try:
            select_task_index = self.task_listbox.curselection()[0]
            if self.task_manager.delete_task(select_task_index):
                self.update_task_listbox()
                messagebox.showinfo("Info", "Task deleted!")
            else:
                messagebox.showwarning("Warning", "Invalid task number!")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.task_manager.get_tasks()):
            status = "Done" if task["done"] else "Not done"
            self.task_listbox.insert(tk.END, f"{index+1}. {task['task']} - {status}")

if __name__ == "__main__":
    task_manager = TaskManager()
    root = tk.Tk()
    app = ToDoApp(root, task_manager)
    root.mainloop()
