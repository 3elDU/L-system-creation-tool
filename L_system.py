import turtle

xPos = -200
yPos = 200

size = 5
pensize = 1

itr = 3

def draw():
    turtle.reset()
    turtle.clear()
    turtle.hideturtle()
    turtle.tracer(0)
    turtle.penup()
    turtle.setposition(xPos, yPos)
    turtle.pendown()
    turtle.pensize(pensize)
    
    axmTemp = ""

    f = open("L_system_settings.txt", "r")
    c = f.read().split('\n')
    f.close()

    # print(c)

    axiom = c[0]
    translate = eval(c[1])
    command = eval(c[2])

    # print(translate, command, sep='\n')
    
    for k in range(itr):
        for ch in axiom:
            axmTemp += translate[ch]
        axiom = axmTemp
        axmTemp = ""

    for ch in axiom:
        exec(command[ch])

    turtle.update()

def up():
    global yPos
    yPos += 10
    draw()

def down():
    global yPos
    yPos -= 10
    draw()

def left():
    global xPos
    xPos -= 10
    draw()

def right():
    global xPos
    xPos += 10
    draw()

def sizeUp():
    global size
    size += 1
    draw()

def sizeDown():
    global size
    size -= 1
    draw()

def penSizeDown():
    global pensize
    pensize -= 1
    draw()

def penSizeUp():
    global pensize
    pensize += 1
    draw()

def iterUp():
    global itr
    itr += 1
    draw()

def iterDown():
    global itr
    itr -= 1
    draw()


draw()

turtle.listen()

turtle.onkey(up, "w")  # This will call the up function if the "Left" arrow key is pressed
turtle.onkey(down, "s")
turtle.onkey(left, "a")
turtle.onkey(right, "d")

turtle.onkey(sizeUp, "Up")
turtle.onkey(sizeDown, "Down")

turtle.onkey(penSizeUp, "Right")
turtle.onkey(penSizeDown, "Left")

turtle.onkey(iterUp, "c")
turtle.onkey(iterDown, "z")

turtle.onkey(draw, "r")


turtle.mainloop()  # This will make sure the program continues to run 
