#
# @lc app=leetcode id=999 lang=python3
#
# [999] Available Captures for Rook
#

# @lc code=start
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        pos = {}
        for i, row in enumerate(board):
            if "R" in row:
                pos['x'] = row.index("R")
                pos['y'] = i
                break
        col = []
        for i in range(len(board)):
            col.append(board[i][pos['x']])

        row = ''.join(board[pos['y']]).replace('.','')
        col = ''.join(col).replace('.','')

        count = 0
        rowRook = row.index("R")
        colRook = col.index("R")

        if rowRook > 0 and row[rowRook-1] == 'p':          count+=1
        if rowRook < len(row)-1 and row[rowRook+1] == 'p': count+=1
        if colRook > 0 and col[colRook-1] == 'p':          count+=1
        if colRook < len(col)-1 and col[colRook+1] == 'p': count+=1

        return count
# @lc code=end

