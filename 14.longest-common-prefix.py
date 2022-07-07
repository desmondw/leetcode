#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        base = strs[0]
        for word in strs[1:]:
            if len(base) > len(word):
                base = base[:len(word)]
            for i in range(len(base)-1,-1,-1):
                if base[i] != word[i]:
                    base = base[:i]
                if not base:
                    return ''
        return base
# @lc code=end

