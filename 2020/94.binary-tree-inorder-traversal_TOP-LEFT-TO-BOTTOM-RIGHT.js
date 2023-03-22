/*
 * @lc app=leetcode id=94 lang=javascript
 *
 * [94] Binary Tree Inorder Traversal
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
 * @return {number[]}
 */
 var inorderTraversal = function(root) {
  let valsByOffset = traverse(root, 0)
  console.log(valsByOffset)
  let valsSortedByOffset = Object.entries(valsByOffset).sort((a,b)=>a[0]-b[0])
  console.log(valsSortedByOffset)
  console.log(valsSortedByOffset.map(v=>v[1]))
  console.log(valsSortedByOffset.map(v=>v[1]).flat())
  // return valsSortedByOffset.map(v=>v[1]).sort((a,b)=>a-b)).flat()
  return valsSortedByOffset.map(v=>v[1]).flat()
};

function traverse(node, offset) {
  if (!node) return {}

  let zip = { }
  let left = traverse(node.left, offset-1)
  let center = { [offset]: [node.val] }
  let right = traverse(node.right, offset+1)

  // zip
  Object.entries(left).forEach(([k,v])=>{ zip[k] = [...zip[k]??[], ...v] })
  Object.entries(center).forEach(([k,v])=>{ zip[k] = [...zip[k]??[], ...v] })
  Object.entries(right).forEach(([k,v])=>{ zip[k] = [...zip[k]??[], ...v] })
  
  return zip
}
// @lc code=end

