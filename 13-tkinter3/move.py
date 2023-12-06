import tkinter, random, time
cv = tkinter.Canvas()
cv.pack()

stvorec1 = cv.create_rectangle(10,10,110,110, fill="red")
for i in range(999):
    cv.update()
    time.sleep(0.02)
    cv.move(stvorec1, 1,0)
    farba = random.choice(("red","green","orange","purple"))
    cv.itemconfig(stvorec1, fill=farba)

cv.mainloop()