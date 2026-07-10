import tkinter as tk
from tkinter import messagebox


# ---------------- Player Node ----------------
class Player:
    def __init__(self, name):
        self.name = name
        self.next = None


# ---------------- Linked List ----------------
class GameTeam:
    def __init__(self):
        self.head = None

    def add_first(self, name):
        new = Player(name)
        new.next = self.head
        self.head = new

    def add_last(self, name):
        new = Player(name)

        if self.head is None:
            self.head = new
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new

    def add_position(self, name, pos):
        new = Player(name)

        if pos == 0:
            new.next = self.head
            self.head = new
            return

        temp = self.head

        for i in range(pos - 1):
            if temp is None:
                return False
            temp = temp.next

        if temp is None:
            return False

        new.next = temp.next
        temp.next = new
        return True

    def delete_name(self, name):
        temp = self.head
        prev = None

        while temp:
            if temp.name == name:
                if prev is None:
                    self.head = temp.next
                else:
                    prev.next = temp.next
                return True

            prev = temp
            temp = temp.next

        return False

    def delete_position(self, pos):

        if self.head is None:
            return False

        if pos == 0:
            self.head = self.head.next
            return True

        temp = self.head

        for i in range(pos - 1):
            if temp.next is None:
                return False
            temp = temp.next

        if temp.next:
            temp.next = temp.next.next
            return True

        return False

    def get_players(self):
        players = []
        temp = self.head

        while temp:
            players.append(temp.name)
            temp = temp.next

        return players


# ---------------- GUI ----------------

team = GameTeam()

root = tk.Tk()
root.title("Game Team Management")
root.geometry("500x500")
root.config(bg="lightblue")

title = tk.Label(root, text="GAME TEAM MANAGEMENT",
                 font=("Arial", 18, "bold"),
                 bg="lightblue",
                 fg="darkblue")
title.pack(pady=10)

# Player Name
tk.Label(root, text="Player Name",
         bg="lightblue",
         font=("Arial", 12)).pack()

name_entry = tk.Entry(root, font=("Arial", 12))
name_entry.pack()

# Position
tk.Label(root, text="Position",
         bg="lightblue",
         font=("Arial", 12)).pack()

position_entry = tk.Entry(root, font=("Arial", 12))
position_entry.pack()


# ---------------- Functions ----------------

def display_team():
    listbox.delete(0, tk.END)

    players = team.get_players()

    if not players:
        listbox.insert(tk.END, "No Players in Team")
    else:
        for i, player in enumerate(players):
            listbox.insert(tk.END, f"{i} : {player}")


def add_first():
    name = name_entry.get()

    if name == "":
        messagebox.showerror("Error", "Enter Player Name")
        return

    team.add_first(name)
    display_team()


def add_last():
    name = name_entry.get()

    if name == "":
        messagebox.showerror("Error", "Enter Player Name")
        return

    team.add_last(name)
    display_team()


def add_position():
    try:
        name = name_entry.get()
        pos = int(position_entry.get())

        if team.add_position(name, pos) == False:
            messagebox.showerror("Error", "Invalid Position")

        display_team()

    except:
        messagebox.showerror("Error", "Enter Valid Position")


def delete_name():
    name = name_entry.get()

    if team.delete_name(name):
        display_team()
    else:
        messagebox.showerror("Error", "Player Not Found")


def delete_position():
    try:
        pos = int(position_entry.get())

        if team.delete_position(pos):
            display_team()
        else:
            messagebox.showerror("Error", "Invalid Position")

    except:
        messagebox.showerror("Error", "Enter Valid Position")


# ---------------- Buttons ----------------

tk.Button(root,
          text="Add at Beginning",
          width=20,
          bg="green",
          fg="white",
          command=add_first).pack(pady=4)

tk.Button(root,
          text="Add at End",
          width=20,
          bg="green",
          fg="white",
          command=add_last).pack(pady=4)

tk.Button(root,
          text="Add at Position",
          width=20,
          bg="blue",
          fg="white",
          command=add_position).pack(pady=4)

tk.Button(root,
          text="Remove by Name",
          width=20,
          bg="red",
          fg="white",
          command=delete_name).pack(pady=4)

tk.Button(root,
          text="Remove by Position",
          width=20,
          bg="red",
          fg="white",
          command=delete_position).pack(pady=4)

tk.Button(root,
          text="Show Team",
          width=20,
          bg="orange",
          command=display_team).pack(pady=4)

# Listbox
listbox = tk.Listbox(root,
                     width=40,
                     height=10,
                     font=("Arial", 12))

listbox.pack(pady=10)

root.mainloop()
