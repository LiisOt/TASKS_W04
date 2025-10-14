print("Program starting.")
print("")
WordCount = 0
CharCount = 0

Word = input("Insert word (empty stops): ")
while Word != '': #Toistaa niin kauan kuin käyttäjä ei paina enteriä
    WordCount += 1 #Laskee sanojen määrän
    CharCount += len(Word) #Laskee merkkien määrän
    Word = input("Insert word (empty stops): ")
print("")
print("You inserted:")
print(f"{WordCount} words")
print(f"{CharCount} characters")
print("")
print("Program ending.")