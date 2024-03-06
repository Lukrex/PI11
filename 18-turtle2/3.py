import turtle, random

t = turtle.Turtle()
turtle.delay(0)


def obluk(d):
    for i in range(9):
        t.fd(d)
        t.lt(10)


def lupen(d):
    for i in range(2):
        obluk(d)
        t.lt(90)


def kvet(d, n):
    for i in range(n):
        t.fillcolor(random.choice(("red", "green", "blue", "yellow")))
        t.begin_fill()
        lupen(d)
        t.left(360/n)
        t.end_fill()


kvet(20, 5)
for i in range(4):
    t.penup()
    t.setpos(random.randint(-300, 300), random.randint(-300, 300))
    t.pendown()
    kvet(20, 5)


turtle.mainloop()