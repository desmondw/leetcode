/*
 * @lc app=leetcode id=103 lang=javascript
 *
 * [103] Binary Tree Zigzag Level Order Traversal
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
var zigzagLevelOrder = function(root) {
  let values = traverse(root, 0)
  return values.map((v,i)=>i%2==0?v:v.reverse())
};

let traverse = function(node, level=0) {
  if (!node) return new Array(level)
  
  let left = traverse(node.left, level+1)
  let right = traverse(node.right, level+1)
  let zip = []

  // zip arrays
  while (left.length || right.length) {
    zip.push([ ...left.shift()??[], ...right.shift()??[] ])
  }
  zip[level] = [ ...zip[level], node.val ]
  
  return zip
};
// @lc code=end

