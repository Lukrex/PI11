import tkinter
cv = tkinter.Canvas(width=600, height=600)
cv.pack()


def kruh(x, y, r, farba):
    cv.create_oval(x-r,y-r,x+r,y+r,fill=farba)


def kruhy_riadok(x, y, pocet, r, farba):
    for i in range(pocet):
        kruh(x, y, r, farba)
        x += 2*r


def kruhy_stvorec(x, y, pocet, r, farba):
    for i in range(pocet):
        kruhy_riadok(x, y, pocet, r, farba)
        y += 2*r


kruhy_stvorec(50, 50, 10, 10, "red")

cv.mainloop()