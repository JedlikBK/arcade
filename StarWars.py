import turtle
import time
import random


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
space.addshape("meteor2.gif")
space.tracer(0)

space.listen()

space.onkeypress(fel, "Up")
space.onkeypress(le, "Down")
space.onkeypress(jobbra, "Left")
space.onkeypress(balra, "Right")

urhajo = turtle.Turtle()
urhajo.shape("sprite.gif")
urhajo.penup()

meteor = turtle.Turtle()
meteor.shape("meteor2.gif")
meteor.setx(750)
meteor.sety(random.uniform(-300, 300))
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

    meteor.setx(meteor.xcor()-30)
    if meteor.xcor() < -400:
        meteor.setx(750)
        meteor.sety(random.uniform(-300, 300))
