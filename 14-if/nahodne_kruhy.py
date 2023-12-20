import tkinter, random

cv_width = 600
cv_height = 400
r = 10
pocet = 99999

cv = tkinter.Canvas(width=cv_width, height=cv_height)
cv.pack()

for i in range(pocet):
    x = random.randint(r + 2, cv_width - r + 2)
    y = random.randint(r + 2, cv_height - r + 2)
    if x <= cv_width // 2 and y < cv_height // 2:
        farba = "red"
    elif x < cv_width // 2 and y >= cv_height // 2:
        farba = "yellow"
    elif x > cv_width // 2 and y < cv_height // 2:
        farba = "blue"
    else:
        farba = "green"
    cv.create_oval(x - r, y - r, x + r, y + r, fill=farba)
    cv.update()

cv.mainloop()
