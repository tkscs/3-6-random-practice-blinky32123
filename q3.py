import random
suits = "♠♥♣♦"
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

values=print(random.choices(values, k=5))
suits=print(random.choices(suits, k=5))
deck = "f[values, suits]"
print(deck)



# Make a deck of cards
# `deck` should be a list of strings with a value and a suit, e.g. "4♣"

#shuffle your `deck` and print it out

# sample a hand of 5 cards and print it out
# (WITHOUT replacement -- no repeats!)

# for i in range(5):
#     values=random.choices(values, k=1)
#     suits=random.choices(suits, k=1)
#     deck = f"{values, suits}"
#     print(deck)
    