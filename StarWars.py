import turtle, random, time



def fel():
    ypos = urhajo.ycor()   
    ypos += 10
    urhajo.sety(ypos)
    
def le():
    ypos = urhajo.ycor()   
    ypos -= 10
    urhajo.sety(ypos)

def balra():
    xpos = urhajo.xcor()   
    xpos += 10
    urhajo.setx(xpos)

def jobbra():
    xpos = urhajo.xcor()   
    xpos -= 10
    urhajo.setx(xpos)

space = turtle.Screen()
space.setup(width=800, height=600)
space.bgpic("background.png")
space.addshape("sprite.gif")
space.tracer(0)

space.listen()

space.onkey(fel,"Up")
space.onkey(le,"Down")
space.onkey(jobbra,"Left")
space.onkey(balra,"Right")

urhajo = turtle.Turtle()
urhajo.shape("sprite.gif")
urhajo.penup()

while True:
    space.update()
    time.sleep(0.2)
    if urhajo.xcor() > 400:
        urhajo.setx(-400)

    if urhajo.xcor() < -400:
        urhajo.setx(400)

    if urhajo.ycor() > 300:
        urhajo.sety(-300)

    if urhajo.ycor() < -300:
        urhajo.sety(300)
