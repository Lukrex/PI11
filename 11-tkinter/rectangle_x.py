import tkinter as tk

canvas = tk.Canvas()
canvas.pack()

# začiatok suradnice x
x = 10
# začiatok suradnice y
y = 10
#dlzka
d = 30

farba = "violet"

canvas.create_rectangle(x, y, x+d, y+d, fill=farba)
canvas.create_rectangle(x+d, y+d, x+2*d, y+2*d, fill=farba)
canvas.create_rectangle(x+2*d, y+2*d, x+3*d, y+3*d, fill=farba)
canvas.create_rectangle(x+3*d, y+3*d, x+4*d, y+4*d, fill=farba)
canvas.create_rectangle(x+4*d, y+4*d, x+5*d, y+5*d, fill=farba)
canvas.create_rectangle(x+5*d, y, x+4*d, y+d, fill=farba)
canvas.create_rectangle(x+4*d, y+d, x+3*d, y+2*d, fill=farba)
canvas.create_rectangle(x+3*d, y+2*d, x+2*d, y+3*d, fill=farba)
canvas.create_rectangle(x+2*d, y+3*d, x+d, y+4*d, fill=farba)
canvas.create_rectangle(x+d, y+4*d, x, y+5*d, fill=farba)

# druha kresba
x = 190
y = 10
d = 30
farba = "purple"

canvas.create_rectangle(x, y, x+d, y+d, fill=farba)
canvas.create_rectangle(x+d, y+d, x+2*d, y+2*d, fill=farba)
canvas.create_rectangle(x+2*d, y+2*d, x+3*d, y+3*d, fill=farba)
canvas.create_rectangle(x+3*d, y+3*d, x+4*d, y+4*d, fill=farba)
canvas.create_rectangle(x+4*d, y+4*d, x+5*d, y+5*d, fill=farba)
canvas.create_rectangle(x+5*d, y, x+4*d, y+d, fill=farba)
canvas.create_rectangle(x+4*d, y+d, x+3*d, y+2*d, fill=farba)
canvas.create_rectangle(x+3*d, y+2*d, x+2*d, y+3*d, fill=farba)
canvas.create_rectangle(x+2*d, y+3*d, x+d, y+4*d, fill=farba)
canvas.create_rectangle(x+d, y+4*d, x, y+5*d, fill=farba)

# okno sa nezavrie hneď, ale po kliknutí X
canvas.mainloop()