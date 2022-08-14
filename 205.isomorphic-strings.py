#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        shash = {}
        thash = {}
        for i in range(len(s)):
            sv = s[i]
            tv = t[i]
            if sv in shash:
                if shash[sv] == tv: continue
                else: return False
            elif tv in thash:
                return False

            shash[sv] = tv
            thash[tv] = sv
        return True

# @lc code=end

