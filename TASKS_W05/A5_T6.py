def showOptions():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")


def askChoice():
    choice = input("Your choice: ").strip()
    if choice.isnumeric():
        return int(choice)
    else:
        print("Unknown option!")
        return None
    
def main():
    count = 0
    print("Program starting.")
    while True:
        showOptions()
        choice = askChoice()

        if choice is None:
            continue

        if choice == 1:
            print(f"Current count - {count}")
        elif choice == 2:
            count += 1
            print("Count increased!")
        elif choice == 3:
            count = 0
            print("Cleared count!")
        elif choice == 0:
            print("Exiting program.\n")
            break
        else:
            print("Unknown option!")

  
    print("Program ending.")

main()