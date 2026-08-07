import heapq
import tkinter as tk
from tkinter import ttk

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def insert(self, root, key):
        if not root:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        t2 = y.left

        y.left = z
        z.right = t2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        t3 = y.right

        y.right = z
        z.left = t3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def get_height(self, root):
        return root.height if root else 0

    def get_balance(self, root):
        return self.get_height(root.left) - self.get_height(root.right) if root else 0

    def preorder(self, root, result):
        if root:
            result.append(str(root.key))
            self.preorder(root.left, result)
            self.preorder(root.right, result)

class TaskManager:
    def __init__(self):
        self.pq = []

    def add_task(self, priority, description):
        heapq.heappush(self.pq, (priority, description))

    def run_tasks(self):
        result = []
        while self.pq:
            p, t = heapq.heappop(self.pq)
            result.append(f"Priority {p} -> {t}")
        return result

def run_program():
    output.delete("1.0", tk.END)

    avl = AVLTree()
    root = None

    values = entry_avl.get().split(",")

    for value in values:
        value = value.strip()
        if value:
            root = avl.insert(root, int(value))

    preorder = []
    avl.preorder(root, preorder)

    output.insert(tk.END, "AVL Tree Preorder:\n")
    output.insert(tk.END, " ".join(preorder) + "\n\n")

    heap_data = list(map(int, entry_heap.get().split(",")))

    min_heap = heap_data.copy()
    heapq.heapify(min_heap)

    max_heap = [-x for x in heap_data]
    heapq.heapify(max_heap)

    output.insert(tk.END, "Min Heap:\n")
    output.insert(tk.END, str(min_heap) + "\n\n")

    output.insert(tk.END, "Max Heap:\n")
    output.insert(tk.END, str([-x for x in max_heap]) + "\n\n")

    manager = TaskManager()
    manager.add_task(2, "Low priority: Backup database")
    manager.add_task(1, "High priority: Handle emergency patient")
    manager.add_task(3, "Medium priority: Run diagnostics")

    output.insert(tk.END, "Priority Queue:\n")
    for task in manager.run_tasks():
        output.insert(tk.END, task + "\n")

root = tk.Tk()
root.title("AVL Tree and Heap GUI")
root.geometry("700x600")

tk.Label(root, text="AVL Tree Values (comma separated)", font=("Arial", 11)).pack(pady=5)

entry_avl = tk.Entry(root, width=60)
entry_avl.insert(0, "20,4,15,70,50,100,80")
entry_avl.pack()

tk.Label(root, text="Heap Values (comma separated)", font=("Arial", 11)).pack(pady=5)

entry_heap = tk.Entry(root, width=60)
entry_heap.insert(0, "9,5,6,2,3")
entry_heap.pack()

tk.Button(root, text="Run", command=run_program, bg="green", fg="white", width=15).pack(pady=10)

output = tk.Text(root, width=80, height=25)
output.pack(pady=10)

root.mainloop()
