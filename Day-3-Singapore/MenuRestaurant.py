
# This code is for the food menu
import shutil

def order(a):
    columns = shutil.get_terminal_size().columns
    print("You ordered ".center(columns)+a.center(columns))


def menu():
    columns = shutil.get_terminal_size().columns
    print("Welcome to the food menu".center(columns))
    print("1. Pizza".center(columns))
    print("2. Burger".center(columns))
    print("3. Pasta".center(columns))
    print("4. French Fries".center(columns))
    print("5. Sandwich".center(columns))
    print("6. Exit".center(columns))
    choice = int(input("Enter your choice: ".center(columns)))
    if choice == 1:
        order("Pizza")
    elif choice == 2:
        order("Burger")
    elif choice == 3:
        order("Pasta")
    elif choice == 4:
        order("French Fries")
    elif choice == 5:
        order("Sandwich")
    elif choice == 6:
        exit()
    else:
        print("Invalid choice")
        
#Calling the main function
menu()
