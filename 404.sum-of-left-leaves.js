/*
 * @lc app=leetcode id=404 lang=javascript
 *
 * [404] Sum of Left Leaves
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var sumOfLeftLeaves = function(node) {
  if (!node) return 0
  let leftVal = 0
  if (node.left && !node.left.left && !node.left.right) leftVal = node.left.val
  return leftVal + sumOfLeftLeaves(node.left) + sumOfLeftLeaves(node.right)
};
// @lc code=end

