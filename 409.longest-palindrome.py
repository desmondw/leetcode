#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash = {}
        total = 0

        for c in s:
            if c not in hash: hash[c] = 0
            hash[c] += 1
            if hash[c] == 2:
                del hash[c]
                total += 2
        if len(hash): total += 1
        return total

# @lc code=end

