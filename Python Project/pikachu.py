import turtle
t=turtle.Turtle()
t.pensize(3)
t.speed(0)
def meme(x,y):
    t.up()
    t.goto(x,y)
    t.down()
    
def eye1(x,y):
    meme(x, y)
    t.seth(0)
    t.fillcolor('#333333')
    t.begin_fill()
    t.circle(22)
    t.end_fill()

    meme(x + 6, y + 22)
    t.fillcolor('#ffffff')
    t.begin_fill()
    t.circle(10)
    t.end_fill()

def eye2(x, y):
    meme(x, y)
    t.seth(0)
    t.fillcolor('#333333')
    t.begin_fill()
    t.circle(22)
    t.end_fill()

    meme(x - 6, y + 22)
    t.fillcolor('#ffffff')
    t.begin_fill()
    t.circle(10)
    t.end_fill()

def base():
    t.fillcolor('#ffdd00')
    t.begin_fill()
    #
    t.penup()
    t.circle(130, 40)
    t.pendown()
    t.circle(100, 105)
    t.left(180)
    t.circle(-100, 5)

    #
    t.seth(20)
    t.circle(300, 30)
    t.circle(30, 50)
    t.seth(190)
    t.circle(300, 36)

    #
    t.seth(150)
    t.circle(150, 70)

    #
    t.seth(200)
    t.circle(300, 40)
    t.circle(30, 50)
    t.seth(20)
    t.circle(300, 35)
    #
    t.seth(240)
    t.circle(105, 95)
    t.left(180)
    t.circle(-105, 5)

    #
    t.seth(210)
    t.circle(500, 18)
    t.seth(200)
    t.fd(10)
    t.seth(280)
    t.fd(7)
    t.seth(210)
    t.fd(10)
    t.seth(300)
    t.circle(10, 80)
    t.seth(220)
    t.fd(10)
    t.seth(300)
    t.circle(10, 80)
    t.seth(240)
    t.fd(12)
    t.seth(0)
    t.fd(13)
    t.seth(240)
    t.circle(10, 70)
    t.seth(10)
    t.circle(10, 70)
    t.seth(10)
    t.circle(300, 18)

    t.seth(75)
    t.circle(500, 8)
    t.left(180)
    t.circle(-500, 15)
    t.seth(250)
    t.circle(100, 65)

    #
    t.seth(320)
    t.circle(100, 5)
    t.left(180)
    t.circle(-100, 5)
    t.seth(220)
    t.circle(200, 20)
    t.circle(20, 70)

    t.seth(60)
    t.circle(-100, 20)
    t.left(180)
    t.circle(100, 20)
    t.seth(300)
    t.circle(10, 70)

    t.seth(60)
    t.circle(-100, 20)
    t.left(180)
    t.circle(100, 20)
    t.seth(10)
    t.circle(100, 60)

    #
    t.seth(180)
    t.circle(-100, 10)
    t.left(180)
    t.circle(100, 10)
    t.seth(5)
    t.circle(100, 10)
    t.circle(-100, 40)
    t.circle(100, 35)
    t.left(180)
    t.circle(-100, 10)

    #
    t.seth(290)
    t.circle(100, 55)
    t.circle(10, 50)

    t.seth(120)
    t.circle(100, 20)
    t.left(180)
    t.circle(-100, 20)

    t.seth(0)
    t.circle(10, 50)

    t.seth(110)
    t.circle(100, 20)
    t.left(180)
    t.circle(-100, 20)

    t.seth(30)
    t.circle(20, 50)
    t.seth(100)
    t.circle(100, 40)

    #
    t.seth(200)
    t.circle(-100, 5)
    t.left(180)
    t.circle(100, 5)
    t.left(30)
    t.circle(100, 75)
    t.right(15)
    t.circle(-300, 21)
    t.left(180)
    t.circle(300, 3)

    #
    t.seth(43)
    t.circle(200, 60)

    t.right(10)
    t.fd(10)

    t.circle(5, 160)
    t.seth(90)
    t.circle(5, 160)
    t.seth(90)

    t.fd(10)
    t.seth(90)
    t.circle(5, 180)
    t.fd(10)

    t.left(180)
    t.left(20)
    t.fd(10)
    t.circle(5, 170)
    t.fd(10)
    t.seth(240)
    t.circle(50, 30)

    t.end_fill()

    meme(130, 125)
    t.seth(-20)
    t.fd(5)
    t.circle(-5, 160)
    t.fd(5)

    #
    meme(166, 130)
    t.seth(-90)
    t.fd(3)
    t.circle(-4, 180)
    t.fd(3)
    t.seth(-90)
    t.fd(3)
    t.circle(-4, 180)
    t.fd(3)

    #
    meme(168, 134)
    t.fillcolor('#ffdd00')
    t.begin_fill()
    t.seth(40)
    t.fd(200)
    t.seth(-80)
    t.fd(150)
    t.seth(210)
    t.fd(150)
    t.left(90)
    t.fd(100)
    t.right(95)
    t.fd(100)
    t.left(110)
    t.fd(70)
    t.right(110)
    t.fd(80)
    t.left(110)
    t.fd(30)
    t.right(110)
    t.fd(32)

    t.right(106)
    t.circle(100, 25)
    t.right(15)
    t.circle(-300, 2)
    
    t.seth(30)
    t.fd(40)
    t.left(100)
    t.fd(70)
    t.right(100)
    t.fd(80)
    t.left(100)
    t.fd(46)
    t.seth(66)
    t.circle(200, 38)
    t.right(10)
    t.fd(10)
    t.end_fill()

    #
    t.fillcolor('#923E24')
    meme(126.82, -156.84)
    t.begin_fill()

    t.seth(30)
    t.fd(40)
    t.left(100)
    t.fd(40)
    t.pencolor('#923e24')
    t.seth(-30)
    t.fd(30)
    t.left(140)
    t.fd(20)
    t.right(150)
    t.fd(20)
    t.left(150)
    t.fd(20)
    t.right(150)
    t.fd(20)
    t.left(130)
    t.fd(18)
    t.pencolor('#000000')
    t.seth(-45)
    t.fd(67)
    t.right(110)
    t.fd(80)
    t.left(110)
    t.fd(30)
    t.right(110)
    t.fd(32)
    t.right(106)
    t.circle(100, 25)
    t.right(15)
    t.circle(-300, 2)
    t.end_fill()

def mouth(x, y):

    #
    meme(-17, 94)
    t.seth(8)
    t.fd(4)
    t.back(8)

    meme(x, y)
    t.fillcolor('#88141D')
    t.begin_fill()
    #
    l1= []
    l2 = []
    t.seth(190)
    a = 0.7
    for i in range(28):
        a += 0.1
        t.right(3)
        t.fd(a)
        l1.append(t.position())

    meme(x, y)

    t.seth(10)
    a = 0.7
    for i in range(28):
        a += 0.1
        t.left(3)
        t.fd(a)
        l2.append(t.position())

    #

    t.seth(10)
    t.circle(50, 15)
    t.left(180)
    t.circle(-50, 15)

    t.circle(-50, 40)
    t.seth(233)
    t.circle(-50, 55)
    t.left(180)
    t.circle(50, 12.1)
    t.end_fill()

    #
    meme(17, 54)
    t.fillcolor('#DD716F')
    t.begin_fill()
    t.seth(145)
    t.circle(40, 86)
    t.penup()
    for pos in reversed(l1[:20]):
        t.goto(pos[0], pos[1] + 1.5)
    for pos in l2[:20]:
        t.goto(pos[0], pos[1] + 1.5)
    t.pendown()
    t.end_fill()

def ear1(x, y):
    meme(x, y)
    t.fillcolor('#000000')
    t.begin_fill()
    t.seth(330)
    t.circle(100, 35)
    t.seth(219)
    t.circle(-300, 19)
    t.seth(110)
    t.circle(-30, 50)
    t.circle(-300, 10)
    t.end_fill()

def ear2(x, y):
    meme(x, y)
    t.fillcolor('#000000')
    t.begin_fill()
    t.seth(300)
    t.circle(-100, 30)
    t.seth(35)
    t.circle(300, 15)
    t.circle(30, 50)
    t.seth(190)
    t.circle(300, 17)
    t.end_fill()

    #
def cheek1(x, y):
    turtle.tracer(False)
    meme(x, y)
    t.seth(300)
    t.fillcolor('#DD4D28')
    t.begin_fill()
    a = 2.3
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
            t.lt(3)
            t.fd(a)
        else:
            a += 0.05
            t.lt(3)
            t.fd(a)
    t.end_fill()
    turtle.tracer(True)

def cheek2(x, y):
    turtle.tracer(False)
    meme(x, y)
    t.seth(60)
    t.fillcolor('#DD4D28')
    t.begin_fill()
    a = 2.3
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
            t.lt(3)
            t.fd(a)
        else:
            a += 0.05
            t.lt(3)
            t.fd(a)
    t.end_fill()
    turtle.tracer(True)
    
    

base()
t.speed(10)
eye1(-85, 90)
eye2(50, 110)
t.speed(0)
mouth(-5, 25)
t.speed(10)
cheek1(-126, 32)
cheek2(107, 63)
ear1(-250, 100)
ear2(140, 270)
t.hideturtle()
meme(200,-270)
t.color("black")
t.write("-By Aryan",font=('Helvetica',50,"italic"))
