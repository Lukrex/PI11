import tkinter, random

x=500
y=400
x2=x
y2=y


def jedlo():
    global x2, y2
    xx, yy = random.randint(10, 990), random.randint(10, 790)
    x2, y2 = xx, yy
    print("mnam")
    cv.coords(food, xx-3, yy-3, xx+3, yy+3)
    print(x2, y2)


def pohyb(event):
    global x, y
    if event.keysym == "w":
        cv.move(hrac, 0, -10)
        y-=10
    elif event.keysym == "s":
        cv.move(hrac, 0, 10)
        y+=10
    elif event.keysym == "a":
        cv.move(hrac, -10, 0)
        x-=10
    elif event.keysym == "d":
        cv.move(hrac, 10, 0)
        x+=10

    if x+50 > x2 > x-50 and y+50 > y2 > y-50:
        print(x, y, x2 ,y2)
        jedlo()


cv = tkinter.Canvas(height=800, width=1000)
cv.pack()
cv.bind_all('<KeyPress>', pohyb)

hrac = cv.create_rectangle(x - 50, y - 50, x + 50, y + 50, fill="blue", outline="blue")
food = cv.create_rectangle(x2-3, y2-3, x2+3, y2+3, fill="black")
jedlo()

cv.mainloop()