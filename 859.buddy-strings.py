#
# @lc app=leetcode id=859 lang=python3
#
# [859] Buddy Strings
#

# @lc code=start
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            ss = sorted(s)
            for i in range(1,len(ss)):
                if ss[i-1] == ss[i]:
                    return True
            return False

        badIndexes = []
        for i,c in enumerate(s):
            if (c != goal[i]):
                badIndexes.append(i)
            if len(badIndexes) > 2:
                return False

        if len(badIndexes) < 2:
            return False

        i,i2 = badIndexes
        s2 = s[:i] + s[i2] + s[i+1:i2] + s[i] + s[i2+1:]

        return s2 == goal
# @lc code=end

