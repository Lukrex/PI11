import tkinter
import random

cv = tkinter.Canvas(width=1200, height=600, bg="sky blue")
cv.pack()

# začiatok suradnice x
x = 3
# začiatok suradnice y
y = 10
#dlzka
d = 108
pocet = 1198 // d #celočíselné delenie (integer) 7 // 3 = 2
xx = x

for j in range(598 // d):
    for i in range(pocet):
        farba = random.choice(("green", "red", "blue", "orange", "purple", "yellow"))
        cv.create_rectangle(x,y+d//2,x+d,y+d+d//2,fill=farba)
        cv.create_polygon(x,y+d//2,x+d//2,y,x+d,y+d//2,fill="brown",outline="black")
        cv.create_rectangle(x+d//4,y+d//4+d//2,x+d//4*3,y+d//4*3+d//2,width=2,fill="sky blue")
        cv.create_line(x+d//2,y+d//4+d//2,x+d//2,y+d//4*3+d//2,width=2)
        cv.create_line(x+d//4,y+d,x+d//4+d//2,y+d,width=2)
        x = x + d
    y = y + d + d//2
    x = xx


cv.mainloop()