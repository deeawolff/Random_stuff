from turtle import *

color('blue', 'purple')
begin_fill()
speed(100)
sides = int(input("input sides: "))
for i in range(sides):
    forward(50)
    left(360 / sides)
end_fill()
done()
