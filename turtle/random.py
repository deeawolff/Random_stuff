from turtle import *
import random

color('red', 'yellow')
begin_fill()
speed(100)
for i in range(500):
    forward(random.randint(1, 50))
    left(random.randint(0, 360))
end_fill()
done()
