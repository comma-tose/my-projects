"""Summary
Python app for messaging
Primarily a demo
"""

import datetime

blockedUsers = []
allowedUsers = []
publicInbox = "False"
inbox = []
junk = []

try:
    with open("blockedUsers.txt", 'r') as file:
        for line in file:
            blockedUsers.append(line.strip())
except FileNotFoundError:
    pass

try:
    with open("allowedUsers.txt", 'r') as file:
        for line in file:
            allowedUsers.append(line.strip())
except FileNotFoundError:
    pass

try:
    with open("inbox.txt", 'r') as file:
        for line in file:
            inbox.append(line.strip())
except FileNotFoundError:
    pass

try:
    with open("junk.txt", 'r') as file:
        for line in file:
            junk.append(line.strip())
except FileNotFoundError:
    pass

try:
    with open("publicInbox.txt", 'r') as file:
        publicInbox = file.read()
except FileNotFoundError:
    pass

def messageRecieved(message, sender):
    global inbox
    global junk
    if publicInbox == "False":
        if sender in allowedUsers:
            inbox.append(f"({datetime.datetime.now()}) ({sender}): {message}")
        else:
            junk.append(f"({datetime.datetime.now()}) ({sender}): {message}")
    else:
        if sender in blockedUsers:
            junk.append(f"({datetime.datetime.now()}) ({sender}): {message}")
        else:
            inbox.append(f"({datetime.datetime.now()}) ({sender}): {message}")

def printInbox():
    i = 0
    for i in range(len(inbox)):
        print(inbox[i])

def printJunk():
    i = 0
    for i in range(len(junk)):
        print(junk[i])

def newMessage():
    message = str(input("Type your message...\n"))
    sendTo = str(input("Enter recipient: "))
    try:
        if str(input("Press 1 to confirm that you want to send this message: ")) == "1":
            messageRecieved(message, sendTo) # Currently, newMessage is set up so that a written message is sent to yourself with the sender being who you sent it to.
            print("Message sent")
        else:
            print("Cancelled.")
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt: Safely exiting...")
        saveAndExit()

def blockUser():
    global blockedUsers
    try:
        toBlock = str(input("Enter the user to block: "))
        blockedUsers.append(toBlock)
        print(f"Blocked {toBlock}.")
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt: Safely exiting...")
        saveAndExit()

def unblockUser():
    global blockedUsers
    try:
        toUnblock = str(input("Enter the user to unblock: "))
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt: Safely exiting...")
        saveAndExit()
    try:
        blockedUsers.pop(allowedUsers.index(toUnblock))
        print(f"Unbocked {toUnblock}.")
    except ValueError:
        print(f"{toUnblock} is not blocked.")

def allowUser():
    global allowedUsers    
    try:
        toAllow = str(input("Enter the user to allow: "))
        allowedUsers.append(toAllow)
        print(f"Allowed {toAllow}.")
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt: Safely exiting...")
        saveAndExit()

def unallowUser():
    global allowedUsers
    try:
        toUnallow = str(input("Enter the user to unallow: "))
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt: Safely exiting...")
        saveAndExit()
    try:
        allowedUsers.pop(allowedUsers.index(toUnallow))
        print(f"Unallowed {toUnallow}.")
    except ValueError:
        print(f"{toUnallow} is not allowed.")

def saveAndExit():    
    with open("inbox.txt", "w") as file:
        for item in inbox:
            file.write(f"{item}\n")
    with open("junk.txt", "w") as file:
        for item in junk:
            file.write(f"{item}\n")
    with open("publicInbox.txt", "w") as file:
        file.write(str(publicInbox))
    with open("blockedUsers.txt", "w") as file:
        for item in blockedUsers:
            file.write(f"{item}\n")
    with open("allowedUsers.txt", "w") as file:
        for item in allowedUsers:
            file.write(f"{item}\n")
    print("Goodbye!")
    exit()

def mainMenu():
    print("Simple messaging service")
    print("What would you like to do?")
    print(f"(1). View inbox ({len(inbox)} message)")
    print(f"(2). Vew junk mail ({len(junk)} message)")
    print(f"(3). Send a message")
    print(f"(4). Toggle public inbox (Currently {publicInbox})")
    print(f"(5). Block a user ({len(blockedUsers)} blocked users)")
    print(f"(6). Unblock a user ({len(blockedUsers)} blocked users)")
    print(f"(7). Allow a user ({len(allowedUsers)} allowed users)")
    print(f"(8). Unallow a user ({len(allowedUsers)} allowed users)")
    print(f"(9). Empty your inboxes")
    print(f"(0). Safely save and exit")
    choice()

def choice():
    try:
        global publicInbox
        global inbox
        global junk
        option = str(input("Option: "))
        if option == "1":
            printInbox()
        elif option == "2":
            printJunk()
        elif option == "3":
            newMessage()
        elif option == "4":
            if publicInbox == "True":
                publicInbox = "False"
            else:
                publicInbox = "True"
        elif option == "5":
            blockUser()
        elif option == "6":
            unblockUser()
        elif option == "7":
            allowUser()
        elif option == "8":
            unallowUser()
        elif option == "9":
            if str(input("Press 1 to confirm inbox deletion: ")) == "1":
                inbox = []
                junk = []
                print("Inboxes cleared.")
            else:
                print("Cancelled, Inboxes not cleared.")
        elif option == "0":
            saveAndExit()
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt: Safely exiting...")
        saveAndExit()

while True:
    mainMenu()

print("If you are seeing this message the code somehow escaped the program loop.\nThis should not happen. Safely exiting...")
saveAndExit()
