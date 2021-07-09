/*
 * @lc app=leetcode id=563 lang=javascript
 *
 * [563] Binary Tree Tilt
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
var findTilt = function(root) {
  if (!root) return 0

  let tilt = Math.abs(getSum(root.left) - getSum(root.right))

  return tilt + findTilt(root.left) + findTilt(root.right)
};

var getSum = function(root) {
  if (!root) return 0

  let left = getSum(root.left)
  let right = getSum(root.right)

  return root.val + left + right
};
// @lc code=end

