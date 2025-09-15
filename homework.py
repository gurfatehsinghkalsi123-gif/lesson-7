# Get input from user
char = input("Enter a single character: ")

# Check if only one character is entered
if len(char) == 1:
    # Get ASCII value using ord()
    ascii_value = ord(char)
    print(f"The ASCII value of '{char}' is {ascii_value}.")
else:
    print("Please enter exactly one character.")
