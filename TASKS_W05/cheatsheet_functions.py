# def greet(name):
#     print(f"Hello {name}")

# greet("Liis")

# def greet(name):
#     return f"Hello, {name}"

# print(greet("Liis"))

# def greeting_airport(person, age):
#     print(f"How do you do {person}")
#     if age >= 18:
#         print("Welcome to your flight")
#     else:
#         print(f"You need to wait for {18-age} years to flight solo.")

# greeting_airport("Liis", 34) 

# def initialize():
#     print("Initializing resources...")
# def process_data(data):
#     return data.upper()
# def save_results(results):
#     print(f"Saving results: {results}")

# def main():
#     initialize()
#     data = "sample data"
#     processed_data = process_data(data)
#     save_results(processed_data)

# main()

def displayMenu() -> None:
    print("Menu:")
    print("1 -  View balance")
    print("2 - Deposit balance")
    print("3 - Withdraw money")
    print("0 - Exit")
    return None

def getUserChoice() -> int:
    userInput = input("Enter your choice: ")
    return int(userInput)

def main() -> None:
    print("Welcome to the bank app...")
    choice = -1
    while choice != 0:
        displayMenu()
        choice = getUserChoice()
    return None

main()

