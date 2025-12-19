# Not commented as this is a cleanup of an old project.

import turtle as osu
import random as rng

score = ""

try:
    with open("score.txt", 'r') as file:
        for line in file:
            score = int(line.strip())
except FileNotFoundError:
    print("Debug: File not found, creating new score.txt file")
    with open("score.txt", "w") as file:
        file.write("0")
    with open("score.txt", 'r') as file:
        for line in file:
            score = int(line.strip())

print(f"Debug: Starting with imported score {score}")

def logout():
    global score
    with open("score.txt", "w") as file:
        file.write(str(score))
    print(f"Debug: Exiting with final score {score}")
    wn.bye()

def update_scoreboard():
    scoreboard.clear()
    scoreboard.write(f"Score: {score}", move=False, align='left', font=('Arial', 10, 'normal'))

def clicked(x, y):
    global score
    score = score + 1
    print(f"Debug: Turtle clicked at ({x}, {y})")
    clone = target.clone()
    targetcol = rng.randint(0, 5)
    if targetcol == 0:
        clone.color("red")
    elif targetcol == 1:
        clone.color("yellow")
    elif targetcol == 2:
        clone.color("blue")
    elif targetcol == 3:
        clone.color("green")
    elif targetcol == 4:
        clone.color("purple")
    elif targetcol == 5:
        clone.color("orange")
    else:
        print(f"Debug: Color out of range ({targetcol})")
    target.goto(rng.randint(-250, 250), rng.randint(-250, 250))
    update_scoreboard()

wn = osu.Screen()
wn.title("Turtle Clicker")
wn.bgcolor("white")
wn.setup(width=512, height=512)

scoreboard = osu.Turtle()
scoreboard.penup()
scoreboard.speed(0)
scoreboard.goto(-250, -245)
scoreboard.hideturtle()
update_scoreboard()

wn.onkey(logout, "Return")
wn.listen()

target = osu.Turtle()
target.shape("turtle")
target.color("black")
target.speed(0)
target.penup()
target.goto(0,0)
target.onclick(clicked, btn=1)

wn.mainloop()