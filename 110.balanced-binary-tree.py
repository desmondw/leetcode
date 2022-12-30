#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBalancedTree(root) >= 0

    def isBalancedTree(self, root: TreeNode, depth=2) -> list:
        if not root:
            return depth
        depth += 1

        left = self.isBalancedTree(root.left, depth)
        right = self.isBalancedTree(root.right, depth)

        if abs(left - right) > 1:
            return float('-inf')

        return max(left, right)
# @lc code=end