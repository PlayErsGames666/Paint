import turtle

screen = turtle.Screen()
screen.listen()

t = turtle.Turtle()

def forward():
    t.forward(10)

def backward():
    t.backward(10)

def left():
    t.left(90)

def right():
    t.right(90)

screen.onkey(forward, 'w')
screen.onkey(backward, 's')
screen.onkey(left, 'a')
screen.onkey(right, 'd')

screen.mainloop()