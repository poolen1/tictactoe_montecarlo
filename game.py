import hal


class Game:
    def __init__(self):
        self.rows = 3
        self.cols = 3
        self.game_state = []
        self.init_board()
        self.computer = None
        self.is_draw = False

    def init_board(self):
        for row in range(self.rows):
            game_row = []
            for col in range(self.cols):
                game_row.append('-')
            self.game_state.append(game_row)

    def start_game(self):
        print("Welcome to Tic Tac Toe")
        print("Press 1 to play as x")
        print("Press 2 to play as o")
        print("Press 3 to exit")
        val = input()

        if val == '3':
            exit()
        elif val == '1':
            self.play_game(val)
        elif val == '2':
            self.play_game(val)

    def play_game(self, start_player):
        if start_player == '1':
            self.player_move('x')
            self.computer = hal.GameAI(self.game_state, 'o')
            while True:
                self.ai_move('o')
                self.player_move('x')
        elif start_player == '2':
            self.computer = hal.GameAI(self.game_state, 'x')
            while True:
                self.ai_move('x')
                self.player_move('o')

    def player_move(self, piece):
        valid = False
        while not valid:
            space = input("Enter space to move to: ")
            valid = self.place_piece(space, piece)

        self.print_board()
        solved = self.is_solved()
        if solved:
            if self.is_draw:
                print("Cat's game!")
                exit()
            print("Player wins!")
            exit()

    # random AI move
    '''
        def ai_move(self, piece):
        valid = False
        while not valid:
            print("computer moving...")
            space = self.computer.random_move()
            valid = self.place_piece(space, piece)

        self.print_board()
        solved = self.is_solved()
        if solved:
            if self.is_draw:
                print("Cat's game!")
                exit()
            print("Computer wins!")
            exit()
    '''
    # Actual AI move
    def ai_move(self, piece):
        valid = False
        while not valid:
            print("computer moving...")
            space = self.computer.search(self.game_state, piece)
            valid = self.place_piece(space, piece)

        self.print_board()
        solved = self.is_solved()
        if solved:
            if self.is_draw:
                print("Cat's game!")
                exit()
            print("Computer wins!")
            exit()

    def place_piece(self, move, piece):
        is_valid = True
        if move == '1' and self.game_state[2][0] == '-':
            self.game_state[2][0] = piece
        elif move == '2' and self.game_state[2][1] == '-':
            self.game_state[2][1] = piece
        elif move == '3' and self.game_state[2][2] == '-':
            self.game_state[2][2] = piece
        elif move == '4' and self.game_state[1][0] == '-':
            self.game_state[1][0] = piece
        elif move == '5' and self.game_state[1][1] == '-':
            self.game_state[1][1] = piece
        elif move == '6' and self.game_state[1][2] == '-':
            self.game_state[1][2] = piece
        elif move == '7' and self.game_state[0][0] == '-':
            self.game_state[0][0] = piece
        elif move == '8' and self.game_state[0][1] == '-':
            self.game_state[0][1] = piece
        elif move == '9' and self.game_state[0][2] == '-':
            self.game_state[0][2] = piece
        else:
            is_valid = False

        return is_valid

    def is_valid(self, move):
        is_valid = True
        if move == '1' and self.game_state[2][0] == '-':
            pass
        elif move == '2' and self.game_state[2][1] == '-':
            pass
        elif move == '3' and self.game_state[2][2] == '-':
            pass
        elif move == '4' and self.game_state[1][0] == '-':
            pass
        elif move == '5' and self.game_state[1][1] == '-':
            pass
        elif move == '6' and self.game_state[1][2] == '-':
            pass
        elif move == '7' and self.game_state[0][0] == '-':
            pass
        elif move == '8' and self.game_state[0][1] == '-':
            pass
        elif move == '9' and self.game_state[0][2] == '-':
            pass
        else:
            is_valid = False

        return is_valid

    def print_board(self):
        for row in self.game_state:
            print(row)

    def is_solved(self):
        # Horizontals
        for row in self.game_state:
            solved = True
            first = row[0]
            for col in row:
                if col != first or first == '-':
                    solved = False
                    continue

        if solved:
            return solved

        # Verticals
        for col in self.game_state:
            solved = True
            first = col[0]
            for row in col:
                if row != first or first == '-':
                    solved = False
                    continue

        if solved:
            return solved

        # Diagonals
        first = self.game_state[0][0]
        if first == self.game_state[1][1] and first == self.game_state[2][2] and first != '-':
            solved = True
            return solved

        first = self.game_state[0][2]
        if first == self.game_state[1][1] and first == self.game_state[0][2] and first != '-':
            solved = True
            return solved

        solved = True
        for row in self.game_state:
            for col in row:
                if col is '-':
                    return False

        if solved:
            self.is_draw = True
            return solved

        solved = False
        return solved
