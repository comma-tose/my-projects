# Not commented as this is a cleanup of an old project.
print("This script allows you to check if a Windows 95 key is a valid key. This works because Windows 95 keys are checked using a series of mathematical algorithms. If you have a retail key, it should look like XXX-XXXXXXX, and if you have an OEM key, it should look like XXXXX-OEM-XXXXXXX-XXXXX.")
print("You can exit this program at any time by pressing Ctrl + Z followed by Enter.")

def retail():
    licensekey = str(input("Please enter your retail key: "))
    if len(licensekey) == 11 and licensekey[3] == "-":
        licensekey1 = int(licensekey[:3])
        licensekey2 = str(licensekey[4:])
        if licensekey1 == 333 or licensekey1 == 444 or licensekey1 == 555 or licensekey1 == 666 or licensekey1 == 777 or licensekey1 == 888 or licensekey1 == 999:
                print("Sorry, your retail key is not valid. The first three digits of a retail key cannot be 333, 444, 555, 666, 777, 888, or 999.")
        else:
            if (int(licensekey2[0]) + int(licensekey2[1]) + int(licensekey2[2]) + int(licensekey2[3]) + int(licensekey2[4]) + int(licensekey2[5]) + int(licensekey2[6]))%7 == 0 and not "9" in str(licensekey2):
                    print(f"Your retail key {licensekey} is valid!")
            else:
                print("Sorry, your retail key is not valid. The last seven of a retail key digits cannot contain 9, and the sum of the digits divided by 7 must not leave a remainder.")
    else:
        print("You entered your key in an invalid format, or you didn't enter a key at all.")

def oem():
    licensekey = str(input("Please enter your OEM key: "))
    print(len(licensekey), licensekey[5:10], licensekey[17], licensekey[3:5], licensekey[:3])
    if len(licensekey) == 23 and licensekey[5:10] == "-OEM-" and licensekey[17] == "-":
        licensekey1 = int(licensekey[:3])
        licensekey2 = int(licensekey[10:17])
        licensekey3 = int(licensekey[3:5])
        if licensekey1 > 366:
                print("Sorry, your OEM key is not valid. The first three digits of an OEM key must be less than 366.")
        else:
            if licensekey3 < 4 or licensekey3 > 94:
                if licensekey2%7 == 0 and not "9" in str(licensekey2):
                        print(f"Your OEM key {licensekey} is valid!")
                else:
                    print("Sorry, your OEM key is not valid. The last seven of an OEM key digits cannot contain 9, and the sum of the digits divided by 7 must not leave a remainder.")
            else:
                print("Sorry, your OEM key is not valid. The fourth and fifth digits of an OEM key must be greater than 93 or less than 05.")
    else:
        print("You entered your key in an invalid format, or you didn't enter a key at all.")

def wip():
    print("Windows 95 OEM keys are still a work in progress.")
    print("Since I am no longer developing this, the OEM key checker is essensially broken.")
    oem()

while True:
    key_type = str(input("Do you have an OEM key or a retail key? "))
    key_type = key_type.lower()
    if key_type == "retail":
        retail()
    elif key_type == "oem":
        wip()
    else:
        print("You entered an invalid option, please try again.")