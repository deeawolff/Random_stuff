import collections

thing = collections.namedtuple('thing', ['letter1', 'letter2'])

thinggie = thing(i for i in list("abcdefghijklmnopqrstuvwxyz"))

print([str(i) for i in range(10)])
