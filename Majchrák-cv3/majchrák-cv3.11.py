import tkinter, random

cv = tkinter.Canvas()
cv.pack()

input = input("Text do kartičky: ")

def karticka(x, y, text):
    cv.create_rectangle(x-50,y-20,x+50,y+20,fill="light grey")
    cv.create_text(x, y, text=text, fill="black", font=('arial 14'))


for i in range(10):
    karticka(random.randint(50, 300), random.randint(50, 200), input)

tkinter.mainloop()