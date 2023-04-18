#
# @lc app=leetcode id=1337 lang=python3
#
# [1337] The K Weakest Rows in a Matrix
#

# @lc code=start
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        mapd = {}
        for i, row in enumerate(mat):
            n = row.count(1)
            if n not in mapd:
                mapd[n] = []
            mapd[n].append(i)

        keys = sorted(mapd.keys())
        vals = [idx for key in keys for idx in mapd[key]]
        return vals[:k]

# @lc code=end

