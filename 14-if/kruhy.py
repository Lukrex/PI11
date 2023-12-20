import tkinter

cv_width = 600
cv_height = cv_width
r = 8
pocet = cv_width // (r*2)

cv = tkinter.Canvas(width=cv_width, height=cv_height)
cv.pack()

for i in range(pocet): # riadky
    for j in range(pocet): # stlpce
        x = j * r*2 + r + 2
        y = i * r*2 + r + 2
        if j == pocet // 2:
            farba = "red"
        else:
            farba = "white"
        cv.create_oval(x-r, y-r, x+r, y+r, fill=farba)

cv.mainloop()
