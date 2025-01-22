from turtle import*
speed(7)
#we want to paint a hause 

#step 1:  draw a spuare

width(7)

color("green")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end od square 

#drawing a door

forward(70)

color("yellow")
left(90)
forward(150)
right(90)
forward(60)
right(90)
forward(150)


penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(60, 150)
pendown()
left(30)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)

penup()
goto(140, 150)
pendown()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)






exitonclick()
