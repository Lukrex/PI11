import tkinter, random

cv_width = 600
cv_height = 400
n = 50

cv = tkinter.Canvas(width=cv_width, height=cv_height)
cv.pack()

for i in range(n):
    x = random.randint(40, cv_width - 40)
    y = random.randint(40, cv_height - 40)
    cislo = random.randint(1, 9)
    farba = "#"+("%06x"%random.randint(0,16777215))
    cv.create_oval(x - 20, y - 20, x + 20, y + 20, fill=farba)
    cv.create_text(x, y, text=cislo, font=('arial 30'))


cv.mainloop()