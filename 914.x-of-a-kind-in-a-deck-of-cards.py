#
# @lc app=leetcode id=914 lang=python3
#
# [914] X of a Kind in a Deck of Cards
#

# @lc code=start
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        hash = {}
        for card in deck:
            if card not in hash:
                hash[card] = 0
            hash[card] += 1

        nums = list(hash.values())
        nums.sort()
        if nums[0] == 1: return False

        for denom in range(2, nums[0]+1):
            gucci = True
            for num in nums:
                if num % denom:
                    gucci = False
                    break
            if gucci: return True
        return False

    # def getLowestCommonDenominator(n1, n2):

# @lc code=end

