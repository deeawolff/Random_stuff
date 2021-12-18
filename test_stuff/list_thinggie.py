import collections

Thing = collections.namedtuple('thing', ['letter1', 'letter2'])

thinggie = [Thing(l1, l2) for l1 in list("abcdefghijklmnopqrstuvwxyz") for l2 in list("1234567890")]

print(thinggie)

print([str(i) for i in range(10)])
