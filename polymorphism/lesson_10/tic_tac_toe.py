from easy import Easy
from normal import Normal


class TicTacToe:
    MAPPING = {'easy': Easy,
               'normal': Normal}

    def __init__(self, level='easy'):
        self.field = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.level = level

    def go(self, col=5, row=5):
        if col != 5:
            self.field[col][row] = 'player'
        else:
            col, row = self.MAPPING[self.level].go(self.field)
            self.field[col][row] = 'bot'
        return self.test_victory()

    def test_victory(self):
        victory_list = [
            [[0, 0], [0, 1], [0, 2]],
            [[1, 0], [1, 1], [1, 2]],
            [[2, 0], [2, 1], [2, 2]],
            [[0, 0], [1, 0], [2, 0]],
            [[0, 1], [1, 1], [2, 1]],
            [[0, 2], [1, 2], [2, 2]],
            [[0, 0], [1, 1], [2, 2]],
            [[2, 0], [1, 1], [0, 2]],
                        ]
        player = []
        bot = []
        for col_index, col in enumerate(self.field):
            for row_index, row in enumerate(col):
                if row == 'player':
                    player.append([col_index, row_index])
                if row == 'bot':
                    bot.append([col_index, row_index])

        for elem in victory_list:
            if sorted(player) == sorted(elem):
                return True
            if len(bot) > 3:
                print(elem)
                a = 0
                for value in elem:
                    if value in bot:
                        a += 1
                        if a == 3:
                            return True
            if sorted(bot) == sorted(elem):
                return True
        return False


game = TicTacToe('normal')
game.go(0, 2)
game.go()
game.go(0, 1)
assert not game.go()
assert not game.go(1, 2)
is_winner = game.go()
assert is_winner

game = TicTacToe('normal')
game.go()
game.go(2, 1)
game.go()
game.go(1, 0)
assert not game.go()
assert not game.go(1, 2)
is_winner = game.go()
assert is_winner
