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

def robbanas():
        corX = urhajo.xcor()
        corY = urhajo.ycor()
        explosion.setx(corX)
        explosion.sety(corY)
        explosion.showturtle()
        meteor.setx(750)
        meteor.sety(random.randint(-270, 270))


space = turtle.Screen()
space.setup(width=800, height=600)
space.bgpic("background.png")
space.addshape("sprite.gif")
space.addshape("meteor2.gif")
space.addshape("explosion.gif")
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
meteor.sety(random.uniform(-270, 270))
kijelzo = turtle.Turtle()
kijelzo.hideturtle()

explosion = turtle.Turtle()
explosion.shape("explosion.gif")
explosion.shapesize(1, 1, 1)
explosion.hideturtle()

meteorSzamlalo = turtle.Turtle()
meteorSzamlalo.hideturtle()
meteorSzamlalo.penup()
meteorSzamlalo.color("Yellow")
meteorSzamlalo.setx(370)
meteorSzamlalo.sety(250)
szamlalo = 0

eletSzamlalo = turtle.Turtle()
eletSzamlalo.hideturtle()
eletSzamlalo.penup()
eletSzamlalo.color("Red")
eletSzamlalo.setx(-370)
eletSzamlalo.sety(250)
life = 3

while life > 0:
    space.update()
    time.sleep(0.1)
    if urhajo.xcor() > 400:
        urhajo.setx(-400)

    if urhajo.xcor() < -400:
        urhajo.setx(400)

    if urhajo.ycor() > 300:
        urhajo.sety(-300)

    if urhajo.ycor() < -300:
        urhajo.sety(300)

    meteorSzamlalo.write(szamlalo, align="center", font=("Arial", 36, "bold"))
    eletSzamlalo.write(life, align="center", font=("Arial", 36, "bold"))

    meteor.setx(meteor.xcor()-30)
    if meteor.xcor() < -400:        # meteor újra megjelenik
        meteor.setx(750)
        meteor.sety(random.randint(-270, 270))
        szamlalo += 1
        meteorSzamlalo.clear()
    if urhajo.distance(meteor.xcor(), meteor.ycor()) < 20:      # meteor eltalál
        life -= 1
        robbanas()
        eletSzamlalo.clear()

time.sleep(5)
eletSzamlalo.write("Meghaltál!", align="center", font=("Arial", 36, "bold"))
