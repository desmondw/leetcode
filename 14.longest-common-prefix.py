#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0: return ""
        base = strs[0]

        for str in strs:
            for i,letter in enumerate(base):
                if i >= len(str) or letter != str[i]:
                    base = base[:i]
                    if len(base) == 0: return ""
                    break
        return base
            

        
# @lc code=end

sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))
print(sol.longestCommonPrefix(["ab","a"]))