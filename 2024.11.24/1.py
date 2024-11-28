def deck() -> tuple:
    suits = ['черви', 'бубны', 'пики', 'трефы']
    nominals = range(2, 15)
    for suit in suits:
        for nominal in nominals:
            yield (nominal, suit)

# >>> list(deck())[::13]
# [(2, 'черви'), (2, 'бубны'), (2, 'пики'), (2, 'трефы')]
# >>> list(deck())[12::13]
# [(14, 'черви'), (14, 'бубны'), (14, 'пики'), (14, 'трефы')]
