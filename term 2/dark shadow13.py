import turtle as tr
import random as rnd


tr.speed(500)


for j in range(100):
    tr.penup()
    x_position = rnd.randint(-200, 200)
    y_position =rnd.randint(-150, 150)
    tr.goto(x_position,y_position)
    tr.pendown()
    

tr.done()
pen_size = rnd .randint(1, 5)
tr.pensize(pen_size)
for i in range(4):
    tr.fd(150)
    tr.lt(120)
tr.done()
