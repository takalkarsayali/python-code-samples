import  turtle
t = turtle.Turtle()

t.speed(100)
turtle.bgcolor("BLack")
for i in range(300):
    t.color('cyan')
    t.circle(i)
    t.lt(5)

turtle.done()