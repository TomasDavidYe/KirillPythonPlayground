# TODO
# Create a class ChessBoard which has a filed n = dimension of the board
# Let 'O' character represent an empty field
# Let 'X' character represent an blocked field
# The ChessBoard, after initialization should have all fields empty
# The chess board should implment a method block(x, y) to block a field with coordinates (x, y)
# The chess board should implment a method print() to display the board on the console

class ChessBoard:
    def __init__(self, n, board = []):
        self.demension = n
        self.board = board

    def print_board(self):
        for i in range(self.demension):
            print('{}'.format(self.board[i]))

    def initialize_chessboard(self):
        row = ['0'] * self.demension
        for i in range(self.demension):
            row = row.copy()
            self.board.append(row)
        self.print_board()

    def block_cell(self, x, y):
        self.board[y][x] = 'X'
        self.print_board()

    def unblock_cell(self, x, y):
        self.board[y][x] = '0'
        self.print_board()


chess_board = ChessBoard(5)
