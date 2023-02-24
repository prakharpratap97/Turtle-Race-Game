from turtle import *
from random import randint
import time

# Countdown
for i in range(3, 0, -1):
    goto(0, 0)
    write(str(i), align='center', font=('Arial', 48, 'normal'))
    time.sleep(1)
    clear()

write("Get set...", align='center', font=('Arial', 48, 'normal'))
time.sleep(1)

clear()

write("Go!", align='center', font=('Arial', 48, 'normal'))
time.sleep(1)

clear()

# Set up the screen
speed(100)
penup()
goto(-140, 140)

# Draw the race track
for checkpoint in range(15):
    write(checkpoint, align='center')
    right(90)
    for num in range(8):
        penup()
        forward(10)
        pendown()
        forward(10)
    penup()
    backward(160)
    left(90)
    forward(20)

# Create the turtles
flash = Turtle()
flash.color('red')
flash.shape('turtle')
flash.penup()
flash.goto(-160, 100)

quicksilver = Turtle()
quicksilver.color('blue')
quicksilver.shape('turtle')
quicksilver.penup()
quicksilver.goto(-160, 70)

bolt = Turtle()
bolt.color('green')
bolt.shape('turtle')
bolt.penup()
bolt.goto(-160, 40)

# Start the race
for turn in range(110):
    flash.forward(randint(1, 5))
    quicksilver.forward(randint(1, 5))
    bolt.forward(randint(1, 5))

# Determine the winners
winners = [(flash.position()[0], "Flash"), (quicksilver.position()[0], "Quicksilver"), (bolt.position()[0], "Bolt")]
winners.sort(reverse=True)

# Print the winners' positions and names
for i, winner in enumerate(winners):
    goto(-150, -50 - i*20)
    write(f"{i+1}. {winner[1]} - {winner[0]:.2f}", align='left', font=('Arial', 12, 'normal'))

hideturtle()

# Wait for 10 seconds before closing the window
time.sleep(10)

done()
