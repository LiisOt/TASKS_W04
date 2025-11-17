SEPARATOR = ";"

def readValues(filename: str) -> str:
    numbers = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.isdigit():
                    numbers.append(line)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return SEPARATOR.join(numbers)

def analyseValues(values: str) -> str:
    if not values:
        return "Count;Sum;Greatest;Average\n0;0;0;0.00\n"
    
    nums = [int(n) for n in values.split(SEPARATOR)]
    count = len(nums)
    total = sum(nums)
    greatest = max(nums)
    average = total / count if count > 0 else 0
    # Tagastab täpselt kahe reaga CSV stringi ja ühe lõppreaga
    return f"Count;Sum;Greatest;Average\n{count}{SEPARATOR}{total}{SEPARATOR}{greatest}{SEPARATOR}{average:.2f}\n"

def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    print("#### Number analysis - START ####")
    values = readValues(filename)
    result = analyseValues(values)
    print(result, end="")  # ei lisa täiendavat reavahet
    print("#### Number analysis - END ####")
    print("Program ending.")

if __name__ == "__main__":
    main()
