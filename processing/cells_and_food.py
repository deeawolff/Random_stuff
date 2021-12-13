import time
import math
from processing_py import *
import random
import matplotlib.pyplot as plt

screen_size = [1200, 800]

app = App(screen_size[0], screen_size[1])

cells = []

foods = []


def find_angle_from_oa(distances):
    tan_angle = 0.000000001
    if distances[0] != 0 and distances[1] != 0:
        tan_angle = distances[1] / distances[0]
    angle = math.atan(tan_angle)
    return angle


def find_o_from_hypotenuse_angle(hypotenuse, angle):
    return hypotenuse * math.sin(angle)


def find_a_from_hyoptenuse_angel(hypotenuse, angle):
    return hypotenuse * math.cos(angle)


def find_difference_between_two_coordinates(p1, p2):
    return [p1[0] - p2[0], p1[1] - p2[1]]


def are_objects_touching_each_other(p1, p2, p1size, p2size):
    if p1[0] + p1size > p2[0] - p2size:
        if p1[0] - p1size < p2[0] + p2size:
            if p1[1] + p1size > p2[1] - p2size:
                if p1[1] - p1size < p2[1] + p2size:
                    return True


class Cell:
    def __init__(self, number, food, position, colour, cell_type):
        self.number = number
        self.position = position
        self.movement = 6
        self.colour = colour
        self.this_cells_food = foods[random.randint(0, 2)]
        self.food_position = self.this_cells_food.return_position()
        self.size = food
        self.ready_for_deletion = False
        self.eating = False
        self.cells_touching = []
        self.cell_type = cell_type

    def update(self):

        if not self.eating:
            self.size -= 0.02

        self.move_towards_food()
        self.try_and_eat()
        self.try_and_divide()
        self.see_if_dead()
        if self.touching_other_cell() and self.cell_type == "sharer":
            self.try_share_food()

        if self.this_cells_food.size <= 1:
            self.eating = False
            self.find_new_food()

        app.fill(self.colour[0], self.colour[1], self.colour[2])
        app.ellipse(self.position[0], self.position[1], self.size, self.size)

    def move_towards_food(self):
        difference_between_coordinates = find_difference_between_two_coordinates(self.position, self.food_position)
        angle = find_angle_from_oa(difference_between_coordinates)

        change_in_x = find_a_from_hyoptenuse_angel(self.movement, angle)  # + random.randint(-2, 2)
        change_in_y = find_o_from_hypotenuse_angle(self.movement, angle)  # + random.randint(-2, 2)

        if self.position[0] < self.food_position[0]:
            self.position = [self.position[0] + change_in_x, self.position[1] + change_in_y]

        else:
            self.position = [self.position[0] - change_in_x, self.position[1] - change_in_y]

        return

    def try_and_eat(self):
        if are_objects_touching_each_other(self.position, self.food_position, self.size, self.this_cells_food.size):
            self.this_cells_food.get_eaten()
            self.size += 0.2
            self.eating = True

    def find_new_food(self):
        self.this_cells_food = foods[random.randint(0, len(foods) - 1)]
        self.food_position = self.this_cells_food.return_position()

    def try_and_divide(self):
        if self.size >= 10:
            # if not random.randint(0, 10):
            #    cells.append(
            #       Cell(i, 5, self.position, [random.randint(0, 254), random.randint(0, 254), random.randint(0, 254)],
            #             self.cell_type))
            # else:
            cells.append(Cell(i, 5, self.position, self.colour, self.cell_type))
            self.size -= 5

    def see_if_dead(self):
        if self.size <= 1:
            self.ready_for_deletion = True

    def touching_other_cell(self):
        self.cells_touching = []
        will_return = False
        for x in range(len(cells)):
            if are_objects_touching_each_other(self.position, cells[x].position, self.size,
                                               cells[x].this_cells_food.size):
                self.cells_touching.append(cells[x])
                will_return = True

        return will_return

    def try_share_food(self):
        for x in range(len(self.cells_touching)):
            if self.cells_touching[x].colour == self.colour:
                if self.size > self.cells_touching[x].size:
                    self.size -= 1
                    self.cells_touching[x].size += 1


class Food:
    def __init__(self, number):
        self.position = [random.randint(1, screen_size[0]), random.randint(1, screen_size[1])]
        self.size = random.randint(2, 25)
        self.number = number
        self.ready_for_deletion = False

    def update(self):
        # self.go_to_mouse()
        app.fill(255, 255, 0)
        app.ellipse(self.position[0], self.position[1], self.size, self.size)

    def return_position(self):
        return self.position

    def go_to_mouse(self):
        self.position = [app.mouseX, app.mouseY]

    def get_eaten(self):
        self.size = self.size - 0.2
        if self.size <= 1:
            self.ready_for_deletion = True


for i in range(6):
    foods.append(Food(i))

for i in range(5):
    cells.append(Cell(i, 5, [random.randint(1, screen_size[0]), random.randint(1, screen_size[1])],
                      [0, 255, 0],
                      "sharer"))  # [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

for i in range(5):
    cells.append(Cell(i, 5, [random.randint(1, screen_size[0]), random.randint(1, screen_size[1])],
                      [255, 0, 0], "loner"))  # [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

sharer_population = []
loner_popuation = []
other_cells_population = []

try:
    while True:
        app.background(0, 0, 0)  # set background:  red, green, blue
        app.fill(255, 255, 0)  # set color for objects: red, green, blue
        cells_deleted_this_time_round = 0
        sharer_number = 0
        loner_number = 0
        random_other_cells = 0
        for i in range(len(cells)):

            if cells[i - cells_deleted_this_time_round].ready_for_deletion:
                del cells[i - cells_deleted_this_time_round]
                cells_deleted_this_time_round += 1
            else:
                cells[i - cells_deleted_this_time_round].update()

            if cells[i - cells_deleted_this_time_round].cell_type == "sharer":
                sharer_number += 1
            elif cells[i - cells_deleted_this_time_round].cell_type == "loner":
                loner_number += 1
            else:
                random_other_cells += 1

        for i in range(len(foods)):
            if foods[i].ready_for_deletion:
                del foods[i]
                foods.append(Food(len(foods) - 1))
            else:
                foods[i].update()

        sharer_population.append(sharer_number)
        loner_popuation.append(loner_number)
        other_cells_population.append(random_other_cells)
        app.redraw()  # refresh the window


except KeyboardInterrupt:
    x = []
    for i in range(len(sharer_population)):
        x.append(i)

y = sharer_population

plt.plot(x, y)
