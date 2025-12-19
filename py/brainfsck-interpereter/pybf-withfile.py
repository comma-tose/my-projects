# Sets up the array, pointer, and instruction tracker
array = []
pointer = 0
instruction = 0
for i in range(30000):
    array.append(0)

# The code is the code.bf code in the current directory. Default code included with repository is a simple "Hello, world!"
try:
    with open("code.bf", "r") as file:
        program = file.read()
except FileNotFoundError:
    print("No file!")
    exit()

# Moves to the next instruction
def increment():
    global instruction
    instruction = instruction + 1

# Adds 0x01 to the current cell
def plus():
    global array
    array[pointer] = array[pointer] + 1
    if array[pointer] == 256:
        array[pointer] = 0

# Subtracts 0x01 from the current cell
def minus():
    global array
    array[pointer] = array[pointer] - 1
    if array[pointer] == -1:
        array[pointer] = 255

# Moves the pointer left
def left():
    global pointer
    pointer = pointer - 1
    if pointer == -1:
        pointer = 0

# Moves the pointer right
def right():
    global pointer
    pointer = pointer + 1
    if pointer > len(array) or pointer == len(array):
        pointer = len(array) - 1

# Writes the current cell's ASCII value to bfout.txt
def period():
    with open("bfout.txt", "a") as file:
        file.write(chr(array[pointer]))

# Gets input from the user. Input is an integer, and not the character itself.
def comma():
    global array
    while True:
        try:
            to_enter = int(input("Input requested: "))
            if to_enter > -1 and to_enter < 256:
                array[pointer] = to_enter
                break
        except ValueError:
            pass

# Writes the current array to array.txt
def writearray():
    with open("array.txt", "w") as file:
        for i in range(0, len(array)):
            file.write(f"{array[i]}\n")

""" Loops
This was the hardest part to code by far.
Works like this:
1. Notes the current instruction for going back to.
2. Checks if the current instruction is a loop break.
2a. If it is, and the current cell is 0x00, then the loop breaks.
2b. if it is, but the current cell is not 0x00, the pointer returns to the start of the loop.
2c. If it is not, the program continues to run as normal.
3. IndexError is used to check if the end of the code has been reached.
"""
def loop():
    global instruction
    increment()
    returnto = instruction
    try:
        while True:
            if program[instruction] == "]":
                if array[pointer] == 0:
                    break
                else:
                    instruction = returnto
            else:
                eval()
    except IndexError:
        print("Code completed.")
        writearray()
        exit()

# Performs one step of code, simple as that. IndexError is used to check if the end of the code has been reached.
def eval():
    try:
        if program[instruction] == "+":
            plus()
            increment()
        elif program[instruction] == "-":
            minus()
            increment()
        elif program[instruction] == "<":
            left()
            increment()
        elif program[instruction] == ">":
            right()
            increment()
        elif program[instruction] == ".":
            period()
            increment()
        elif program[instruction] == ",":
            comma()
            increment()
        elif program[instruction] == "[":
            if array[pointer] == 0:
                increment()
            else:
                loop()
        else:
            increment()
    except IndexError:
        print("Code completed.")
        writearray()
        exit()

# Starts the code.
while True:
    eval()