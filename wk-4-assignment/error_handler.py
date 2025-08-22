# error_handler.py

# Ask user for filename
filename = input("Enter filename to read: ")

# Try to open and read the file
try:
    with open(filename, 'r') as file:
        content = file.read()
        print("File contents:")
        print(content)

except FileNotFoundError:
    print(f"Error: Sorry, '{filename}' was not found!")
    
except PermissionError:
    print(f"Error: Can't read '{filename}' - permission denied!")
    
except Exception as e:
    print(f"Error: Something went wrong - {e}")