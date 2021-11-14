#!/usr/bin/python3
import pygame
from pygame.locals import *
import time

import random
import sys

game_on = True


class Square(pygame.sprite.Sprite):

    def __init__(self, _size_):
        self.size = int(_size_)
        # print(f"{_size_} == {self.size}")

        super(Square, self).__init__()  # find out what this does
        self.surf = pygame.Surface((int(_size_) - 1, int(_size_) - 1))

        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()

        # print(f"square initialised with size {_size_}  \n")

    def fill(self, r, g, b):
        self.surf.fill((r, g, b))
        # print(f"fill funtion in square called, rgb= {r},{g},{b} \n")


class Grid:
    size = 10
    arr = []

    def __init__(self, screensize):
        self.size = int(input("input grid size (10 is recomended): "))
        for i in range(self.size):
            row = []
            for x in range(self.size):
                square = Square(int(screensize) / self.size)
                row.append(square)
            self.arr.append(row)

    def surf(self):
        for i in range(self.size):
            for x in range(self.size):
                screen.blit(self.arr[i][x].surf, (i * self.arr[0][0].size, x * self.arr[0][0].size))

    def colour_change(self, x, y, r, g, b):
        # print(f"colourchange function in grid called position= {x},{y} \n")
        self.arr[x][y].fill(r, g, b)


class Snake:
    length = 3
    positions = []
    current_position = [0, 0]
    positions.append(current_position)
    direction = 2

    def __init__(self):
        self.length = int(input("input snake length: "))
        print("\n")
        for i in range(self.length):
            self.positions.append([0, 0])

    def change_direction(self, new_direction):
        self.direction = new_direction

    def move(self):

        if self.direction == 1:
            self.current_position = [self.current_position[0], self.current_position[1] - 1]

        if self.direction == 2:
            self.current_position = [self.current_position[0], self.current_position[1] + 1]

        if self.direction == 3:
            self.current_position = [self.current_position[0] - 1, self.current_position[1]]

        if self.direction == 4:
            self.current_position = [self.current_position[0] + 1, self.current_position[1]]

        self.positions.append(self.current_position)

        apple.check_eaten(self.current_position)

        if snake.isdead():
            sys.exit(0)

    def display(self):
        grid.colour_change(self.positions[-self.length][0], self.positions[-self.length][1], 0, 0, 0)
        grid.colour_change(self.positions[-1][0], self.positions[-1][1], 0, 255, 0)

    def yum(self):
        self.length += 1

    def isdead(self):

        for i in range(self.length - 1):
            x = i + 2
            if self.positions[-x] == self.positions[-1]:
                print(str(self.positions[-x]) + " == " + str(self.current_position))
                return True
        if self.positions[-1][0] < 0 or self.positions[-1][1] < 0 or self.positions[-1][1] > grid.size or \
                self.positions[-1][1] > grid.size:
            return True

        return False

    def is_snake_here(self, x, y):
        for i in range(self.length + 1):
            a = i + 1
            if self.positions[-a] == [x, y]:
                return True

        return False

    # async def wait_for_movement(self):
    #     await asyncio.sleep(1)
    #     self.move()
    #


class Apple:
    position = [0, 0]

    def __init__(self):
        self.position = [random.randint(0, grid.size - 1), random.randint(0, grid.size - 1)]
        if snake.is_snake_here(self.position[0], self.position[1]):
            self.nom()
        print(self.position)
        self.display()

    def nom(self):
        self.position = [random.randint(0, grid.size), random.randint(0, grid.size)]
        # could replace random with a function in grid

        if snake.is_snake_here(self.position[0], self.position[1]):
            self.nom()
        self.display()
        snake.yum()

    def check_eaten(self, snake_position):
        if self.position == snake_position:
            self.nom()
            return True
        else:
            return False

    def display(self):
        grid.colour_change(self.position[0], self.position[1], 255, 0, 0)


screen_size = input("input screen size, 500 is small, 750 is medium and 1000 is large : ")

# screen_size = grid.size * Square.totalsquaresize

grid = Grid(screen_size)
snake = Snake()
apple = Apple()

print(screen_size)
pygame.init()
screen = pygame.display.set_mode((int(screen_size), int(screen_size)))

while game_on:
    for event in pygame.event.get():

        if event.type == KEYDOWN:

            if event.key == K_BACKSPACE:
                game_on = False

            if event.key == K_UP:
                print("up")
                snake.change_direction(1)
                snake.move()
                snake.display()

            if event.key == K_DOWN:
                print("down")
                snake.change_direction(2)
                snake.move()
                snake.display()

            if event.key == K_LEFT:
                print("left")
                snake.change_direction(3)
                snake.move()
                snake.display()

            if event.key == K_RIGHT:
                print("right")
                snake.change_direction(4)
                snake.move()
                snake.display()

        elif event.type == QUIT:
            game_on = False
        #
        # if int(time.time()) % 2 == 0:
        #     snake.move()
        #     print("moved")

        grid.surf()
        pygame.display.flip()
