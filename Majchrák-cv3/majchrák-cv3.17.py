import tkinter, random

r = 5
pocet = 10000

cv = tkinter.Canvas()
cv.pack()

for i in range(pocet):
    x = random.randint(10, 350)
    y = random.randint(10, 250)
    if y < 90:
        cv.create_oval(x - r, y - r, x + r, y + r, fill="black", outline="")
    elif y < 170:
        cv.create_oval(x - r, y - r, x + r, y + r, fill="red", outline="")
    else:
        cv.create_oval(x - r, y - r, x + r, y + r, fill="gold", outline="")


tkinter.mainloop()