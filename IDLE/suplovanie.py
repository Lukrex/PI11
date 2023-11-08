import tkinter

canvas = tkinter.Canvas(width=850,height=450)
canvas.pack()

#L
canvas.create_line(50,50,50,200,100,200,fill="blue",width=20)
#U
canvas.create_line(150,50,150,200,200,200,200,50,fill="magenta",width=12)
#K
canvas.create_line(250,50,250,200,250,125,300,50,250,125,300,200,fill="orange",width=8)
#A
canvas.create_line(350,200,375,50,400,200,fill="black",width=10)
canvas.create_line(365,125,385,125,fill="black",width=10)
#S
canvas.create_line(500,100,475,50,450,100,500,150,475,200,450,150,fill="green",width=14)
#M
canvas.create_line(50,400,50,250,75,325,100,250,100,400,fill="red",width=12)
#A
canvas.create_line(150,400,175,250,200,400,fill="blue",width=6)
canvas.create_line(165,325,185,325,fill="blue",width=6)
#J
canvas.create_line(300,250,300,400,250,400,250,350,fill="magenta",width=16)
#C
canvas.create_line(400,250,350,250,350,400,400,400,fill="orange",width=20)
#H
canvas.create_line(450,250,450,400,450,325,500,325,500,400,500,250,fill="black",width=8)
#R
canvas.create_line(550,400,550,250,600,260,600,315,550,325,600,400,fill="green",width=12)
#A
canvas.create_line(650,400,675,250,700,400,fill="purple",width=10)
canvas.create_line(665,325,685,325,fill="purple",width=10)
#K
canvas.create_line(750,250,750,400,750,325,800,250,750,325,800,400,fill="teal",width=7)
#Dĺžeň
canvas.create_line(375,40,400,20,fill="black",width=10)
#Mäkčeň
canvas.create_line(450,20,475,40,500,20,fill="green",width=14)
#Dĺžeň
canvas.create_line(675,240,700,220,fill="purple",width=10)
