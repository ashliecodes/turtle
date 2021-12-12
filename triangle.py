import turtle
side_length = 200
angle = 120
turtle.color('blue')
for side in range(3):
    turtle.forward(side_length)
    turtle.right(angle)
turtle.done()
import turtle
sides = int(input('Number of sides: '))
angle = 360 / sides
side_length = 60
for side in range(sides):
    turtle.forward(side_length)
    turtle.right(angle)
turtle.done()


