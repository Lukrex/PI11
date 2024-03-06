import turtle

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
turtle.delay(0)

t1.pu()
t1.setpos(-100,-50)
t1.pd()

t2.pu()
t2.setpos(100,-50)
t2.pd()

t3.pu()
t3.setpos(0,50)
t3.pd()

for i in range(200):
    for j in range(4):
        t1.fd(100)
        t2.fd(100)
        t3.fd(100)
        t1.lt(90)
        t2.lt(90)
        t3.lt(90)
    t1.lt(360/200)
    t2.lt(360/200)
    t3.lt(360/200)

turtle.mainloop()