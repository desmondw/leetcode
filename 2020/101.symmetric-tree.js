/*
 * @lc app=leetcode id=101 lang=javascript
 *
 * [101] Symmetric Tree
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
 * @return {boolean}
 */
var isSymmetric = function(root) {
  if (!root) return true
  let left = getNodes(root.left, true, false)
  let right = getNodes(root.right, false, true)
  console.log(left)
  console.log(right)
  return left.join() == right.reverse().join()
};

function getNodes(node, isLeft, flip) {
  if (!node) return [null]
  let left = getNodes(node.left, true, flip)
  let right = getNodes(node.right, false, flip)
  let meta = flip ? !isLeft : isLeft
  return [...left, [node.val, meta], ...right]
}
// @lc code=end

