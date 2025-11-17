def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")

    filename = input("Insert a filename to read: ")            # Kysytään tiedoston nimi

    print(f'Reading names from "{filename}".')

    with open(filename, "r") as f:                             # Avataan tiedosto lukutilassa.  "r" = "read"
        names = [line.strip() for line in f if line.strip()]   # Luetaan rivit listaan, poistetaan tyhjät välit ja skipataan tyhjät rivit

    print("Analysing names...")

    count = len(names)                                         # Lasketaan nimien määrä

    
    shortest = len(min(names, key = len)) if count > 0 else 0  # Etsitään lyhyin nimi (pituus)
    longest = len(max(names, key = len)) if count > 0 else 0   # Etsitään pisin nimi (pituus)
    average = (sum(len(n) for n in names) / count ) if count > 0 else 0.0  # Lasketaan keskipituus

    print("Analysis complete.")

    report = (                                                 # Muodostetaan raportti
        "#### REPORT BEGIN ####\n"
        f"Name count - {count}\n"
        f"Shortest name - {shortest} chars\n"
        f"Longest name - {longest} chars\n"
        f"Average name - {average:.2f} chars\n"
        "#### REPORT END ####"
    )

    print(report)                                              # Tulostetaan raportti
    print("Program ending.")

if __name__ == "__main__":
    main()

