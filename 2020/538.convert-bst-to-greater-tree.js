/*
 * @lc app=leetcode id=538 lang=javascript
 *
 * [538] Convert BST to Greater Tree
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
 * @return {TreeNode}
 */
var convertBST = function(root) {
  convert(root)
  return root
};
var convert = function(node, total=0) {
  if (!node) return total
  
  total = convert(node.right, total)
  node.val += total
  total = node.val
  total = convert(node.left, total)
  
  return total
};
// @lc code=end

