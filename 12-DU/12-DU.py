import tkinter
import random

cv = tkinter.Canvas(width=1200, height=600, bg="sky blue")
cv.pack()

# začiatok suradnice x
x = 10
# začiatok suradnice y
y = 10
#dlzka
d = 12
xx = x

for j in range(598 // d):
    for i in range(1198 // d):
        farba = random.choice(("green", "red", "blue", "orange", "purple", "yellow", "teal", "cyan", "dark red", "pink"))
        # L
        cv.create_rectangle(x, y, x + d, y + d, fill=farba)
        cv.create_rectangle(x, y + d, x + d, y + 2 * d, fill=farba)
        cv.create_rectangle(x, y + 2 * d, x + d, y + 3 * d, fill=farba)
        cv.create_rectangle(x, y + 3 * d, x + d, y + 4 * d, fill=farba)
        cv.create_rectangle(x, y + 4 * d, x + d, y + 5 * d, fill=farba)
        cv.create_rectangle(x, y + 5 * d, x + d, y + 6 * d, fill=farba)
        cv.create_rectangle(x, y + 6 * d, x + d, y + 7 * d, fill=farba)
        cv.create_rectangle(x + d, y + 6 * d, x + 2 * d, y + 7 * d, fill=farba)
        cv.create_rectangle(x + 2 * d, y + 6 * d, x + 3 * d, y + 7 * d, fill=farba)
        cv.create_rectangle(x + 3 * d, y + 6 * d, x + 4 * d, y + 7 * d, fill=farba)
        cv.create_rectangle(x + 4 * d, y + 6 * d, x + 5 * d, y + 7 * d, fill=farba)

        # U
        cv.create_rectangle(x + 6 * d, y, x + 7 * d, y + d, fill=farba)
        cv.create_rectangle(x + 6 * d, y + d, x + 7 * d, y + 2 * d, fill=farba)
        cv.create_rectangle(x + 6 * d, y + 2 * d, x + 7 * d, y + 3 * d, fill=farba)
        cv.create_rectangle(x + 6 * d, y + 3 * d, x + 7 * d, y + 4 * d, fill=farba)
        cv.create_rectangle(x + 6 * d, y + 4 * d, x + 7 * d, y + 5 * d, fill=farba)
        cv.create_rectangle(x + 6 * d, y + 5 * d, x + 7 * d, y + 6 * d, fill=farba)

        cv.create_rectangle(x + 7 * d, y + 6 * d, x + 8 * d, y + 7 * d, fill=farba)
        cv.create_rectangle(x + 8 * d, y + 6 * d, x + 9 * d, y + 7 * d, fill=farba)
        cv.create_rectangle(x + 9 * d, y + 6 * d, x + 10 * d, y + 7 * d, fill=farba)

        cv.create_rectangle(x + 10 * d, y, x + 11 * d, y + d, fill=farba)
        cv.create_rectangle(x + 10 * d, y + d, x + 11 * d, y + 2 * d, fill=farba)
        cv.create_rectangle(x + 10 * d, y + 2 * d, x + 11 * d, y + 3 * d, fill=farba)
        cv.create_rectangle(x + 10 * d, y + 3 * d, x + 11 * d, y + 4 * d, fill=farba)
        cv.create_rectangle(x + 10 * d, y + 4 * d, x + 11 * d, y + 5 * d, fill=farba)
        cv.create_rectangle(x + 10 * d, y + 5 * d, x + 11 * d, y + 6 * d, fill=farba)

        # K
        cv.create_rectangle(x + 12 * d, y, x + 13 * d, y + d, fill=farba)
        cv.create_rectangle(x + 12 * d, y + d, x + 13 * d, y + 2 * d, fill=farba)
        cv.create_rectangle(x + 12 * d, y + 2 * d, x + 13 * d, y + 3 * d, fill=farba)
        cv.create_rectangle(x + 12 * d, y + 3 * d, x + 13 * d, y + 4 * d, fill=farba)
        cv.create_rectangle(x + 12 * d, y + 4 * d, x + 13 * d, y + 5 * d, fill=farba)
        cv.create_rectangle(x + 12 * d, y + 5 * d, x + 13 * d, y + 6 * d, fill=farba)
        cv.create_rectangle(x + 12 * d, y + 6 * d, x + 13 * d, y + 7 * d, fill=farba)

        cv.create_rectangle(x + 13 * d, y + 3 * d, x + 14 * d, y + 4 * d, fill=farba)
        cv.create_rectangle(x + 14 * d, y + 4 * d, x + 15 * d, y + 5 * d, fill=farba)
        cv.create_rectangle(x + 15 * d, y + 5 * d, x + 16 * d, y + 6 * d, fill=farba)
        cv.create_rectangle(x + 16 * d, y + 6 * d, x + 17 * d, y + 7 * d, fill=farba)
        cv.create_rectangle(x + 14 * d, y + 2 * d, x + 15 * d, y + 3 * d, fill=farba)
        cv.create_rectangle(x + 15 * d, y + d, x + 16 * d, y + 2 * d, fill=farba)
        cv.create_rectangle(x + 16 * d, y, x + 17 * d, y + d, fill=farba)

        # A
        cv.create_rectangle(x + 18 * d, y + d, x + 19 * d, y + 2 * d, fill=farba)
        cv.create_rectangle(x + 18 * d, y + 2 * d, x + 19 * d, y + 3 * d, fill=farba)
        cv.create_rectangle(x + 18 * d, y + 3 * d, x + 19 * d, y + 4 * d, fill=farba)
        cv.create_rectangle(x + 18 * d, y + 4 * d, x + 19 * d, y + 5 * d, fill=farba)
        cv.create_rectangle(x + 18 * d, y + 5 * d, x + 19 * d, y + 6 * d, fill=farba)
        cv.create_rectangle(x + 18 * d, y + 6 * d, x + 19 * d, y + 7 * d, fill=farba)

        cv.create_rectangle(x + 19 * d, y, x + 20 * d, y + d, fill=farba)
        cv.create_rectangle(x + 20 * d, y, x + 21 * d, y + d, fill=farba)
        cv.create_rectangle(x + 21 * d, y, x + 22 * d, y + d, fill=farba)

        cv.create_rectangle(x + 19 * d, y + 3 * d, x + 20 * d, y + 4 * d, fill=farba)
        cv.create_rectangle(x + 20 * d, y + 3 * d, x + 21 * d, y + 4 * d, fill=farba)
        cv.create_rectangle(x + 21 * d, y + 3 * d, x + 22 * d, y + 4 * d, fill=farba)

        cv.create_rectangle(x + 22 * d, y + d, x + 23 * d, y + 2 * d, fill=farba)
        cv.create_rectangle(x + 22 * d, y + 2 * d, x + 23 * d, y + 3 * d, fill=farba)
        cv.create_rectangle(x + 22 * d, y + 3 * d, x + 23 * d, y + 4 * d, fill=farba)
        cv.create_rectangle(x + 22 * d, y + 4 * d, x + 23 * d, y + 5 * d, fill=farba)
        cv.create_rectangle(x + 22 * d, y + 5 * d, x + 23 * d, y + 6 * d, fill=farba)
        cv.create_rectangle(x + 22 * d, y + 6 * d, x + 23 * d, y + 7 * d, fill=farba)

        # S
        cv.create_rectangle(x + 24 * d, y + d, x + 25 * d, y + 2 * d, fill=farba)
        cv.create_rectangle(x + 24 * d, y + 2 * d, x + 25 * d, y + 3 * d, fill=farba)

        cv.create_rectangle(x + 25 * d, y, x + 26 * d, y + d, fill=farba)
        cv.create_rectangle(x + 26 * d, y, x + 27 * d, y + d, fill=farba)
        cv.create_rectangle(x + 27 * d, y, x + 28 * d, y + d, fill=farba)
        cv.create_rectangle(x + 28 * d, y, x + 29 * d, y + d, fill=farba)

        cv.create_rectangle(x + 25 * d, y + 3 * d, x + 26 * d, y + 4 * d, fill=farba)
        cv.create_rectangle(x + 26 * d, y + 3 * d, x + 27 * d, y + 4 * d, fill=farba)
        cv.create_rectangle(x + 27 * d, y + 3 * d, x + 28 * d, y + 4 * d, fill=farba)

        cv.create_rectangle(x + 28 * d, y + 4 * d, x + 29 * d, y + 5 * d, fill=farba)
        cv.create_rectangle(x + 28 * d, y + 5 * d, x + 29 * d, y + 6 * d, fill=farba)

        cv.create_rectangle(x + 27 * d, y + 6 * d, x + 28 * d, y + 7 * d, fill=farba)
        cv.create_rectangle(x + 26 * d, y + 6 * d, x + 27 * d, y + 7 * d, fill=farba)
        cv.create_rectangle(x + 25 * d, y + 6 * d, x + 26 * d, y + 7 * d, fill=farba)
        cv.create_rectangle(x + 24 * d, y + 6 * d, x + 25 * d, y + 7 * d, fill=farba)
        x = x + 30 * d
    y = y + 10 * d
    x = xx

cv.mainloop()