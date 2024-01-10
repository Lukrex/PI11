import tkinter

cv_width = 600
cv_height = 600
sirka = 45

pocet = cv_width // sirka + sirka
x = -sirka

cv = tkinter.Canvas(width=cv_width, height=cv_height)
cv.pack()

for i in range(pocet):
    cv.create_line(sirka + x, 0, sirka + x, cv_height, width=2, fill="blue")
    cv.create_line(0, sirka + x, cv_width, sirka + x, width=2, fill="blue")
    x += sirka//2
    cv.create_line(sirka + x, 0, sirka + x, cv_height, width=2, fill="red")
    cv.create_line(0, sirka + x, cv_width, sirka + x, width=2, fill="red")
    x += sirka // 2


cv.mainloop()
