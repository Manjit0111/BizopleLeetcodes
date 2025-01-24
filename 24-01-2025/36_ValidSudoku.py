class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        answer=[]
        for i in range(len(board)):
            for j in range(len(board)):
                element=board[i][j]
                if element!='.':
                    answer+=[(i,element),(element,j),(i//3,j//3,element)]
        return len(answer)==len(set(answer))