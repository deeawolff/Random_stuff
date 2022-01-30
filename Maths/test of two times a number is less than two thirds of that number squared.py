import matplotlib.pyplot as plt

for n in range(100):
    two_thirds = 2 / 3
    two_thirds_of_n = n * two_thirds
    if n * 2 < two_thirds_of_n * two_thirds_of_n:
        print(True)
    else:
        print(False)


def graph(y):
    x = [i for i in range(len(y))]
    plt.plot(x, y)
    plt.show()


graph([n * 2 for n in range(100)])
graph([n * n])
