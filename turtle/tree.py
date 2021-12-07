import random
import turtle
import math

RADIANS = 180 / math.pi

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Turtle")
wn.tracer(0)

tim = turtle.Turtle()

tim.color('blue', 'purple')
tim.begin_fill()
tim.speed(0)


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


def my_tree(tree, recursion_number):
    output = ""
    for i in range(len(tree)):
        # print(f"tree[i] = {tree[i]}")
        if tree[i] == "1":

            output = output + random.choice(["1", "11", "11", ])

        elif tree[i] == "0":
            output += "0[[0][0]]0"

        elif tree[i] == "]":
            output = output + "]"

        elif tree[i] == "[":
            output = output + "["

    if recursion_number == 0:
        return output
    else:
        output = my_tree(output, recursion_number - 1)
        return output


def fractal_tree(tree, recursion_number):
    output = ""
    for i in range(len(tree)):
        # print(f"tree[i] = {tree[i]}")
        if tree[i] == "1":
            output = output + "11"

        elif tree[i] == "0":
            output += "1[0]0"

        elif tree[i] == "]":
            output = output + "]"

        elif tree[i] == "[":
            output = output + "["

    if recursion_number == 0:
        return output
    else:
        output = fractal_tree(output, recursion_number - 1)
        return output


def draw_fractal_tree(recursion_depth, tim_distance):
    path = my_tree("0", recursion_depth)
    print(path)
    saved_states = []
    for i in range(len(path)):
        if path[i] == "1":
            tim.forward(tim_distance)

        elif path[i] == "0":
            tim.color("green")
            tim.forward(tim_distance)
            tim.color("blue")

        elif path[i] == "[":
            saved_states.append(get_turtle_state(tim))
            tim.left(20)

        elif path[i] == "]":
            tim.penup()
            restore_turtle_state(tim, saved_states[-1])
            tim.pendown()
            del saved_states[-1]
            tim.right(20)


def get_turtle_state(_turtle):
    return _turtle.heading(), _turtle.position()


def restore_turtle_state(_turtle, state):
    _turtle.setheading(state[0])
    _turtle.setposition(state[1][0], state[1][1])


print(find_opposite(1, 3, 100))

print(find_hypotenuse(1, 3, 100))

# num_of_stages = int(input("number of stages"))
# branch_numbers = []
# tree = []

# for i in range(num_of_stages):

#    branch_numbers.append(int(input("number of branches")))


# tim.forward(100)


tim.left(90)
tim.penup()
tim.backward(400)
tim.pendown()
print(fractal_tree("0", 3))
draw_fractal_tree(7, 6)
wn.update()

turtle.done()
