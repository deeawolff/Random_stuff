from processing_py import *
import math

screen_size = (600, 400)
app = App(screen_size[0], screen_size[1])  # create window: width, height

answers = [[] for i in range(15)]

angle = 360 / len(answers)
print(f"angle = {angle} len(answers) = {len(answers)}  angle * len(answers) = {angle * len(answers)}")

squares = [4, 9, 16, 25, 36]

for i in range(1, 16):
    for x in range(len(squares)):
        for e in range(1, 16):
            # print(f"e = {e} i = {i}")
            if e + i == squares[x]:
                # print(f"added {e}")

                answers[i - 1].append(e)

print(answers)


class pointOnTheCircle:
    position = ()

    def __init__(self, number_on_the_circle, _angle, size_of_the_screen, radius):
        self.position = (size_of_the_screen[0] / 2 + radius * math.cos(math.radians(angle * number_on_the_circle)),
                         size_of_the_screen[1] / 2 + radius * math.sin(math.radians(angle * number_on_the_circle)))
        number_of_points_on_circle = 360 / _angle
        circumference = math.pi * 2 * radius
        self.size = circumference / number_of_points_on_circle


points_on_the_circle = [pointOnTheCircle(i, angle, screen_size, 100) for i in range(len(answers))]
while (True):
    app.background(0, 0, 0)  # set background:  red, green, blue
    app.fill(255, 255, 0)  # set color for objects: red, green, blue

    for i in range(len(answers)):
        app.ellipse(points_on_the_circle[i].position[0], points_on_the_circle[i].position[1],
                    points_on_the_circle[i].size, points_on_the_circle[i].size)

    # for i in range(len(answers)):
    #    for x in range(len)

    app.redraw()  # refresh the window
