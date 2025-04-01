import time
import pandas

def add():
    print("In add function")
    


def modify():
    print("In modify function")


def remove():
    print("In remove function")


def view():
    print("In view function")


def end():
    print("\nSee ya!\n")
    exit()


def main():
    menu_options = {1: add, 2: modify, 3: remove, 4: view, 5: end}

    choice = -1
    is_choice_valid = False
    while not is_choice_valid:
        # Main menu
        for option in menu_options:
            print(f"{option}. {menu_options[option].__name__.capitalize()}")

        choice = int(input("What do you want to do? "))
        if choice in menu_options:
            is_choice_valid = True
        else:
            print("\nPlease select a valid option.\n")

    menu_options[choice]()

if __name__ == "__main__":
    main()
