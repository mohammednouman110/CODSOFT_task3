import random
import string

# ------------------------------------
# List to store generated passwords
# ------------------------------------
password_history = []

# ------------------------------------
# Function to generate password
# ------------------------------------
def generate_password(length):
    characters = (
        string.ascii_uppercase +   # A-Z
        string.ascii_lowercase +   # a-z
        string.digits +            # 0-9
        string.punctuation         # special characters
    )

    password = ""
    for _ in range(length):
        password += random.choice(characters)

    return password


# ------------------------------------
# Function to display menu
# ------------------------------------
def show_menu():
    print("\n====== PASSWORD GENERATOR MENU ======")
    print("1. Generate Password")
    print("2. Generate Multiple Passwords")
    print("3. List Generated Passwords")
    print("4. Exit")
    print("====================================")


# ------------------------------------
# Function to list stored passwords
# ------------------------------------
def list_passwords():
    if not password_history:
        print("No passwords generated yet.")
    else:
        print("\nSaved Passwords:")
        for i, pwd in enumerate(password_history, 1):
            print(f"{i}. {pwd}")


# ------------------------------------
# Main Program
# ------------------------------------
while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    # Option 1: Single password
    if choice == "1":
        try:
            length = int(input("Enter password length: "))
            if length <= 0:
                print("Password length must be greater than 0.")
            else:
                password = generate_password(length)
                password_history.append(password)
                print("Generated Password:", password)
        except ValueError:
            print("Please enter a valid number.")

    # Option 2: Multiple passwords
    elif choice == "2":
        try:
            count = int(input("How many passwords to generate? "))
            length = int(input("Enter password length: "))

            if count <= 0 or length <= 0:
                print("Values must be greater than 0.")
            else:
                print("\nGenerated Passwords:")
                for i in range(count):
                    pwd = generate_password(length)
                    password_history.append(pwd)
                    print(f"{i+1}. {pwd}")
        except ValueError:
            print("Please enter valid numeric values.")

    # Option 3: List passwords
    elif choice == "3":
        list_passwords()

    # Option 4: Exit
    elif choice == "4":
        print("Thank you for using Password Generator!")
        break

    # Invalid choice
    else:
        print("Invalid choice! Please select 1–4.")
