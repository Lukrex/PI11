import turtle

t = turtle.Turtle()
turtle.delay(0)


def stvorec(dlzka):
    for i in range(4):
        t.fd(dlzka)
        t.lt(90)


def n_uholnik(n, dlzka):
    for i in range(n):
        t.fd(dlzka)
        t.lt(360/n)


xx = 3
for i in range(3, 16):
    n_uholnik(i, 50)


turtle.mainloop()