import turtle
shelly=turtle.Turtle()
colors=['blue','green','purple', 'white']

turtle.bgcolor('black')

for i in range(12):
    for i in range(4):
        shelly.color(colors[i])
        shelly.forward(100)
        shelly.left(90)
    shelly.right(60)
shelly.penup()
shelly.color('red')

for i in range(6):
    shelly.forward(180)
    shelly.pendown()
    shelly.circle(5)
    shelly.penup()
    shelly.backward(180)
    shelly.right(60)
shelly.hideturtle()
    
    
