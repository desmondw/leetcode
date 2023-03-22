#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not self.isPalindrome(s):
            while 1 < len(s):
                if s[0] != s[-1]:
                    return self.isPalindrome(s[1:]) or self.isPalindrome(s[:-1])
                s = s[1:-1]
        return True

    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-z0-9]','',s.lower())
        return s == s[::-1]

# @lc code=end

