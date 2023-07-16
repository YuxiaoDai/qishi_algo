class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        visited = set()

        def check(i, j, k):
            #print(i, j, k, board[i][j], word[k])
            if board[i][j] != word[k]:
                return False
            

            if k == len(word) - 1:
                return True
            
            visited.add((i,j))
            result = False
            for di, dj in directions:
                newi = i + di
                newj = j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]) and (newi,newj) not in visited:
                    if check(newi, newj, k + 1):
                        result = True
                        break
            visited.remove((i,j))

            return result


        for i in range(len(board)):
            for j in range(len(board[0])):
                if check(i,j,0):
                    return True
        return False