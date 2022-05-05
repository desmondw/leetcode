/*
 * @lc app=leetcode id=108 lang=javascript
 *
 * [108] Convert Sorted Array to Binary Search Tree
 */

// @lc code=start
class TreeNode {
  constructor(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
  }
}
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
var sortedArrayToBST = function(nums) {
  if (!nums.length) return null
  let idx = ~~(nums.length/2)
  let node = new TreeNode(nums[idx])
  node.left = sortedArrayToBST(nums.slice(0,idx))
  node.right = sortedArrayToBST(nums.slice(idx+1))
  
  return node
};
// @lc code=end

