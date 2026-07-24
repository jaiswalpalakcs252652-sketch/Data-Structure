import tkinter as tk
from tkinter import messagebox, simpledialog

class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def enqueue(self, item):
        if len(self.queue) == self.size:
            messagebox.showerror("Queue", "Queue is Full!")
        else:
            self.queue.append(item)
            update_listbox()
            messagebox.showinfo("Success", f"{item} inserted successfully.")

    def dequeue(self):
        if len(self.queue) == 0:
            messagebox.showerror("Queue", "Queue is Empty!")
        else:
            item = self.queue.pop(0)
            update_listbox()
            messagebox.showinfo("Deleted", f"{item} removed successfully.")

    def peek(self):
        if len(self.queue) == 0:
            messagebox.showinfo("Peek", "Queue is Empty!")
        else:
            messagebox.showinfo("Peek", f"Front Element: {self.queue[0]}")

    def traverse(self):
        if len(self.queue) == 0:
            messagebox.showinfo("Queue", "Queue is Empty!")
        else:
            messagebox.showinfo("Queue Elements", " → ".join(self.queue))

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.size


def update_listbox():
    listbox.delete(0, tk.END)
    for item in q.queue:
        listbox.insert(tk.END, item)


def enqueue():
    item = entry.get()
    if item == "":
        messagebox.showwarning("Warning", "Please Enter a Value")
    else:
        q.enqueue(item)
        entry.delete(0, tk.END)


def dequeue():
    q.dequeue()


def peek():
    q.peek()


def traverse():
    q.traverse()


def empty():
    if q.is_empty():
        messagebox.showinfo("Status", "Queue is Empty")
    else:
        messagebox.showinfo("Status", "Queue is Not Empty")


def full():
    if q.is_full():
        messagebox.showinfo("Status", "Queue is Full")
    else:
        messagebox.showinfo("Status", "Queue is Not Full")


root = tk.Tk()
root.title("Queue Operations")
root.geometry("850x550")
root.configure(bg="#F3E8FF")

size = simpledialog.askinteger("Queue Size", "Enter Maximum Queue Size")
if size is None:
    root.destroy()
    exit()

q = Queue(size)

title = tk.Label(
    root,
    text="QUEUE OPERATIONS USING GUI",
    font=("Comic Sans MS", 22, "bold"),
    bg="#F3E8FF",
    fg="#6A0DAD"
)
title.pack(pady=10)

left_frame = tk.Frame(root, bg="#D8B4FE", bd=3, relief="ridge")
left_frame.pack(side="left", fill="y", padx=20, pady=20)

button_style = {
    "font": ("Century Gothic", 11, "bold"),
    "width": 18,
    "bg": "#9D4EDD",
    "fg": "white",
    "activebackground": "#7B2CBF",
    "activeforeground": "white",
    "bd": 2
}

tk.Button(left_frame, text="Enqueue", command=enqueue, **button_style).pack(pady=8)
tk.Button(left_frame, text="Dequeue", command=dequeue, **button_style).pack(pady=8)
tk.Button(left_frame, text="Peek", command=peek, **button_style).pack(pady=8)
tk.Button(left_frame, text="Traverse", command=traverse, **button_style).pack(pady=8)
tk.Button(left_frame, text="Check Empty", command=empty, **button_style).pack(pady=8)
tk.Button(left_frame, text="Check Full", command=full, **button_style).pack(pady=8)

tk.Button(
    left_frame,
    text="EXIT",
    command=root.destroy,
    bg="#FF4D6D",
    fg="white",
    font=("Century Gothic", 11, "bold"),
    width=18
).pack(pady=20)

right_frame = tk.Frame(root, bg="#F3E8FF")
right_frame.pack(side="right", expand=True, fill="both", padx=20, pady=20)

tk.Label(
    right_frame,
    text="Enter Item",
    font=("Comic Sans MS", 16, "bold"),
    bg="#F3E8FF",
    fg="#6A0DAD"
).pack(pady=10)

entry = tk.Entry(
    right_frame,
    font=("Century Gothic", 14),
    width=25,
    bd=3,
    relief="groove"
)
entry.pack(pady=10)

tk.Label(
    right_frame,
    text="Current Queue",
    font=("Comic Sans MS", 18, "bold"),
    bg="#F3E8FF",
    fg="#6A0DAD"
).pack(pady=15)

listbox = tk.Listbox(
    right_frame,
    width=30,
    height=12,
    font=("Century Gothic", 14),
    bg="#FFF0F5",
    fg="#4B0082",
    bd=3,
    relief="sunken"
)
listbox.pack()

root.mainloop()
