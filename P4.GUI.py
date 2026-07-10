import tkinter as tk
from tkinter import messagebox


class Node:
    def __init__(self, table):
        self.data = table
        self.next = None
        self.prev = None


class RestaurantReservation:
    def __init__(self):
        self.head = None

    def reserve_beginning(self, table):
        new = Node(table)
        if self.head is None:
            self.head = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new

    def reserve_end(self, table):
        new = Node(table)

        if self.head is None:
            self.head = new
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new
        new.prev = temp

    def reserve_position(self, table, pos):

        if pos == 0:
            self.reserve_beginning(table)
            return

        temp = self.head

        for i in range(pos):
            if temp is None:
                raise Exception("Invalid Position")
            temp = temp.next

        if temp is None:
            raise Exception("Invalid Position")

        new = Node(table)

        new.next = temp
        new.prev = temp.prev

        if temp.prev:
            temp.prev.next = new

        temp.prev = new

    def cancel_beginning(self):

        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def cancel_end(self):

        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.prev.next = None

    def cancel_position(self, pos):

        if self.head is None:
            return

        temp = self.head

        for i in range(pos):
            if temp is None:
                raise Exception("Invalid Position")
            temp = temp.next

        if temp is None:
            raise Exception("Invalid Position")

        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next

        if temp.next:
            temp.next.prev = temp.prev

    def display(self):

        tables = []
        temp = self.head

        while temp:
            tables.append(str(temp.data))
            temp = temp.next

        return " <-> ".join(tables)

    def search(self, table):

        temp = self.head

        while temp:
            if temp.data == table:
                return True
            temp = temp.next

        return False

    def total(self):

        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count


restaurant = RestaurantReservation()


def refresh():
    data = restaurant.display()

    if data == "":
        output.config(text="No Reserved Tables")
    else:
        output.config(text=data)


def reserve_first():
    try:
        table = int(table_entry.get())
        restaurant.reserve_beginning(table)
        refresh()
        messagebox.showinfo("Success", "Table Reserved at Beginning")
    except:
        messagebox.showerror("Error", "Enter Valid Table Number")


def reserve_last():
    try:
        table = int(table_entry.get())
        restaurant.reserve_end(table)
        refresh()
        messagebox.showinfo("Success", "Table Reserved at End")
    except:
        messagebox.showerror("Error", "Enter Valid Table Number")


def reserve_pos():
    try:
        table = int(table_entry.get())
        pos = int(position_entry.get())
        restaurant.reserve_position(table, pos)
        refresh()
        messagebox.showinfo("Success", "Reservation Added")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def cancel_first():
    restaurant.cancel_beginning()
    refresh()


def cancel_last():
    restaurant.cancel_end()
    refresh()


def cancel_pos():
    try:
        pos = int(position_entry.get())
        restaurant.cancel_position(pos)
        refresh()
    except Exception as e:
        messagebox.showerror("Error", str(e))


def search():
    try:
        table = int(table_entry.get())

        if restaurant.search(table):
            messagebox.showinfo("Search", "Table Found")
        else:
            messagebox.showwarning("Search", "Table Not Found")

    except:
        messagebox.showerror("Error", "Enter Valid Table Number")


def total():
    messagebox.showinfo("Total Reservations",
                        f"{restaurant.total()} Reservations")


root = tk.Tk()
root.title("Restaurant Table Reservation System")
root.geometry("700x600")
root.configure(bg="#F8E8D0")

title = tk.Label(root,
                 text="🍽 RESTAURANT TABLE RESERVATION 🍽",
                 font=("Arial", 18, "bold"),
                 bg="#8B0000",
                 fg="white",
                 pady=10)

title.pack(fill="x", pady=10)

tk.Label(root,
         text="Table Number",
         font=("Arial", 12),
         bg="#F8E8D0").pack()

table_entry = tk.Entry(root, font=("Arial", 12))
table_entry.pack(pady=5)

tk.Label(root,
         text="Position",
         font=("Arial", 12),
         bg="#F8E8D0").pack()

position_entry = tk.Entry(root, font=("Arial", 12))
position_entry.pack(pady=5)

frame = tk.Frame(root, bg="#F8E8D0")
frame.pack(pady=15)

tk.Button(frame, text="Reserve First", width=18,
          command=reserve_first).grid(row=0, column=0, padx=5, pady=5)

tk.Button(frame, text="Reserve Last", width=18,
          command=reserve_last).grid(row=0, column=1, padx=5, pady=5)

tk.Button(frame, text="Reserve Position", width=18,
          command=reserve_pos).grid(row=0, column=2, padx=5, pady=5)

tk.Button(frame, text="Cancel First", width=18,
          command=cancel_first).grid(row=1, column=0, padx=5, pady=5)

tk.Button(frame, text="Cancel Last", width=18,
          command=cancel_last).grid(row=1, column=1, padx=5, pady=5)

tk.Button(frame, text="Cancel Position", width=18,
          command=cancel_pos).grid(row=1, column=2, padx=5, pady=5)

tk.Button(frame, text="Search Table", width=18,
          command=search).grid(row=2, column=0, padx=5, pady=5)

tk.Button(frame, text="Total Reservations", width=18,
          command=total).grid(row=2, column=1, padx=5, pady=5)

tk.Button(frame, text="Display", width=18,
          command=refresh).grid(row=2, column=2, padx=5, pady=5)

tk.Label(root,
         text="Reserved Tables",
         font=("Arial", 14, "bold"),
         bg="#F8E8D0").pack(pady=10)

output = tk.Label(root,
                  text="No Reserved Tables",
                  font=("Arial", 13),
                  bg="white",
                  width=60,
                  height=6,
                  relief="sunken",
                  wraplength=500)

output.pack(pady=10)

tk.Button(root,
          text="Exit",
          font=("Arial", 12, "bold"),
          bg="red",
          fg="white",
          command=root.destroy).pack(pady=15)

root.mainloop()
