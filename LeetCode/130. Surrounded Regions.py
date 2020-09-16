#Own solution using DFS and searching which is a bit wordy for the explanation
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #If the region is not surrounded by X, there should be at least one block at the board line.
        #we just need to check if there is any O, if there is and it's not checked, do BFS/DFS and do the checking
        if len(board) == 0 or len(board[0]) == 0:
            return 
        m, n = len(board), len(board[0])
        boundary = []
        for i in range(m):
            boundary.append((i, 0))
            boundary.append((i, n-1))
        for j in range(1,n-1):
            boundary.append((0, j))
            boundary.append((m-1, j))
        print(boundary)
        isO = [['X']*n for _ in range(m)]
        print(isO)
        queue = []
        for ind in boundary:
            if board[ind[0]][ind[1]] == 'O':
                queue.append(ind)
        print(queue)

        while len(queue) != 0:
            index = queue.pop()
            if isO[index[0]][index[1]] == 'O':
                continue 
            isO[index[0]][index[1]] = 'O'
            if index[0] != 0 and board[index[0]-1][index[1]] == 'O':
                queue.append((index[0]-1,index[1]))
            if index[0] != m-1 and board[index[0]+1][index[1]] == 'O':
                queue.append((index[0]+1,index[1]))
            if index[1] != 0 and board[index[0]][index[1]-1] == 'O':
                queue.append((index[0],index[1]-1))
            if index[1] != n-1 and board[index[0]][index[1]+1] == 'O':
                queue.append((index[0],index[1]+1))
        print(isO)

        board[:] = isO[:]
        return
