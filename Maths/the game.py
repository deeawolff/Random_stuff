import math

from processing_py import *

screen_size = (1200, 800)
app = App(screen_size[0], screen_size[1])  # create window: width, height

answers = [[] for i in range(23)]

angle = 360 / len(answers)
# print(f"angle = {angle} len(answers) = {len(answers)}  angle * len(answers) = {angle * len(answers)}")
n2plus1 = [2 * n + 1 for n in range(len(answers))]

n2plus1_counter = 0
while n2plus1[n2plus1_counter] < len(answers):
    n2plus1_counter += 1

print(n2plus1_counter)
squares = [i * i for i in range(0, n2plus1_counter)]

for i in range(1, len(answers) + 1):
    for x in range(len(squares)):
        for e in range(1, len(answers) + 1):
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


points_on_the_circle = [pointOnTheCircle(i, angle, screen_size, screen_size[1] / 3) for i in range(len(answers))]
while (True):
    app.textSize(22)
    app.background(255, 255, 255)  # set background:  red, green, blue
    app.fill(255, 255, 0)  # set color for objects: red, green, blue

    for i in range(len(answers)):
        app.fill(255, 255, 0)
        app.ellipse(points_on_the_circle[i].position[0], points_on_the_circle[i].position[1],
                    points_on_the_circle[i].size, points_on_the_circle[i].size)

    for i in range(len(answers)):
        app.fill(0, 0, 0)
        app.text(i + 1, points_on_the_circle[i].position[0] - 11, points_on_the_circle[i].position[1] + 11)

        for x in range(len(answers[i])):
            app.line(points_on_the_circle[i].position[0], points_on_the_circle[i].position[1],
                     points_on_the_circle[answers[i][x] - 1].position[0],
                     points_on_the_circle[answers[i][x] - 1].position[1])

    app.redraw()  # refresh the window
