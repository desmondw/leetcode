#
# @lc app=leetcode id=2418 lang=python3
#
# [2418] Sort the People
#

# @lc code=start
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        foo = list(zip(names, heights))
        foo.sort(key=lambda v: -v[1])
        return [name for (name, _) in foo]
# @lc code=end

