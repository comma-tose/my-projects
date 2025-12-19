# Not commented as this is a cleanup of an old project.

# Simple tool for 0x0.st file uploads.
# Requires curl

import os

if input("Would you like to copy a file from a remote URL instead of uploading a file? (Y/N) ").lower() == "y":
    file = f"url={input("Enter the URL to copy from: ")}"
else:
    file = f"file=@{input("Enter the file path: ")}"

if input("Would you like to generate a longer and harder to guess URL? (Y/N) ").lower() == "y":
    secret = True
else:
    secret = False

if input("Would you like to set an expiration date? (Y/N) ").lower() == "y":
    try:
        expires = int(input("You can use hours since upload or milliseconds since the UNIX epoch.\nExpiration date: "))
    except ValueError:
        print("Invalid time. You can only use integers. Not setting an expiration date...")
        expires = False
else:
    expires = False

if expires == False:
    if secret == True:
        os.system(f"curl --user-agent \"0x0st-py\" -F'{file}' -Fsecret= http://0x0.st")
    else:
        os.system(f"curl --user-agent \"0x0st-py\" -F'{file}' http://0x0.st")
else:
    if secret == True:
        os.system(f"curl --user-agent \"0x0st-py\" -F'{file}' -Fexpires={expires} -Fsecret= http://0x0.st")
    else:
        os.system(f"curl --user-agent \"0x0st-py\" -F'{file}' -Fexpires={expires} http://0x0.st")