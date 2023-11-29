import tkinter, random

cv = tkinter.Canvas(width=500,height=500)
cv.pack()

meno = "Ján"
priezvisko = "Mrkvička"
vek = 255

print(f"Volám sa {meno} {priezvisko} a mám {vek:02x} rokov.") #vek:02, 02 je počet cifier a x prevedie do hex. sústavy

polomer = 20
for i in range(2000):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    farba = f"#{r:02x}{g:02x}{b:02x}"
    x = random.randint(2,480)
    y = random.randint(2,480)
    cv.create_oval(x-polomer, y-polomer, x + polomer, y + polomer, fill=farba)


cv.mainloop()