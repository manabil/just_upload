from operator import itemgetter

fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}
print(sorted(fruit.items()))
print(sorted(fruit.items(), key=itemgetter(0)))
print(sorted(fruit.items(), key=itemgetter(1)))
print(sorted(fruit.items(), key=itemgetter(1), reverse=True))

