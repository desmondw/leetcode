#
# @lc app=leetcode id=1773 lang=python3
#
# [1773] Count Items Matching a Rule
#

# @lc code=start
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        key = -1
        if   ruleKey == 'type':  key = 0
        elif ruleKey == 'color': key = 1
        elif ruleKey == 'name':  key = 2
        return len(list(filter(lambda v: v[key] == ruleValue, items)))
# @lc code=end

