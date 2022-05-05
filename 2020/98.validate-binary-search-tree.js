/*
 * @lc app=leetcode id=98 lang=javascript
 *
 * [98] Validate Binary Search Tree
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

//    2
//  1   3

//     5
//   4   6
// n n  3 7

//    1
//  1   n

/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function(root, min=null, max=null) {
  if (!root) return true
  if ((min != null && root.val <= min) || (max != null && root.val >= max)) {
    return false
  }

  let left = isValidBST(root.left, min, root.val)
  let right = isValidBST(root.right, root.val, max)
  return left && right
};
// @lc code=end

