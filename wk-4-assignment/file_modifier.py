# simple_file_modifier.py

# Ask user for filename
filename = input("Enter filename to read: ")

# Try to read the file
try:
    # Read the file
    with open(filename, 'r') as file:
        content = file.read()
    
    # Modify the content (make it uppercase)
    modified_content = content.upper()
    
    # Write to new file
    new_filename = "modified_" + filename
    with open(new_filename, 'w') as file:
        file.write(modified_content)
    
    print(f"Created {new_filename} successfully!")

except FileNotFoundError:
    print("Sorry, file not found!")
except Exception as e:
    print(f"Error: {e}")