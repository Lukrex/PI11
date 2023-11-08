import tkinter as tk

canvas = tk.Canvas()
canvas.pack()

# začiatok suradnice x
x = 100
# začiatok suradnice y
y = 50
dlzka = 50

canvas.create_rectangle(x, y, x + dlzka, y + dlzka, fill="red")
canvas.create_rectangle(x + dlzka, y, x + (2*dlzka), y + dlzka, fill="blue")
canvas.create_rectangle(x + (2*dlzka), y, x + (3*dlzka), y + dlzka, fill="red")
canvas.create_oval(x + dlzka, y + dlzka, x + (2*dlzka), y + (2*dlzka), fill="black")
canvas.create_oval(x + dlzka, y + (2*dlzka), x + (2*dlzka), y + (3*dlzka), fill="black")
canvas.create_rectangle(x, y + (4*dlzka), x + dlzka, y + (3*dlzka), fill="blue")
canvas.create_rectangle(x + dlzka, y + (4*dlzka), x + (2*dlzka), y + (3*dlzka), fill="red")
canvas.create_rectangle(x + (2*dlzka), y + (4*dlzka), x + (3*dlzka), y + (3*dlzka), fill="blue")

# okno sa nezavrie hneď, ale po kliknutí X
canvas.mainloop()