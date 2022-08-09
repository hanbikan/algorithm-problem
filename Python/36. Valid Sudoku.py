class Solution:
    def isValidSudoku(self, board):
        for row in board:
            if not self.isVaildList(row): return False
        for column in zip(*board):
            if not self.isVaildList(column): return False
        for sect_x in range(3):
            for sect_y in range(3):
                x1,y1,x2,y2 = sect_x*3, sect_y*3, sect_x*3+2, sect_y*3+2
                tmp = []
                for x in range(x1, x2+1):
                    for y in range(y1, y2+1):tmp.append(board[x][y])
                print(tmp)
                if not self.isVaildList(tmp): return False
        return True
    def isVaildList(self, List):
        unit = [i for i in List if i != '.']
        if len(unit) == len(set(unit)): return True
        else: return False

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
s = Solution()
print(s.isValidSudoku(board))