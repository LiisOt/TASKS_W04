def write_file(content, file_name):
    file = open(file_name, "w")  # Open the file in write mode
    file.write(content)  # Write the names to the file
    file.close()  # Close the file
    return None

def main():
    print("Program starting.")
    first_name = input("Insert first name: ")
    last_name = input("Insert last name: ")
    file_name = input("Insert filename: ")
    content = "{}\n{}".format(first_name, last_name) # Prepare content to write
    write_file(content, file_name) # Call the function to write to file
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()