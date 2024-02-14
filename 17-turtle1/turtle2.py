import turtle
t = turtle.Turtle()
t.speed(0)


def sachovnica(dlzka, farba1, farba2):
    yy = 0
    for a in range(8):
        t.pendown()
        for i in range(4):
            t.fillcolor(farba1)
            t.begin_fill()
            for j in range(4):
                t.fd(dlzka)
                t.left(90)
            t.end_fill()
            t.fd(dlzka)
            t.fillcolor(farba2)
            t.begin_fill()
            for j in range(4):
                t.fd(dlzka)
                t.left(90)
            t.end_fill()
            t.fd(dlzka)
        farba1, farba2 = farba2, farba1
        yy -= dlzka
        t.penup()
        t.setpos(0, yy)


sachovnica(30, "yellow", "brown")


turtle.mainloop()