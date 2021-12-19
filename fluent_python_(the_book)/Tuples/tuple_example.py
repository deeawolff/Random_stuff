lax_coordinates = (
33.9425, -118.408056)  # an example of how if some types of data were sorted it could destroy the data
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)  # an example of tuple Unpacking
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print(f"{passport}")

for country, _ in traveler_ids:
    print(country)

print(divmod(20, 8))

t = (20, 8)
print(divmod(*t))

quotient, remainder = divmod(*t)

print((quotient, remainder))

a, b, *rest = range(5)

print((a, b, rest))

*head, a, b = range(5)

print((head, a, b))
