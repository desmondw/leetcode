#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(0, len(s))[::-1]:
            c1 = s[i]
            lastIndexes = [j+i for j, c2 in enumerate(s[i:]) if c1 == c2]
            for j in lastIndexes:
                substring = s[i:j+1]
                if self.isPalindrome(substring):
                    count += 1
        return count

    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]

# @lc code=end

