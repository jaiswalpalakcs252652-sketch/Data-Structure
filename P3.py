import time
from colorama import init, Fore, Style


class Player:
    def __init__(self, name):
        self.name = name
        self.next = None


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
                print("Invalid Position")
                return
            temp = temp.next

        new.next = temp.next
        temp.next = new

    def delete_name(self, name):
        temp = self.head
        prev = None

        while temp:
            if temp.name == name:
                if prev is None:
                    self.head = temp.next
                else:
                    prev.next = temp.next
                return

            prev = temp
            temp = temp.next

        print("Player not found")

    def delete_position(self, pos):
        if self.head is None:
            return

        if pos == 0:
            self.head = self.head.next
            return

        temp = self.head

        for i in range(pos - 1):
            if temp.next is None:
                print("Invalid Position")
                return
            temp = temp.next

        if temp.next:
            temp.next = temp.next.next

    def display(self):
        if self.head is None:
            print("No Players in Team")
            return

        print("\nGame Team:")

        temp = self.head

        while temp:
            print(temp.name)
            temp = temp.next


team = GameTeam()

while True:

    print("\n----- GAME TEAM MENU -----")
    print("1. Add Player at Beginning")
    print("2. Add Player at End")
    print("3. Add Player at Position")
    print("4. Remove Player by Name")
    print("5. Remove Player by Position")
    print("6. Show Team")
    print("7. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        name = input("Enter Player Name: ")
        team.add_first(name)

    elif choice == 2:
        name = input("Enter Player Name: ")
        team.add_last(name)

    elif choice == 3:
        name = input("Enter Player Name: ")
        pos = int(input("Enter Position: "))
        team.add_position(name, pos)

    elif choice == 4:
        name = input("Enter Player Name to Remove: ")
        team.delete_name(name)

    elif choice == 5:
        pos = int(input("Enter Position to Remove: "))
        team.delete_position(pos)

    elif choice == 6:
        team.display()

    elif choice == 7:
        print("Game Over!")
        break

    else:
        print("Invalid Choice")

    time.sleep(1)
