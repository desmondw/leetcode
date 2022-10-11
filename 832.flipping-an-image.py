#
# @lc app=leetcode id=832 lang=python3
#
# [832] Flipping an Image
#

# @lc code=start
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        i2 = []
        for row in image:
            row.reverse()
            r2=[]
            for c in row:
                r2.append(1 if c == 0 else 0)
            i2.append(r2)
        return i2
# @lc code=end

