#
# @lc app=leetcode id=1160 lang=python3
#
# [1160] Find Words That Can Be Formed by Characters
#

# @lc code=start
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total = 0
        for word in words:
            dupe = list(word[:])
            for c in chars:
                if c in dupe:
                    dupe.remove(c)
                if not len(dupe):
                    total += len(word)
                    break
        return total
# @lc code=end

