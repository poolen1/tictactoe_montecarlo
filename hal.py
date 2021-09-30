import random as rand
import numpy as np
import math


class MCNode:
    def __init__(self, state, ptr):
        self.ptr = ptr
        self.wins = 0
        self.sims = 0
        self.successors = []


class GameAI:
    def __init__(self, state0, piece):
        self.root = MCNode(state0, None)
        self.piece = piece

    def expand_node(self, node):
        moves = self.get_legal_ops(node)
        for move in moves:
            state = self.sim_action(str(move), node.state)
            node.successors.append(self.create_successor(node, state))

    def sim_action(self, move, state):
        piece = self.piece
        if move == '1' and state[2][0] == '-':
            state[2][0] = piece
        elif move == '2' and state[2][1] == '-':
            state[2][1] = piece
        elif move == '3' and state[2][2] == '-':
            state[2][2] = piece
        elif move == '4' and state[1][0] == '-':
            state[1][0] = piece
        elif move == '5' and state[1][1] == '-':
            state[1][1] = piece
        elif move == '6' and state[1][2] == '-':
            state[1][2] = piece
        elif move == '7' and state[0][0] == '-':
            state[0][0] = piece
        elif move == '8' and state[0][1] == '-':
            state[0][1] = piece
        elif move == '9' and state[0][2] == '-':
            state[0][2] = piece

        return state

    @staticmethod
    def create_successor(node, state):
        child = MCNode(state, node)
        return child

    @staticmethod
    def is_leaf(node):
        if node.successors:
            return False
        else:
            return True

    def selection(self, node):
        leaf = node
        while not self.is_leaf(leaf):
            leaf = self.selection_policy(node.successors)
        return leaf

    @staticmethod
    def selection_policy(root):
        nodes = root.successors
        ucbs = []

        for node in nodes:
            if node.sims is 0:
                return node
            ucb = node.wins + (2 * math.sqrt(math.log(root.sims) / node.sims))
            ucbs.append(ucb)
        max_ucb = max(ucbs)
        best_node = nodes[ucbs.index(max_ucb)]

        return best_node

    @staticmethod
    def get_legal_ops(node):
        state = node.state
        moves = []
        legal_ops = []

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

        for i in range(moves):
            if moves[i] is True:
                legal_ops.append(str(moves[i].index() + 1))

        return legal_ops

    def rollout(self, node):
        rolling_node = node
        while not self.is_solved(rolling_node):
            rolling_node = self.rollout_policy(rolling_node)
        terminal = rolling_node
        return terminal

    def rollout_policy(self, node):
        if not node.successors:
            self.expand_node(node)
        length = node.successors.len()
        rolling_node = node.successors[np.rand.randrange[length]]
        return rolling_node

    def backprop(self):
        pass

    def search(self, root):
        # while constraint not met
        leaf = self.selection(root)
        sim_result = self.rollout(leaf)
        self.backprop(sim_result)

    @staticmethod
    def get_path(final_node):
        the_ptr = final_node.ptr
        the_path = [final_node]
        while the_ptr:
            the_path.append(the_ptr)
            the_ptr = the_ptr.ptr
        the_path.reverse()

        return the_path

    @staticmethod
    def is_solved(state):
        # Horizontals
        for row in state:
            solved = True
            first = row[0]
            for col in row:
                if col != first or first == '-':
                    solved = False
                    continue

        if solved:
            return solved

        # Verticals
        for col in state:
            solved = True
            first = col[0]
            for row in col:
                if row != first or first == '-':
                    solved = False
                    continue

        if solved:
            return solved

        # Diagonals
        first = state[0][0]
        if first == state[1][1] and first == state[2][2] and first != '-':
            solved = True
            return solved

        first = state[0][2]
        if first == state[1][1] and first == state[0][2] and first != '-':
            solved = True
            return solved

        solved = True
        for row in state:
            for col in row:
                if col is '-':
                    return False

        if solved:
            return solved

        solved = False
        return solved

    # For testing game logic before AI was implemented
    @staticmethod
    def random_move():
        move_digit = rand.randrange(1, 9)

        return str(move_digit)
