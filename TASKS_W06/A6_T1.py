def read_file(filename): 
    file = open(filename, "r") # Open the file in read mode
    content = ''    # Read the content of the file
    row = file.readline()  # Read a single line from the file
    while row != "":      # Loop until the end of the file
        content += row  # Append the line to content
        row = file.readline()  # Read the next line
    file.close()  # Close the file
    return content # Return the content of the file

def main() -> None:
    print("Program starting.")
    print("This program can read a file.")
    filename = input("Insert filename: ")
    fileContent = read_file(filename) # Call the read_file function
    print(f"#### START '{filename}' ####")
    print(fileContent)  # Print the content of the file
    print(f"#### END '{filename}' ####")
    print("Program ending.")
    return None

if __name__ == "__main__":
        main()
