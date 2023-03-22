#
# @lc app=leetcode id=1441 lang=python3
#
# [1441] Build an Array With Stack Operations
#

# @lc code=start
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        iTarget = 0
        ops = []
        j=0
        while j < n and iTarget < len(target):
            num = target[iTarget]
            lastNum = target[iTarget-1] if iTarget > 0 else 0
            numDiff = num - lastNum
            for _ in range(1, numDiff):
                ops.append('Push')
                ops.append('Pop')
            ops.append('Push')
            iTarget += 1
            j += 1

        return ops
# @lc code=end

