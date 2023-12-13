import tkinter

cv_width = 600
cv_height = 400
n = 40
farba1 = "red"
farba2 = "blue"
farba3 = "yellow"

cv = tkinter.Canvas(width=cv_width, height=cv_height)
cv.pack()

i = n * 10 + 10
while i > 10:
    i -= 10
    cv.create_rectangle(cv_width//2 - i//2, cv_height//2 - i//2, cv_width//2 + i//2, cv_height//2 + i//2, fill=farba1)
    farba1, farba2, farba3 = farba2, farba3, farba1

cv.mainloop()