import tkinter as tk
from tkinter import messagebox


class Stack:
    def __init__(self):
        self.items = []

    def insert(self, item, position):
        if position < 0 or position > len(self.items):
            raise IndexError("Invalid Position")
        self.items.insert(position, item)

    def delete(self, position):
        if position < 0 or position >= len(self.items):
            raise IndexError("Invalid Position")
        return self.items.pop(position)

    def peek(self):
        if not self.items:
            raise IndexError("Stack is Empty")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def traverse(self):
        if not self.items:
            return "Stack is Empty"
        return " <- ".join(self.items)

    def display(self):
        if not self.items:
            return "Stack is Empty"
        return "\n".join(reversed(self.items))


stack = Stack()


def update_display():
    stack_display.config(state="normal")
    stack_display.delete(1.0, tk.END)
    stack_display.insert(tk.END, stack.display())
    stack_display.config(state="disabled")


def insert_item():
    item = entry_item.get()
    pos = entry_position.get()

    if item == "" or pos == "":
        messagebox.showerror("Error", "Enter Item and Position")
        return

    try:
        stack.insert(item, int(pos))
        messagebox.showinfo("Success", f"'{item}' inserted successfully.")
        update_display()
    except Exception as e:
        messagebox.showerror("Error", str(e))


def delete_item():
    pos = entry_position.get()

    if pos == "":
        messagebox.showerror("Error", "Enter Position")
        return

    try:
        item = stack.delete(int(pos))
        messagebox.showinfo("Deleted", f"'{item}' deleted successfully.")
        update_display()
    except Exception as e:
        messagebox.showerror("Error", str(e))


def peek_item():
    try:
        messagebox.showinfo("Peek", f"Top Item: {stack.peek()}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def check_empty():
    if stack.is_empty():
        messagebox.showinfo("Stack", "Stack is Empty")
    else:
        messagebox.showinfo("Stack", "Stack is NOT Empty")


def stack_size():
    messagebox.showinfo("Size", f"Stack Size: {stack.size()}")


def traverse_stack():
    messagebox.showinfo("Traverse", stack.traverse())


root = tk.Tk()
root.title("Stack Operations Using GUI")
root.geometry("500x550")
root.configure(bg="lightblue")

title = tk.Label(root, text="STACK OPERATIONS", font=("Arial", 18, "bold"),
                 bg="lightblue", fg="darkblue")
title.pack(pady=10)

tk.Label(root, text="Enter Item:", bg="lightblue",
         font=("Arial", 11)).pack()

entry_item = tk.Entry(root, font=("Arial", 12))
entry_item.pack(pady=5)

tk.Label(root, text="Enter Position:", bg="lightblue",
         font=("Arial", 11)).pack()

entry_position = tk.Entry(root, font=("Arial", 12))
entry_position.pack(pady=5)

tk.Button(root, text="Insert", width=20, bg="lightgreen",
          command=insert_item).pack(pady=5)

tk.Button(root, text="Delete", width=20, bg="tomato", 
          command=delete_item).pack(pady=5)

tk.Button(root, text="Peek", width=20, bg="orange", 
          command=peek_item).pack(pady=5)

tk.Button(root, text="Is Empty?", width=20, bg="yellow", 
          command=check_empty).pack(pady=5)

tk.Button(root, text="Size", width=20, bg="lavender", 
          command=stack_size).pack(pady=5)

tk.Button(root, text="Traverse", width=20, bg="gray", 
          command=traverse_stack).pack(pady=5)

tk.Label(root, text="Current Stack", bg="lightblue",
         font=("Arial", 12, "bold")).pack(pady=10)

stack_display = tk.Text(root, height=10, width=30,
                        font=("Courier New", 12))
stack_display.pack()

stack_display.config(state="disabled")

root.mainloop()
