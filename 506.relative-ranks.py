#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#

# @lc code=start
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scored = [[i,v] for i, v in enumerate(score)]
        scored.sort(key=lambda o: -o[1])
        for place, o in enumerate(scored):
            place = str(place+1)
            if place == '1': place = "Gold Medal"
            if place == '2': place = "Silver Medal"
            if place == '3': place = "Bronze Medal"
            score[o[0]] = place

        return score

# @lc code=end

