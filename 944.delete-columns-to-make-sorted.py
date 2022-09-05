#
# @lc app=leetcode id=944 lang=python3
#
# [944] Delete Columns to Make Sorted
#

# @lc code=start
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for col in range(len(strs[0])):
            s = ''
            for row in range(len(strs)):
                s += strs[row][col]
            if s != ''.join(sorted(s)):
                count += 1
        return count
# @lc code=end

