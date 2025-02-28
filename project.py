import random
import csv

def main():
    startup()

    if not check_master_password():
        print("Exiting...")
        return

    passwords = load_passwords()

    while True:
        print("\nOptions:")
        choice = input("1. Generate and store new password\n"
                       "2. Store a password\n"
                       "3. Delete a password\n"
                       "4. View all Passwords\n"
                       "5. Quit\n"
                       "Enter your choice (1-5): ")

        if choice == '1':
            service = input("What website is this password used for?: ").strip()
            if service in passwords:
                print("Website already exists!")
                continue
            password = generate_password()
            print(f"Generated password: {password}")
            passwords[service] = password
            save_passwords(passwords)

        elif choice == '2':
            service = input("What website is this password used for?: ").strip()
            password = input("Enter password: ").strip()
            passwords[service] = password
            save_passwords(passwords)

        elif choice == '3':
            service = input("Enter website to delete password: ").strip()
            if service in passwords:
                del passwords[service]
                save_passwords(passwords)
                print("Website deleted")
            else:
                print("Website not found")

        elif choice == '4':
            if passwords:
                print("\nStored Passwords:")
                for service, pwd in passwords.items():
                    print(f"{service}: {pwd}")
            else:
                print("No passwords stored")

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-5.")

def startup():
    print("Hi user! Welcome to your password storage.")

def check_master_password(master_file='master_password.txt'):
    try:
        with open(master_file, 'r') as f:
            stored_password = f.read().strip()
    except FileNotFoundError:
        create_master_password(master_file)
        with open(master_file, 'r') as f:
            stored_password = f.read().strip()

    attempts = 3
    while attempts > 0:
        entered = input("Enter master password: ")
        if entered == stored_password:
            return True
        attempts -= 1
        print(f"Incorrect password. {attempts} attempts remaining.")

    print("Too many failed attempts.")
    return False

def create_master_password(master_file='master_password.txt'):
    print("First-time setup: Create a master password")
    while True:
        master = input("Create master password: ")
        confirm = input("Confirm master password: ")
        if master == confirm:
            break
        print("Passwords don't match. Try again.")

    with open(master_file, 'w') as f:
        f.write(master)
    print("Master password created.")

def generate_password(length=12):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*'
    password = ''
    for _ in range(length):
        random_char = random.choice(chars)
        password += random_char
    return password

def load_passwords(passwords_file='passwords.csv'):
    passwords = {}
    try:
        with open(passwords_file, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 2:
                    service, pwd = row
                    passwords[service] = pwd
    except FileNotFoundError:
        pass
    return passwords

def save_passwords(passwords, passwords_file='passwords.csv'):
    with open(passwords_file, 'w', newline='') as f:
        writer = csv.writer(f)
        for service, pwd in passwords.items():
            writer.writerow([service, pwd])

if __name__ == "__main__":
    main()
