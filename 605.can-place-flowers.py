#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i=0
        while i < len(flowerbed):
            pre = flowerbed[i-1] if i>0 else 0
            post = flowerbed[i+1] if i<len(flowerbed)-1 else 0
            if pre == flowerbed[i] == post == 0:
                n-=1
                if n <= 0: return True
                i+=1
            i+=1
        return n <= 0
# @lc code=end

