# import matplotlib.pyplot as plt


# def graph(y):
#    x = [i for i in range(len(y))]
#    plt.plot(x, y)


squares_bigger_than_a_given_number_up_to_20 = []
for n in range(300):
    i = 1
    while n > i * i:
        i = i + 1
    print(f"n = {n} i = {i} i * i = {i * i}")
    squares_bigger_than_a_given_number_up_to_20.append(i)

print(squares_bigger_than_a_given_number_up_to_20)

# graph([n * 2 for n in range(20)])
# graph([1/3 * n * n for n in range(20)])
# graph(squares_bigger_than_a_given_number_up_to_20)
# plt.show()
