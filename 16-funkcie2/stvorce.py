import tkinter
cv = tkinter.Canvas(width=600)
cv.pack()


def rgb(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"


def stvorce(x, y, pocet, dlzka, r=255, g=255, b=255):
    for i in range(pocet):
        krok = 255 // pocet
        cv.create_rectangle(x, y, x+dlzka, y+dlzka, fill=rgb(r, g, b))
        x += dlzka
        if r > krok:
            r -= krok
        if g > krok:
            g -= krok
        if b > krok:
            b -= krok


stvorce(20, 20, 30, 20, 255, 0, 0)
stvorce(20, 40, 30, 20, 0, 255, 0)
stvorce(20, 60, 30, 20, 0, 0, 255)
stvorce(20, 80, 30, 20, 255, 0, 0)
stvorce(20, 100, 30, 20, 0, 255, 0)
stvorce(20, 120, 30, 20, 0, 0, 255)
stvorce(20, 140, 30, 20, 255, 0, 0)
stvorce(20, 160, 30, 20, 0, 255, 0)
stvorce(20, 180, 30, 20, 0, 0, 255)
stvorce(20, 200, 30, 20, 255, 0, 0)
stvorce(20, 220, 30, 20, 0, 255, 0)
stvorce(20, 240, 30, 20, 0, 0, 255)

tkinter.mainloop()