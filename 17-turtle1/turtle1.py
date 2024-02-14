import turtle, random


def stvorec(dlzka):
    for i in range(4):
        t.fd(dlzka)
        t.left(90)


t = turtle.Turtle()
t.speed(0)


for i in range(30):
    t.penup()
    t.setpos(random.randint(-200, 200), random.randint(-200, 200))
    stvorec(random.randint(0, 350))
    t.pendown()
    t.fillcolor(random.choice(("red", "green", "blue", "yellow")))
    t.begin_fill()
    stvorec(30)
    t.end_fill()


turtle.mainloop()