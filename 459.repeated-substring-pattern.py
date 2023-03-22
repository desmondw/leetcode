#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(int(len(s)/2)):
            sub = s[:i+1]
            if sub not in s[i+1:]:
                return False

            failed = False
            for i in range(0, len(s), len(sub)):
                part = s[i:i+len(sub)]
                if sub != part:
                    failed = True
                    break
            if not failed:
                return True
        return False

# @lc code=end

