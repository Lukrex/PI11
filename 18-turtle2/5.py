import turtle

pocet = 4
turtles = []

for i in range(pocet):
    t = turtle.Turtle()
    t.pu()
    t.setpos(i * 100, 0)
    t.pd()
    turtles.append(t)

# for i in range(4):
#     for t in turtles:
#         t.fd(50)
#         t.rt(90)

for t in turtles:
    for i in range(4):
        t.fd(50)
        t.rt(90)


turtle.mainloop()