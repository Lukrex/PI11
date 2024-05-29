import tkinter as tk


cv = tk.Canvas()
cv.pack()

fbody = open("body.txt", "r")
for riadok in fbody:
    medzera = riadok.find(" ")
    x = int(riadok[:medzera])
    y = int(riadok[medzera:])
    print(x, y)
    print(type(x))


tk.mainloop()