#
# @lc app=leetcode id=1302 lang=python3
#
# [1302] Deepest Leaves Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        return self._deepestLeavesSum(root)[1]

    def _deepestLeavesSum(self, node: Optional[TreeNode], depth=0):
        if not node:
            return (-1, 0)

        if not node.left and not node.right:
            return (depth, node.val)

        left = self._deepestLeavesSum(node.left, depth+1)
        right = self._deepestLeavesSum(node.right, depth+1)

        if left[0] == right[0]:
            return (left[0], left[1] + right[1])
        elif left[0] < right[0]:
            return right
        return left
# @lc code=end

