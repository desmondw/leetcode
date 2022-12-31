#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if not (root.left or root.right):
            return 1
        depths = self.minDepthTree(root)
        return min(depths)

    def minDepthTree(self, root: TreeNode, depth=0) -> list:
        if not root:
            return []
        depth += 1

        left = self.minDepthTree(root.left, depth)
        right = self.minDepthTree(root.right, depth)
        if (len(left) + len(right)) == 0:
            return [depth]

        return left + right
# @lc code=end

