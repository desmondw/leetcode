#
# @lc app=leetcode id=1742 lang=python3
#
# [1742] Maximum Number of Balls in a Box
#

# @lc code=start
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = {}

        for ball in range(lowLimit, highLimit+1):
            box = sum([int(x) for x in list(str(ball))])
            if not box in boxes:
                boxes[box] = 0
            boxes[box] += 1

        return max(boxes.values())

# @lc code=end

