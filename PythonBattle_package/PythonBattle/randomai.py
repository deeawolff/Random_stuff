"""
AI Name: Random AI

Made by: Carter

Strategy currently:
Move around randomly.
Attack any robot in front of you.


RULES:
You have 10 health. So does the other robot.
You might have to start in the middle of either left or right of the 10x10 grid.
You may take one (1) move per turn. This includes moves, turns and attacks.
But you can look at stuff around you as much as you like.
(1,1) is the top left corner.

Things you can do...

Once a turn:

self.robot.attack() - Attacks the thing in front of it.
^ this piece of code
       ^ the robot it controls
             ^ the robot can attack.
             
self.robot.turnRight()
self.robot.turnLeft()
self.robot.goForth() - Move forward 1 space.
self.robot.attack()
 - Attack the thing in front.
self.robot.goBack() - Move back 1 space.


As many times as you like:

self.robot.lookInFront() - Looks ahead. Allowed as much as you like.
Possible answers: "wall", "bot", "blank", "me".

self.robot.checkSpace(space) - Checks a space.
E.g. result = self.robot.checkSpace((3,3)) checks space 3,3, sets 'result' to it. Same answers as above.

self.robot.locateEnemy() - returns (x,y) of the enemy position.

self.robot.position - Your own position.
self.robot.rotation - Your own rotation.
self.robot.calculateCoordinates(direction, distance, position)... read the book to find out :P
"""

import random


class AI:
    def __init__(self):

        self.currentlyDoing = 'stuff'
        self.enemy_position = [0, 0]

        pass

    def turn(self):
        if self.robot.lookInFront() == "bot":
            self.robot.attack()
            return

        if self.robot.locateEnemy()[0] > self.robot.position[0]:
            if self.robot.rotation == 1:
                self.robot.goForth()


        else:
            random.choice([self.robot.turnLeft, self.robot.turnRight, self.robot.goForth, self.robot.goForth,
                           self.robot.goBack()])()

            return
