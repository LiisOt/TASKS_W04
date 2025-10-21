def frameWord(Pword):
    print("*" *(len(Pword)+4))
    print(f"* {Pword} *")
    print("*" *(len(Pword)+4))
    return None

def main():
    print("Program starting.")
    Pword = input("Insert word: ")
    print("")
    frameWord(Pword)
    print("")
    print("Program ending.")
    return None

main()