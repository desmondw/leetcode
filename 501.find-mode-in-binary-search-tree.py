#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        vals = self.getVals(root)
        freq = {}
        for val in vals:
            if val not in freq:
                freq[val] = 0
            freq[val] += 1

        highest = 0
        tops = []
        for n, f in freq.items():
            if f > highest:
                highest = f
                tops = [n]
            elif f == highest:
                tops.append(n)
        return tops

    def getVals(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        left = self.getVals(root.left)
        right = self.getVals(root.right)

        return [root.val] + left + right
# @lc code=end

