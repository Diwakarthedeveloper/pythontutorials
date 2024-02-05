import random, itertools
deck = list(itertools.product(range(1,14),["Spade","Club","Hearts","Diamond"]))

random.shuffle(deck) # this will print is shuffled way while above line will produce in arranged way
print(deck)

a = int(input("enter the number of cards you want to print"))
for i in range(a):
    print(deck[i][0], "of", deck[i][1])

