import turtle
import time
import random


def fel():
    ypos = urhajo.ycor()
    ypos += 15
    urhajo.sety(ypos)


def le():
    ypos = urhajo.ycor()
    ypos -= 15
    urhajo.sety(ypos)


def balra():
    xpos = urhajo.xcor()
    xpos += 15
    urhajo.setx(xpos)


def jobbra():
    xpos = urhajo.xcor()
    xpos -= 15
    urhajo.setx(xpos)


def robbanas():
    corx = meteor.xcor()
    cory = meteor.ycor()
    explosion.setx(corx)
    explosion.sety(cory)
    explosion.showturtle()
    meteor.setx(750)
    meteor.sety(random.randint(-270, 270))
    space.update()

lovedekList = []
def loves():
    corx = urhajo.xcor()
    cory = urhajo.ycor()
    lovedek.setx(corx)
    lovedek.sety(cory)
    lovedek.showturtle()
    lovedekList.append(lovedek.clone())
    lovedek.hideturtle()


def lovedekMove():
    for loves in lovedekList:
        corx = loves.xcor()
        loves.setx(corx + 25)
        if loves.xcor() > 750:
            loves.hideturtle()
            lovedekList.remove(loves)

szamlalo = 0

def Talalat(x):
    for loves in lovedekList:
        if loves.distance(meteor.xcor(), meteor.ycor()) < 20:
            robbanas()
            loves.hideturtle()
            lovedekList.remove(loves)
            x += 1
            meteorSzamlalo.clear()
    return x

# képernyő
space = turtle.Screen()
space.setup(width=800, height=600)
space.bgpic("background.png")
space.addshape("sprite.gif")
space.addshape("meteor2.gif")
space.addshape("explosion.gif")
space.addshape("blastshot.gif")
space.tracer(0)

space.listen()

# gomb érzékelés
space.onkeypress(fel, "Up")
space.onkeypress(le, "Down")
space.onkeypress(jobbra, "Left")
space.onkeypress(balra, "Right")
space.onkeypress(loves, "space")

# Űrhajó
urhajo = turtle.Turtle()
urhajo.shape("sprite.gif")
urhajo.penup()

# Meteor
meteor = turtle.Turtle()
meteor.shape("meteor2.gif")
meteor.setx(750)
meteor.sety(random.uniform(-270, 270))
meteor.penup()
kijelzo = turtle.Turtle()
kijelzo.hideturtle()

# Robbanás
explosion = turtle.Turtle()
explosion.shape("explosion.gif")
explosion.hideturtle()

# Lövedék
lovedek = turtle.Turtle()
lovedek.shape("blastshot.gif")
lovedek.hideturtle()
lovedek.penup()

# Meteorok kilőve
meteorSzamlalo = turtle.Turtle()
meteorSzamlalo.hideturtle()
meteorSzamlalo.penup()
meteorSzamlalo.color("Blue")
meteorSzamlalo.setx(-370)
meteorSzamlalo.sety(200)

# Hátramaradt életek száma
eletSzamlalo = turtle.Turtle()
eletSzamlalo.hideturtle()
eletSzamlalo.penup()
eletSzamlalo.color("Red")
eletSzamlalo.setx(-370)
eletSzamlalo.sety(250)
life = 3
pontok = 0

while life > 0:
    space.update()
    time.sleep(0.01)
    szamlalo = Talalat(szamlalo)
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

    explosion.hideturtle()
    meteor.setx(meteor.xcor() - 13)
    if meteor.xcor() < -400:  # meteor újra megjelenik
        meteor.setx(750)
        meteor.sety(random.randint(-270, 270))

    if urhajo.distance(meteor.xcor(), meteor.ycor()) < 20:  # meteor eltalál
        robbanas()
        time.sleep(1)
        life -= 1
        eletSzamlalo.clear()
    lovedekMove()

# meghaltál

space.update()
urhajo.hideturtle()
meteor.hideturtle()
explosion.hideturtle()
time.sleep(0.5)
space.update()
eletSzamlalo.setx(0)
eletSzamlalo.sety(0)
eletSzamlalo.write("Meghaltál!", align="center", font=("Arial", 36, "bold"))
time.sleep(5)
