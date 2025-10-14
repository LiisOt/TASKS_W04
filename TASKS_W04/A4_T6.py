print("Program starting.")
Number = int(input("Insert a positive integer: "))
steps = 0
sequence = [Number]
while Number != 1:
    if Number % 2 == 0:
        Number = Number // 2 
    else:
        Number = 3 * Number + 1
    sequence.append(Number)

    steps +=1
print(f" -> ".join(str(Number) for Number in sequence))

print(f"Sequence had {steps} total steps.\n")

print("Program ending.")
