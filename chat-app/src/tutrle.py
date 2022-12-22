import time
from turtle import *

tim = Turtle()
screen = Screen()
screen.title("PISB LOGO")
screen.bgcolor("black")
screen.setup(width=540, height=540)
draw = Turtle()
color = ["blue", "white", "white"]
y = [0, 10, -10]
border = Turtle()
border.up()
border.color("green")
border.hideturtle()
border.goto(250, 250)
border.down()
border.goto(250, -250)
border.goto(-250, -250)
border.goto(-250, 250)
border.goto(250, 250)

for i in range(3):
    draw.hideturtle()
    draw.color(color[i])
    x = y[i]
    draw.up()
    draw.goto(0 + x, 0 + x)
    draw.down()
    xc = [0, 68, 68, -68, -68, 68, 68, 0]
    yc = [204, 204, 136, 136, 68, 68, 0, 0]
    for t in range(8):
        draw.goto(xc[t] +x, yc[t] + x)
tim.hideturtle()
tim.up()
tim.pencolor("blue")
tim.goto(-230, -50)
tim.write("CREDENZ", font=("BankGothic Md BT", 22, "bold"))
time.sleep(1)
tim.goto(-20, -50)
tim.write("IS", font=("BankGothic Md BT", 22, "bold"))
time.sleep(1)
tim.goto(50, -50)
tim.write("LIVE 2.0", font=("BankGothic Md BT", 22, "bold"))
anim = Turtle()
anim.pencolor("red")
anim.hideturtle()
anim.up()
anim.goto(-250, -130)
anim.down()
x_cor = [-180, -160, -120, -100, 0, 100, 120, 160, 180, 250]
y_cor = [-130, -90, -170, -130, -130, -130, -90, -170, -130, -130]
for i in range(10):
    anim.goto(x_cor[i], y_cor[i])
screen.exitonclick()
