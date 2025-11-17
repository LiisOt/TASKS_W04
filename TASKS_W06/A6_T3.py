def main():
    print("Program starting.")
    print("This program can copy a file.")

    source_file = input("Insert source filename: ")             # Kysytään lähdetiedoston nimi
    destination_file = input("Insert destination filename: ")   # Kysytään kohdetiedoston nimi

    print(f"Reading file '{source_file}' content.")
    with open(source_file, "r", encoding="UTF-8") as f:         # Avataan lähdetiedosto lukutilassa.  "r" = "read"
        content = f.read()                                      # Luetaan koko tiedoston sisältö muuttujaan content
    print("File content ready in memory.")

    print(f"Writing content into file '{destination_file}'.")
    with open(destination_file, "w", encoding="UTF-8") as f:    # Avataan kohdetiedosto kirjoitustilassa.  "w" = "write"
        f.write(content)                                        # Kirjoitetaan sisältö kohdetiedostoon
    print("Copying operation complete.")

    print("Program ending.")

if __name__ == "__main__":
    main()