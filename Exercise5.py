#TODO Shortest path for king on chess board
class King:
    IMG = (' ♔ ')

    def __str__(self):
        return self.IMG


class ChessBoard:
    def __init__(self):
        self.board = []
        for i in range(8):
            row = [' □ '] * 8
            self.board.append(row)

    def __str__(self):
        result = ''
        for i in range(8):
            result += ''.join(map(str, self.board[i])) + "\n"
        return result

    def setup_king(self, x, y):
        self.board[x][y] = ' ♔ '

    def get_king_position(self):
        king = ' ♔ '
        for item in self.board:
            for i in range(len(item)):
                if item[i] == king:
                    current_position = [self.board.index(item), item.index(king)]
                    return current_position

    def find_legal_moves(self):
        legal_moves = []
        king_position = self.get_king_position()
        x = king_position[0]
        y = king_position[1]
        pom = [-1, 0, 1]
        for i in pom:
            for j in pom:
                if not i == j == 0:
                    legal_moves.append([x+i, y+j])
        return legal_moves


#TODO Shortest path for king on chess board
class King:
    IMG = (' ♔ ')

    def __str__(self):
        return self.IMG


class ChessBoard:
    def __init__(self):
        self.board = []
        for i in range(8):
            row = [' □ '] * 8
            self.board.append(row)

    def __str__(self):
        result = ''
        for i in range(8):
            result += ''.join(map(str, self.board[i])) + "\n"
        return result

    def setup_king(self, x, y):
        self.board[x][y] = ' ♔ '

    def get_king_position(self):
        king = ' ♔ '
        for item in self.board:
            for i in range(len(item)):
                if item[i] == king:
                    current_position = [self.board.index(item), item.index(king)]
                    return current_position

    def find_legal_moves(self):
        legal_moves = []
        king_position = self.get_king_position()
        x = king_position[0]
        y = king_position[1]
        pom = [-1, 0, 1]
        for i in pom:
            for j in pom:
                if not ((i == j == 0) or (x + i < 0) or (x + i > 7) or (y + j < 0) or (y + j > 7)):
                    legal_moves.append([x+i, y+j])
        return legal_moves






chess_board = ChessBoard()

chess_board.setup_king(4,3)
print(chess_board)

print(chess_board.get_king_position())



chess_board = ChessBoard()

chess_board.setup_king(7,7)
print(chess_board)

print(chess_board.get_king_position())

print(chess_board.find_legal_moves())