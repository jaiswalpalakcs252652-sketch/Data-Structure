import time
from colorama import init, Fore, Style

init(autoreset=True)


class Node:
    def __init__(self, table_no):
        self.data = table_no
        self.next = None
        self.prev = None


class RestaurantReservation:
    def __init__(self):
        self.head = None

    # Insert at Beginning
    def reserve_at_beginning(self, table_no):
        new_node = Node(table_no)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Insert at End
    def reserve_at_end(self, table_no):
        new_node = Node(table_no)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

    # Insert at Position
    def reserve_at_position(self, table_no, position):

        if position == 0:
            self.reserve_at_beginning(table_no)
            return

        new_node = Node(table_no)
        temp = self.head

        for i in range(position):
            if temp is None:
                raise IndexError("Position out of bounds.")
            temp = temp.next

        if temp is None:
            raise IndexError("Position out of bounds.")

        new_node.next = temp
        new_node.prev = temp.prev

        if temp.prev:
            temp.prev.next = new_node

        temp.prev = new_node

    # Delete Beginning
    def cancel_beginning(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    # Delete End
    def cancel_end(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.prev.next = None

    # Delete Position
    def cancel_position(self, position):

        if self.head is None:
            return

        temp = self.head

        for i in range(position):
            if temp is None:
                raise IndexError("Position out of bounds.")
            temp = temp.next

        if temp is None:
            raise IndexError("Position out of bounds.")

        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next

        if temp.next:
            temp.next.prev = temp.prev

    # Display
    def display_tables(self):

        if self.head is None:
            print(Fore.RED + "\nNo Reserved Tables.")
            return

        print(Fore.GREEN + "\nReserved Tables:")

        temp = self.head

        while temp:
            print(f"Table {temp.data}", end=" <-> ")
            temp = temp.next

        print("END")

    # Search
    def search_table(self, table_no):
        temp = self.head

        while temp:
            if temp.data == table_no:
                return True
            temp = temp.next

        return False

    # Length
    def total_reservations(self):

        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count


def menu():
    print("\n" + Style.BRIGHT + Fore.YELLOW +
          "===== RESTAURANT TABLE RESERVATION SYSTEM =====")

    print("1.", Fore.CYAN + "Reserve Table at Beginning")
    print("2.", Fore.CYAN + "Reserve Table at End")
    print("3.", Fore.CYAN + "Reserve Table at Position")
    print("4.", Fore.RED + "Cancel First Reservation")
    print("5.", Fore.RED + "Cancel Last Reservation")
    print("6.", Fore.RED + "Cancel Reservation at Position")
    print("7.", Fore.GREEN + "Display Reserved Tables")
    print("8.", Fore.BLUE + "Search Reserved Table")
    print("9.", Fore.MAGENTA + "Total Reservations")
    print("10.", Fore.YELLOW + "Exit")


def main():

    restaurant = RestaurantReservation()

    while True:

        menu()

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                table = int(input("Enter Table Number: "))
                restaurant.reserve_at_beginning(table)
                print(Fore.GREEN + "Table Reserved Successfully.")

            elif choice == 2:
                table = int(input("Enter Table Number: "))
                restaurant.reserve_at_end(table)
                print(Fore.GREEN + "Table Reserved Successfully.")

            elif choice == 3:
                table = int(input("Enter Table Number: "))
                pos = int(input("Enter Position: "))
                restaurant.reserve_at_position(table, pos)
                print(Fore.GREEN + "Table Reserved Successfully.")

            elif choice == 4:
                restaurant.cancel_beginning()
                print(Fore.RED + "First Reservation Cancelled.")

            elif choice == 5:
                restaurant.cancel_end()
                print(Fore.RED + "Last Reservation Cancelled.")

            elif choice == 6:
                pos = int(input("Enter Position to Cancel: "))
                restaurant.cancel_position(pos)
                print(Fore.RED + "Reservation Cancelled.")

            elif choice == 7:
                restaurant.display_tables()

            elif choice == 8:
                table = int(input("Enter Table Number to Search: "))

                if restaurant.search_table(table):
                    print(Fore.GREEN + "Table Reservation Found.")
                else:
                    print(Fore.RED + "Table Reservation Not Found.")

            elif choice == 9:
                print(Fore.MAGENTA +
                      f"Total Reservations: {restaurant.total_reservations()}")

            elif choice == 10:
                print(Fore.YELLOW + "Thank You for Visiting Our Restaurant!")
                break

            else:
                print(Fore.RED + "Invalid Choice.")

        except ValueError:
            print(Fore.RED + "Please Enter a Valid Integer.")

        except IndexError as e:
            print(Fore.RED + str(e))

        except Exception as e:
            print(Fore.RED + str(e))

        time.sleep(1)


if __name__ == "__main__":
    main()
