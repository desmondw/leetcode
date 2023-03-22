#
# @lc app=leetcode id=1475 lang=python3
#
# [1475] Final Prices With a Special Discount in a Shop
#

# @lc code=start
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(0,len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break

        return prices
# @lc code=end

