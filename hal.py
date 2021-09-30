import random as rand
import numpy as np
import math
import time


class MCNode:
    def __init__(self, state, ptr, piece, move=None):
        self.ptr = ptr
        self.state = state
        self.move = move
        self.piece = piece
        self.wins = 0
        self.sims = 0
        self.successors = []


class GameAI:
    def __init__(self, state0, piece):
        self.root = MCNode(state0, None, piece)
        self.piece = piece
        self.current = self.root
        self.is_draw = False

    def expand_node(self, node):
        moves = self.get_legal_ops(node)
        for move in moves:
            state = self.sim_action(str(move), node.state, node.piece)
            node.successors.append(self.create_successor(node, state, move))

    def sim_action(self, move, state, piece):
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

    def create_successor(self, node, state, move):
        piece = self.swap_piece(node)
        child = MCNode(state, node, piece, str(move))
        return child

    @staticmethod
    def swap_piece(node):
        piece = node.piece
        if piece is 'x':
            return 'o'
        elif piece is 'o':
            return 'x'

    @staticmethod
    def is_leaf(node):
        if len(node.successors) > 0:
            return False
        else:
            return True

    def selection(self, node):
        leaf = node
        while not self.is_leaf(leaf):
            leaf = self.selection_policy(node.successors)
        self.current = leaf
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

        for i in range(9):
            moves.append(False)

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

        for i in range(len(moves)):
            if moves[i] is True:
                legal_ops.append(str(i + 1))

        return legal_ops

    def rollout(self, node):
        rolling_node = node
        while not self.is_solved(rolling_node.state):
            rolling_node = self.rollout_policy(rolling_node)
        terminal = rolling_node
        return terminal

    def rollout_policy(self, node):
        if not node.successors:
            self.expand_node(node)
        length = len(node.successors)
        random_index = rand.randrange(length)
        rolling_node = node.successors[random_index]
        return rolling_node

    def backprop(self, terminal):
        self.current.sims += 1

        if self.is_draw:
            self.current.wins += 1
        elif terminal.piece == self.piece:
            self.current.wins += 2

        self.is_draw = False

        parent = self.current.ptr
        child = self.current

        print("parent node: ", parent)

        while parent.ptr is not None:
            parent.sims += 1
            parent.wins += child.wins
            child = parent
            parent = child.ptr

    def search(self, state, piece):
        # while constraint not met
        root = MCNode(state, None, piece)
        i = 0
        while i < 1000:
            leaf = self.selection(root)
            sim_result = self.rollout(leaf)
            self.backprop(sim_result)
            i += 1

        scores = []
        for node in root.successors:
            scores.append(node.win / node.sims)
        hi_score = max(scores)

        return root.successors[scores.index(hi_score)].move

    @staticmethod
    def get_path(final_node):
        the_ptr = final_node.ptr
        the_path = [final_node]
        while the_ptr:
            the_path.append(the_ptr)
            the_ptr = the_ptr.ptr
        the_path.reverse()

        return the_path

    def is_solved(self, state):
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
            self.is_draw = True
            return solved

        solved = False
        return solved

    # For testing game logic before AI was implemented
    @staticmethod
    def random_move():
        move_digit = rand.randrange(1, 9)

        return str(move_digit)
