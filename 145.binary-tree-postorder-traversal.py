#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root or not root.val: return []
        arr = []
        arr += self.postorderTraversal(root.left)
        arr += self.postorderTraversal(root.right)
        arr += [root.val]
        return arr
# @lc code=end

