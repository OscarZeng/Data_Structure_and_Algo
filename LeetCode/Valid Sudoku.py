#When the question has fairly simple logic and you are confident about your logic
#Go and check your details since there may be silly mistakes which has nothing to do with logic
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Simply check each row, column and box, where the box is harder
        for i in range(9):
            checkRow = {"1":False, "2":False,"3":False,"4":False,"5":False,"6":False,"7":False,"8":False,"9":False}
            checkColumn = {"1":False, "2":False,"3":False,"4":False,"5":False,"6":False,"7":False,"8":False,"9":False}
            checkBox = {"1":False, "2":False,"3":False,"4":False,"5":False,"6":False,"7":False,"8":False,"9":False}
            for j in range(9):
                elementRow = board[i][j]
                elementColumn = board[j][i]
                boxRowIndex = int(i/3)*3 + int(j/3)
                boxColumnIndex = int(i%3)*3 + int(j%3)
                elementBox = board[boxRowIndex][boxColumnIndex]
                #When you are using copy and paste, always make sure that you are changing every detail for each case
                if elementRow != '.':
                    if checkRow[elementRow] == True:
                        return False
                    else:
                        checkRow[elementRow] = True
                #Try to seperate the code block which will make the code much more clear.        

                if elementColumn != '.':        
                    if checkColumn[elementColumn] == True:
                        return False
                    else:
                        checkColumn[elementColumn] = True

                if elementBox != '.':
                    if checkBox[elementBox] == True:
                        return False
                    else:
                        checkBox[elementBox] = True
        return True