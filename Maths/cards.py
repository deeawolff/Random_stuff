# def areAnyTheSame(array):
#     for i in len(array):
#


numbers = [[a, b, c, d] for a in range(0, 4) for b in range(0, 4) for c in range(0, 4) for d in range(0, 4) if
           a != b and a != c and a != d and b != c and b != d and c != d]
checkAgainst = [0, 1, 2, 3]
print(numbers)
print(len(numbers))
