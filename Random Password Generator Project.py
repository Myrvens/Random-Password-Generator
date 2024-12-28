import random
import string

# Define available characters for the password
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("How long would you like your password to be? "))
    
    # Shuffle the characters to ensure randomness
    random.shuffle(characters)
    
    # Generate password
    password = []
    for _ in range(password_length):
        password.append(random.choice(characters))
    
    # Shuffle the password and join it as a string
    random.shuffle(password)
    password = "".join(password)
    
    print(password)

# Prompt user to generate a password
option = input("Do you want to generate a password? (Yes/No): ")

if option == "Yes":
    generate_password()
elif option == "No":
    print("Program ended")
    quit()
else:
    print("Invalid input. Please enter Yes or No.")
