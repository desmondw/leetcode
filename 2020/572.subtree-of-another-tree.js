/*
 * @lc app=leetcode id=572 lang=javascript
 *
 * [572] Subtree of Another Tree
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
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
var isSubtree = function(root, subRoot) {
  console.log(printTree(root))
  console.log(printTree(subRoot))
  if (!root) return false
  return printTree(root) === printTree(subRoot) || isSubtree(root.left) || isSubtree(root.right)
};

function printTree(root) {
  if (!root) return ''
  return [root.val, printTree(root.left), printTree(root.right)].join()
}
// @lc code=end

