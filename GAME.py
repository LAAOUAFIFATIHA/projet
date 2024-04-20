import turtle
import time 
import random
dly = 0.2

#set up of screen--------------------------------------
wn= turtle.Screen()
wn.title("game of snake ")
wn.bgcolor("blue")
wn.setup(width = 600 , height = 600)
wn.tracer(0)
#end of screen setup

#function-------------------------------------------
def go_up():
    hd.direction = "up"
def go_down():
    hd.direction = "down"
def go_right():
    hd.direction = "right"
def go_left():
    hd.direction = "left"

def move():
    if hd.direction == "up" :
        y = hd.ycor()
        hd.sety(y + 20)
    if hd.direction == "down" :
        y = hd.ycor()
        hd.sety(y - 20)
    if hd.direction == "right" :
        x = hd.xcor()
        hd.setx(x + 20)
    if hd.direction == "left" :
        x = hd.xcor()
        hd.setx(x - 20)

#snake head-------------------------------------------
hd = turtle.Turtle()
hd.speed(0)
hd.shape("square")
hd.color("black")
hd.penup()
hd.goto(0,0)#the begin from the center
hd.direction = "stop"

#food of snake-------------------------------------------
fd = turtle.Turtle()
fd.speed(0)
fd.shape("circle")
fd.color("red")
fd.penup()
fd.goto(0,100)#the begin from the center

#main of game ---------------------------------------
            #------------keyboard------------------#
wn.listen()
wn.onkeypress(go_up, "u")
wn.onkeypress(go_down, "d")
wn.onkeypress(go_right, "r")
wn.onkeypress(go_left, "l")

s=[]

while True :
    wn.update()
    #-------------after exist---------------#
    if hd.xcor() > 270 or hd.xcor() < -270 or hd.ycor() > 270 or hd.xcor() > 270 or hd.ycor() < -270:
         hd.goto(0,0)

    if hd.distance(fd) < 20 :
        fd.goto(random.randint(-270,270), random.randint(-270,270))
        #---------------------------add a part of body-----------------------#
        ws = turtle.Turtle()
        ws.speed(0)
        ws.shape("square")
        ws.color("grey")
        ws.penup()
        s.append(ws)
        #-----------stack-------------#
    for i in range(len(s)-1,0,-1):
            x = s[i-1].xcor()
            y = s[i-1].ycor()
            s[i].goto(x,y)

    if len(s) > 0:
            x = hd.xcor()
            y = hd.ycor()
            s[0].goto(x,y)

    move()
    time.sleep(dly)
    
    

wn.mainloop()
