import random as rand


class MCNode:
    def __init__(self, state, ptr):
        self.ptr = ptr
        self.wins = 0
        self.sims = 0
        self.successors = []


class GameAI:
    def __init__(self):
        pass

    def expand_node(self):
        pass

    def create_successor(self):
        pass

    def get_legal_ops(self):
        pass

    def selection(self):
        pass

    @staticmethod
    def create_successor(node):
        new_node = MCNode(node.state, node)
        new_node.successors = []
        return new_node

    @staticmethod
    def get_legal_ops(node):
        state = node.state

        rows = 3
        cols = 3
        moves = {}

        if state[2][0] == '-':
            moves[0] = True
        if state[2][1] == '-':
            moves[1] = True
        if state[2][2] == '-':
            moves[2] = True
        if state[1][0] == '-':
            moves[3] = True
        if state[1][1] == '-':
            moves[4] = True
        if state[1][2] == '-':
            moves[5] = True
        if state[0][0] == '-':
            moves[6] = True
        if state[0][1] == '-':
            moves[7] = True
        if state[0][2] == '-':
            moves[8] = True

        return moves

    def expansion(self):
        pass

    def rollout(self):
        pass

    def backprop(self):
        pass

    def search(self):
        pass

    def random_move(self):
        move_digit = rand.randrange(1, 9)

        return str(move_digit)
