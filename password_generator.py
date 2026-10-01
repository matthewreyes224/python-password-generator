import string
import secrets


lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

character_pool = lowercase + uppercase + numbers + symbols


def generate_password(length):
    password = ""

    for _ in range(length):
        password += secrets.choice(character_pool)

    return password


running = True

while running:
    print("\n=== Password Generator ===\n")
    print("Please choose an option below:\n")
    print("1. Generate 15 Character Password")
    print("2. Generate Custom Length Password")
    print("3. Exit")

    choice = input("\nPlease choose 1, 2, or 3: ").strip()

    if choice == "1":
        length = 15

    elif choice == "2":
        try:
            length = int(input("How many characters do you want your password to be? "))

            if length < 15:
                print("Please choose a password length of at least 15 characters.")
                continue

        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

    elif choice == "3":
        print("Exiting Password Generator.")
        running = False
        continue

    else:
        print("Invalid option. Please pick option 1, 2, or 3.")
        continue

    password = generate_password(length)
    print(f"\nYour password is: {password}")

    again = input("\nWould you like to generate another password? (y/n): ").strip().lower()

    if again != "y":
        running = False
        print("Exiting Password Generator.")
