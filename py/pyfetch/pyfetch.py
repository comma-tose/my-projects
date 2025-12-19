# This program was inspired by the program Neofetch.
# However, it does not use code from it.

# info_values is used for the changing output of each value in the fetch.
# All values in info_values are stored as f-strings to prevent them from being truncated as integers or floats.
# info_index is used for the not-changing definition of each value

import platform # Used for the majority of the code
import getpass # Used for the current user in the header
import os # Used for the logical processors value

# The logo's ASCII art, saved as a list with each entry being one value. Will be important later.
logo = ["XXXXXXXXXXXXXXXXX", "XXXXXXXXXXXXXXXXX", "XXXXXXXXXXXXXXXXX", "XXXXXXXXXXXXXXXXX", "XXXXXXXXXXXXXXXXX", "XXXXXXXXXXXXXXXXX", "XXXXXXXXXXXXXXXXX", "XXXXXXXXXXXXXXXXX"] 

# Defines these two variables as lists
info_values = []
info_index = []

# user@hostname
info_values.append(f"@{platform.node()}") 
info_index.append(f"{getpass.getuser()}")

# Separator bar
info_values.append("----------------")
info_index.append("----------------")

# Operating system
info_values.append(f"{platform.system()}")
info_index.append(f"Operating system: ")

# OS release
info_values.append(f"{platform.release()}")
info_index.append("Platform release: ")

# Shows Linux distro if Linux, Windows version (Home, LTSC, Education, etc.) if Windows, and a placeholder if anything else.
if "Linux" in platform.system():
    info_values.append(f"{platform.freedesktop_os_release()}")
    info_index.append("Linux distribution: ")
elif "Windows" in platform.system():
    info_values.append(f"{platform.win32_edition()}")
    info_index.append("Windows edition: ")
else:
    info_values.append("No additional info available")
    info_index.append("OS info: ")

# CPU Architecture (Usually AMD64)
info_values.append(f"{platform.machine()}")
info_index.append("CPU architecture: ")

# Logical processor count (Not core count)
info_values.append(f"{os.cpu_count()}")
info_index.append("Logical processors: ")

# Python version
info_values.append(f"{platform.python_version()}")
info_index.append("Python version: ")

# Prints the ith segment of the ASCII art, then the item, then its value.
for i in range(len(info_values)):
    print(f"{logo[i]}   {info_index[i]}{info_values[i]}")

# Separator bar at the end
print("----------------------------------------------------")

#   Unused (And now broken) code to print the logo
#for i in range(8):
#    print(logo[i])

# TODO - my todo list for this project
# Get Platform info (DONE)
# Apologize to Aiden
# Write makefile

# Polish
