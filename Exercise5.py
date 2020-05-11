# TODO Shortest path for king on chess board
def mapping(x):
    if x == 0:
        return ' □ '
    if x == -1:
        return ' x '
    if x == ' k ':
        return ' ♔ '
    if x == ' t ':
        return ' ◎ '


# class King:
#     IMG = (' ♔ ')
#
#     def __str__(self):
#         return self.IMG


class ChessBoard:

    def __init__(self):
        self.board = []
        self.mapped_board = []
        self.king_position = []
        self.target_position = []
        for i in range(8):
            row = [0] * 8
            mapped_row = list(map(mapping, row))
            self.board.append(row)
            self.mapped_board.append(mapped_row)

    def __repr__(self):
        temp = []
        for row in self.board:
            mapped_row = list(map(mapping, row))
            temp.append(mapped_row)

        result = ''
        for row in temp:
            result += ''.join(row) + "\n"

        return result

    def setup_king(self, x, y):
        self.king_position = [x, y]
        self.board[x][y] = ' k '

    def setup_target(self, x, y):
        self.target_position = [x, y]
        self.board[x][y] = ' t '

    def find_legal_moves(self, x, y):
        legal_moves = []
        self.king_position = [2, 2]
        # x = king_position[0]
        # y = king_position[1]
        pom = [-1, 0, 1]
        for i in pom:
            for j in pom:
                if not ((i == j == 0) or (x + i < 0) or (x + i > 7) or (y + j < 0) or (y + j > 7) or self.board[x + i][
                    y + j] < 0):
                    legal_moves.append([x + i, y + j])
        return legal_moves

    def search_shortest_path(self):
        range_board = self.board.copy()
        range_board[self.target_position[0]][self.target_position[1]] = 0
        range_board[self.king_position[0]][self.king_position[1]] = 0
        queue = []
        queue.append(self.king_position)
        visited = [[False for i in range(8)]
                   for j in range(8)]
        # visited[self.king_position[0]][self.king_position[1]] = True

        while (len(queue) > 0):
            t = queue[0]
            queue.pop(0)
            if (t[0] == self.target_position[0] and t[1] == self.target_position[1]):
                return range_board[t[0]][t[1]]
            for i in range(8):
                if not visited[t[0]][t[1]]:
                    visited[t[0]][t[1]] = True
                    for item in self.find_legal_moves(t[0], t[1]):
                        if not visited[item[0]][item[1]]:
                            queue.append(item)
                            if not (range_board[item[0]][item[1]] > 0):
                                range_board[item[0]][item[1]] = range_board[t[0]][t[1]] + 1
    def show_path(self):
        for i in range(self.search_shortest_path()):



chess_board = ChessBoard()
chess_board.board[1][1] = -1
chess_board.board[4][4] = -1
chess_board.board[3][4] = -1
chess_board.board[5][4] = -1
chess_board.board[6][4] = -1
chess_board.board[4][5] = -1
chess_board.board[4][6] = -1
chess_board.board[6][5] = -1
chess_board.setup_king(2, 2)
chess_board.setup_target(5, 5)
# print(chess_board)
print('Result:')
chess_board.search_shortest_path()
print(chess_board.search_shortest_path())

#
# def get_king_position(self):
#     king = ' ♔ '
#     for item in self.board:
#         for i in range(len(item)):
#             if item[i] == king:
#                 current_position = [self.board.index(item), item.index(king)]
#                 return current_position
#
# def find_legal_moves(self):
#     legal_moves = []
#     king_position = self.get_king_position()
#     x = king_position[0]
#     y = king_position[1]
#     pom = [-1, 0, 1]
#     for i in pom:
#         for j in pom:
#             if not ((i == j == 0) or (x + i < 0) or (x + i > 7) or (y + j < 0) or (y + j > 7)):
#                 legal_moves.append([x+i, y+j])
#     return legal_moves
#
#
#
#
#
#
# chess_board = ChessBoard()
#
# chess_board.setup_king(4,3)
# print(chess_board)
#
# print(chess_board.get_king_position())
#
#
#
# chess_board = ChessBoard()
#
# chess_board.setup_king(7,7)
# print(chess_board)
#
# print(chess_board.get_king_position())
#
# print(chess_board.find_legal_moves())
