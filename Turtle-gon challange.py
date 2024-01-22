import turtle
bob=turtle.Turtle()

a=int(input("How many sides"))
for i in range(a):
    bob.forward(100)
    bob.right(360/a)
turtle.exitonclick()