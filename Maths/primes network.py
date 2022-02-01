import math

from processing_py import *

screen_size = (1200, 800)
app = App(screen_size[0], screen_size[1])  # create window: width, height

answers = [[] for i in range(10)]

angle = 360 / len(answers)
# print(f"angle = {angle} len(answers) = {len(answers)}  angle * len(answers) = {angle * len(answers)}")

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
          109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
          233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293]

for i in range(1, len(answers) + 1):
    for x in range(len(primes)):
        for e in range(1, len(answers) + 1):
            # print(f"e = {e} i = {i}")
            if e + i == primes[x]:
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
