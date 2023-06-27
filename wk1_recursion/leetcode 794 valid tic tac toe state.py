class Solution:
    def win(self, board: List[str], p: str) -> bool:
        return any(board[i][0] == p and board[i][1] == p and board[i][2] == p or
                   board[0][i] == p and board[1][i] == p and board[2][i] == p for i in range(3)) or \
                   board[0][0] == p and board[1][1] == p and board[2][2] == p or \
                   board[0][2] == p and board[1][1] == p and board[2][0] == p

    def validTicTacToe(self, board: List[str]) -> bool:
        o_count = sum(row.count('O') for row in board)
        x_count = sum(row.count('X') for row in board)
        result = not(o_count != x_count and o_count != x_count - 1 or
                     o_count != x_count and self.win(board, 'O') or
                     o_count != x_count - 1 and self.win(board, 'X'))
        return result
