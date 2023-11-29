import tkinter
import random

cv = tkinter.Canvas(width=1200, height=600)
cv.pack()

# začiatok suradnice x
x = 200
# začiatok suradnice y
y = 100
# dlzka
d = 19
xx = x

for j in range((600 - y) // (2 * d + d // 8)):
    for i in range((1200 - x) // (2 * d + d // 8)):
        color = "#" + ("%06x" % random.randint(0, 16777215))
        cv.create_oval(x, y, x + d, y + d, fill=color)
        cv.create_oval(x, y + d, x + d, y + 2 * d, fill=color)
        cv.create_oval(x + d, y, x + 2 * d, y + d, fill=color)
        cv.create_oval(x + d, y + d, x + 2 * d, y + 2 * d, fill=color)
        cv.create_oval(x + d / 2, y + d / 2, x + d + d / 2, y + d + d / 2, fill="yellow")
        x = x + 2 * d + d // 8
    y = y + 2 * d + d // 8
    x = xx

cv.mainloop()
