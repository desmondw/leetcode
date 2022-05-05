/*
 * @lc app=leetcode id=102 lang=javascript
 *
 * [102] Binary Tree Level Order Traversal
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
 * @return {number[][]}
 */

var levelOrder = function(node) {
  let levels = []
  let i=1
  while(true) {
    let level = levelArray(node, i)
    if (!level.length) return levels
    levels.push(level)
    i++
  }
}

var levelArray = function(node, target, depth=1) {
  if (!node) return []
  if (target === depth) return [node.val]
  let left = levelArray(node.left, target, depth+1)
  let right = levelArray(node.right, target, depth+1)
  return [...left, ...right]
}
// @lc code=end

