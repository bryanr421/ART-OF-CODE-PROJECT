import turtle

turtle.bgcolor("red")

bob = turtle.Turtle()
bob.speed(0)  
bob.width(2)



def spral():
    bob.color("blue")
    bob.begin_fill()
    for times in range(70):
        bob.circle(times * 6)
        bob.forward(times * 2)
        bob.right(25)
    bob.end_fill()

def drawfinsih():
    turtle.done()

