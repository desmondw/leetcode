#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        cur = []
        for num in nums:
            if len(cur) and cur[-1] != num - 1:
                ranges.append(self.rangeToText(cur))
                cur = []
            cur.append(num)
        if len(cur):
            ranges.append(self.rangeToText(cur))

        return ranges

    def rangeToText(self, arr):
        # resolve range
        text = str(arr[0])
        if len(arr) > 1:
            text += f'->{arr[-1]}'
        return text
# @lc code=end

