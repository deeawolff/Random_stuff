import random
import string
import time

goal = "Hello"

population = []

mateing_pool = []

fitness_scores = []

for i in range(200):
    population.append("".join(random.choices(string.ascii_letters, k=len(goal))))


def fitness():
    for i in range(len(population)):
        score = 0

        for x in range(len(population[i])):

            if population[i][x] == goal[x]:
                mateing_pool.append(population[i])
                score += 1
        fitness_scores.append([score, i])


def reproduce():
    thing1 = random.choice(mateing_pool)
    thing2 = random.choice(mateing_pool)

    baby = ""

    for i in range(len(population[0])):
        choice = random.randint(0,1)

        if choice == 1:

            if random.randint(0, 100) == 15:
                baby = baby + random.choice(string.ascii_letters)
            else:
                baby = baby + thing1[i]

        elif choice == 1:
            if random.randint(0, 100) == 15:
                baby = baby + random.choice(string.ascii_letters)
            else:
                baby = baby + thing2[i]

    lowest = find_lowest_fitness_score()

    del population[lowest[1]]
    population.append(baby)

def find_lowest_fitness_score():
    lowest = [10000000000000000000, 0]

    for i in range(len(fitness_scores)):
        if fitness_scores[i][0] < lowest[0]:
            lowest = fitness_scores[i]
    return lowest


def is_complete():
    for i in range(len(population)):
        if population[i] == goal:
            return True
    return False


fitness()

while not is_complete():
    for i in range(50):

        reproduce()
        fitness()

    print(population)

print(population)