LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SHIFT = 13  # ROT13

# Function to shift a single character
def shiftCharacter(char, alphabet):
    if char in alphabet:
        idx = alphabet.index(char)
        return alphabet[(idx + SHIFT) % 26]
    return char

# ROT13 function for full string
def rot13(text):
    result = []
    for c in text:
        if c.islower():
            result.append(shiftCharacter(c, LOWER_ALPHABETS))
        elif c.isupper():
            result.append(shiftCharacter(c, UPPER_ALPHABETS))
        else:
            result.append(c)
    return ''.join(result)

# Write content to file
def writeFile(filename, content):
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(content)

# Main program
def main():
    print("Program starting.")
    print("\nCollecting plain text rows for ciphering.")

    rows = []
    while True:
        row = input("Insert row(empty stops): ")
        if row == "":
            break
        rows.append(row)

    ciphered_rows = [rot13(r) for r in rows]

    print("\n#### Ciphered text ####")
    for r in ciphered_rows:
        print(r)

    choice = input("\nDo you want to save the ciphered text? (y/n): ")
    if choice.lower() == 'y':
        filename = input("Insert filename to save: ")
        writeFile(filename, '\n'.join(ciphered_rows) + '\n')
        print("Ciphered text saved!")

    print("Program ending.")

if __name__ == "__main__":
    main()
