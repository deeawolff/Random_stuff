from processing_py import *
import random

app = App(600, 400)


class Grid:
    def __init__(self):
        grid = []
        for i in range(600):
            row = []
            for i in range(400):
                row.append([])
            grid.append(row)

    def add_food(self, x, y):
        grid[x][y] =


class Cell:
    def __init__(self):
        position = [random.randint(0, 600), random.randint(0, 400)]

    def


class Food:
    def __init__(self):
        position = [random.randint(0, 600), random.randint(0, 400)]


while (True):
    app.background(0, 0, 0)  # set background:  red, green, blue
    app.fill(255, 255, 0)  # set color for objects: red, green, blue
    app.ellipse(app.mouseX, app.mouseY, 50, 50)  # draw a circle: center_x, center_y, size_x, size_y
    app.redraw()  # refresh the window
