import getpass
import hashlib
def getpassword(text):
    return hashlib.sha256(text.encode(encoding="utf-8")).hexdigest()
operation = str(input("Press 1 to create an account and 2 to log in: "))
if operation == "1":
    username = f"{str(input('Select username: '))}.txt"
    try:
        with open(username) as file:
            print("User already exists!")
    except FileNotFoundError:
        with open(username, "w") as file:
            file.write(getpassword(getpass.getpass(prompt='Set a password: ')))
elif operation == "2":
    username = f"{str(input('Enter username: '))}.txt"
    try:
        with open(username) as file:
            if getpassword(getpass.getpass(prompt='Enter password: ')) == file.read():
                print("Welcome!")
            else:
                print("Wrong password.")
    except FileNotFoundError:
        print("User does not exist!")
else:
    print("Incorrect option!")