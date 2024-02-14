import turtle


def stvorce(pocet, dlzka):
    for i in range(pocet):
        i += 1
        for j in range(4):
            t.fd(dlzka*i)
            t.left(90)
        t.penup()
        t.right(90)
        t.fd(dlzka/2)
        t.right(90)
        t.fd(dlzka/2)
        t.right(180)
        t.pendown()


t = turtle.Turtle()
t.speed(0)

# for i in range(4):
#     for i in range(1,11):
#         stvorec(10*i)
#     t.left(90)

stvorce(10, 10)

turtle.mainloop()