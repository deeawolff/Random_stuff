from turtle import *

color('blue', 'purple')
begin_fill()
speed(100)
sides = int(input("input sides: "))
x = int(input("input angle multipier"))

for i in range(sides):
    turning = 360 / sides
    forward(50)
    left(turning * x)

end_fill()
done()
