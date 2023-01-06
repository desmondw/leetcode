#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode], content='') -> List[str]:
        if not root:
            return []

        content += '->' + str(root.val)
        if not root.left and not root.right:
            return [content[2:]]

        left = self.binaryTreePaths(root.left, content)
        right = self.binaryTreePaths(root.right, content)

        return left + right

# @lc code=end

