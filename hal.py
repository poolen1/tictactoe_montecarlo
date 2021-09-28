import random as rand


class GameAI:
    def __init__(self):
        pass

    def random_move(self):
        move_digit = rand.randrange(1, 9)

        return str(move_digit)
