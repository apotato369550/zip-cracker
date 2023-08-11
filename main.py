import zipfile
import os

# john the ripper run dir: ".\john-1.9.0-jumbo-1-win64\run"

# function to crack .zip files
def crack_zip_file(file_name):
    # Attempts to bruteforce the file's password using 'rockyou.txt'
    zip_file = zipfile.ZipFile("super-secret-info.zip")

    # Iterates through lines found in 'rockyou.txt'
    with open("rockyou.txt", "r") as file:
        for line in file:
            line = line.strip()
            print("Attempting password: ", line)
            try:
                zip_file.extractall(pwd=line.encode())
                print("Password found: ", line)
                break
            except Exception as e:
                continue
    return

# function to crack .rar files
def crack_rar_file(file_name):
    print("(This application is currently unable to crack .rar files, please come back again some other time.)")
    return

# mainloop of program
def main():
    # enter mainloop where user chooses to start or to exit
    while True:
        print("Welcome to zip-cracker!")
        print("[start] Get crackin'")
        print("[exit] Exit application")

        choice = input("Enter your [choice]: ").strip().lower()

        if choice == "start":
            # have user enter the name of the .zip/.rar file to be cracked
            file_name = input("Enter the path of a .zip or .rar file (or 'exit' to quit): ").strip()

            if file_name.lower() == "exit":
                print("Exiting the file selection system.")
                break

            if not os.path.exists(file_name):
                print("Error: The specified file does not exist.")
                continue

            if file_name.lower().endswith(".zip"):
                crack_zip_file(file_name)
            elif file_name.lower().endswith(".rar"):
                crack_rar_file(file_name)
            else:
                print("Error: Unsupported file format. Please enter a .zip or .rar file.")

        elif choice == "exit":
            # exit the program if user enters exit
            print("Exiting the application.")
            break
        else:
            # tell the user to enter either 'start' or 'exit' if he messes up the input
            print("Error: Invalid input. Please enter either 'start' or 'exit'.")

if __name__ == "__main__":
    main()

