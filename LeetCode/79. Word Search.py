class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        #Here we check every possible starting point
        for i in range(m):
            for j in range(n):
                if self.check(board, i, j, word):
                    return True
        return False
        
    def check(self, board, rowIdx, columnIdx, word):
        if len(word) == 0:
            return True
        #Check whether the index out of range
        if rowIdx<0 or rowIdx>=len(board) or columnIdx<0 or columnIdx >= len(board[0]):
            return False

        #Here list is immutable object, we need to undo the change once we have modified the board
        firstLetter = word[0]
        if firstLetter != board[rowIdx][columnIdx]:
            return False
        temp = board[rowIdx][columnIdx]
        board[rowIdx][columnIdx] = -1
        ans = self.check(board, rowIdx-1,columnIdx,word[1:]) or self.check(board, rowIdx+1,columnIdx,word[1:]) or self.check(board, rowIdx,columnIdx-1,word[1:]) or self.check(board, rowIdx,columnIdx+1,word[1:])
        board[rowIdx][columnIdx] = temp
        return ans
        
