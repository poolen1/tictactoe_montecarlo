

class Game:
    def __init__(self):
        self.rows = 3
        self.cols = 3
        self.game_state = []
        self.init_board()

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
        player = '1'
        print("Start player: ", start_player)

    def player_move(self):
        pass
    
    def ai_move(self):
        pass

    def print_board(self):
        for row in self.game_state:
            print(row)

    def is_solved(self, player):
        solved = True
        for row in self.game_state:
            first = row[0]
            for col in row:
                if col != first:
                    solved = False
                    continue

        if solved:
            return solved
