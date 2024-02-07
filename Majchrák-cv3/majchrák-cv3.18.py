import tkinter

x, y = 190, 130
r = 120
k = 6

cv = tkinter.Canvas()
cv.pack()

kk = k
repeat = True
while repeat == True:
    if kk == k:
        cv.create_oval(x - r, y - r, x + r, y + r, outline="grey")
        kk = 0
    else:
        cv.create_oval(x-r,y-r,x+r,y+r)
    kk += 1
    r -= 3
    if r < 18:
        repeat = False


tkinter.mainloop()