print("Program starting.")
print("")
PointStart = int(input("Insert starting point: "))
PointStop = int(input("Insert stopping point: "))
PointInspect = int(input("Insert inspection point: "))
print("")

Run = True

if(PointStart >= PointStop):
    print("Starting point value must be less than the stopping point value.")
    Run = False
if(PointStart > PointInspect or PointInspect > PointStop):
    print("Inspection value must be within the range of start and stop.")
    Run = False

if(Run):
    print("First loop - inspection with break:")
    for i in range(PointStart, PointStop):
        if(i == PointInspect):
            break
        else:
            print(i, end=" ")
    print("")
    print("Second loop - inspection with continue:")
    for i in range(PointStart, PointStop):
        if(i == PointInspect):
            continue
        else:
            if(i == PointStop-1):
                print(i)
            else:
                print(i, end=" ")
print("Program ending.")