#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsSorted = {}
        for str in strs:
            srt = ''.join(sorted(str))
            if srt not in strsSorted:
                strsSorted[srt] = []
            strsSorted[srt].append(str)
        return strsSorted.values()
# @lc code=end

