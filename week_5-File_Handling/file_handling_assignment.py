# file_handling_assignment.py

# File Creation
try:
    with open('my_file.txt', 'w') as file:
        # Writing three lines of text (mix of strings and numbers)
        file.write("This is line 1 with a number: 100\n")
        file.write("This is line 2 with a number: 200\n")
        file.write("This is line 3 with some text and numbers: 300 and more text\n")
    print("File created and initial content written successfully.")

    # File Reading and Display
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print("\nContent of the file after creation:")
        print(content)

    # File Appending
    with open('my_file.txt', 'a') as file:
        file.write("This is an appended line 4\n")
        file.write("This is an appended line 5\n")
        file.write("This is an appended line 6\n")
    print("\nAdditional lines appended successfully.")

    # Reading and displaying content again after appending
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print("\nContent of the file after appending:")
        print(content)

# Error Handling
except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You do not have permission to write to the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("\nExecution of file handling operations is complete.")

