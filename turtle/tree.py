import turtle
import math

RADIANS = 180 / math.pi

wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")
tim = turtle.Turtle()

tim.color('blue', 'purple')
tim.begin_fill()
tim.speed(100)


def find_opposite(distance_from_center, number_of_branches, length_of_the_adjacent):
    adjacent = length_of_the_adjacent
    number_of_gaps = number_of_branches + 1
    angle = 180 / number_of_gaps
    this_branches_angle = angle * distance_from_center
    radians_this_branches_angle = math.radians(this_branches_angle)

    opposite = math.tan(radians_this_branches_angle) * adjacent

    return opposite


def find_hypotenuse(distance_from_center, number_of_branches, length_of_the_adjacent):
    opposite = find_opposite(distance_from_center, number_of_branches, length_of_the_adjacent)
    number_of_gaps = number_of_branches + 1
    angle = 180 / number_of_gaps
    this_branches_angle = angle * distance_from_center
    radians_this_branches_angle = math.radians(this_branches_angle)

    hypotenuse = opposite / math.sin(radians_this_branches_angle)

    return hypotenuse


def tim_fb(distance):
    tim.forward(distance)
    tim.rotate(180)
    tim.forward(distance)


print(find_opposite(1, 3, 100))

print(find_hypotenuse(1, 3, 100))

num_of_stages = int(input("number of stages"))
stages = []
tree = []

for i in range(num_of_stages):
    stages.append(int(input("number of branches")))

tim.forward(100)

for i in stages:
    tree.append([])
    for x in range(i):

turtle.done()
