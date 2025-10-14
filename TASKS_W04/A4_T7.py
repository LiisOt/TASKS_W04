print("Program starting.\n")
print("Check multiplicative persistence.")
Number = int(input("Insert an integer: "))
Steps = 0
while Number >= 10:
    digits = [int(d) for d in str(Number)] 
    print(" * ".join(str(d) for d in digits), end=" = ")

    result = 1
    for d in digits:
        result *=d

    print(result)

    Number = result
    Steps += 1
  

print("No more steps.\n")
print(f"This program took {Steps} step(s)\n")
print("Program ending.")