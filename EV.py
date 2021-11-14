import random
import string
import time

goal = "DouglasWolff"

population = []

mateing_pool = []

fitness_scores = []

for i in range(100):
    population.append("".join(random.choices(string.ascii_letters, k=len(goal))))


def fitness():
    global fitness_scores
    fitness_scores = []

    for i in range(len(population)):
        score = 0

        for x in range(len(population[i])):

            if population[i][x] == goal[x]:
                score += 1
                mateing_pool.append([population[i], i])

        fitness_scores.append([score, i])


def reproduce():
    thing1 = random.choice(mateing_pool)

    thing2 = random.choice(mateing_pool)


    randomchoice = [0, 1]

    for i in range(fitness_scores[thing1[1]][0]):
        randomchoice.append(0)

    for i in range(fitness_scores[thing2[1]][0]):
        randomchoice.append(1)

    baby = ""

    for i in range(len(population[0])):
        choice = random.choice(randomchoice)

        if choice == 0:

            if random.randint(0, 20) == 0:
                baby = baby + random.choice(string.ascii_letters)
            else:
                baby = baby + thing1[0][i]

        elif choice == 1:
            if random.randint(0, 20) == 0:
                baby = baby + random.choice(string.ascii_letters)
            else:
                baby = baby + thing2[0][i]

    lowest = find_lowest_fitness_score()

    del population[lowest[1]]
    population.append(baby)




def find_lowest_fitness_score():
    lowest = [100, 0]

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


generations = 0
while not is_complete():
    for i in range(50):
        fitness()
        reproduce()
    generations += 1

    print(population)

print(generations)
print(population)
