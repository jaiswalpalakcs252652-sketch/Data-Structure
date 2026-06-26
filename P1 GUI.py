import tkinter as tk
from tkinter import messagebox

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self):
        if not self.items:
            raise IndexError("Stack is empty")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        if self.items:
            return " <- ".join(reversed(self.items))
        return "Stack is empty"


stack = Stack()
def update_stack():
    stack_label.config(text="Stack: " + stack.display())

def push_item():
    item = entry.get()
    if item == "":
        messagebox.showwarning("Warning", "Enter an item!")
        return

    stack.push(item)
    messagebox.showinfo("Success", f"'{item}' pushed successfully.")
    entry.delete(0, tk.END)
    update_stack()

def pop_item():
    try:
        item = stack.pop()
        messagebox.showinfo("Popped", f"'{item}' popped successfully.")
        update_stack()
    except IndexError as e:
        messagebox.showerror("Error", str(e))

def peek_item():
    try:
        item = stack.peek()
        messagebox.showinfo("Top Item", f"Top item is: {item}")
    except IndexError as e:
        messagebox.showerror("Error", str(e))

def check_empty():
    if stack.is_empty():
        messagebox.showinfo("Stack Status", "Stack is Empty")
    else:
        messagebox.showinfo("Stack Status", "Stack is Not Empty")

def stack_size():
    messagebox.showinfo("Stack Size", f"Size of Stack: {stack.size()}")


# GUI Window
root = tk.Tk()
root.title("Stack Operations")
root.geometry("450x450")
root.configure(bg="lavender")

title = tk.Label(root, text="Stack Operations", font=("Arial", 16, "bold"), bg="lavender")
title.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

push_btn = tk.Button(root, text="Push", width=20, bg="lightgreen", command=push_item)
push_btn.pack(pady=5)

pop_btn = tk.Button(root, text="Pop", width=20, bg="tomato", command=pop_item)
pop_btn.pack(pady=5)

peek_btn = tk.Button(root, text="Peek", width=20, bg="orange", command=peek_item)
peek_btn.pack(pady=5)

empty_btn = tk.Button(root, text="Is Empty?", width=20, bg="yellow", command=check_empty)
empty_btn.pack(pady=5)

size_btn = tk.Button(root, text="Size", width=20, bg="lightblue", command=stack_size)
size_btn.pack(pady=5)

exit_btn = tk.Button(root, text="Exit", width=20, bg="gray", command=root.destroy)
exit_btn.pack(pady=5)

stack_label = tk.Label(root, text="Stack: Stack is empty", font=("Arial", 12), bg="white", width=40, height=3)
stack_label.pack(pady=20)

root.mainloop()
