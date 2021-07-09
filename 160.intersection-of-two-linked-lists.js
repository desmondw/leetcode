/*
 * @lc app=leetcode id=160 lang=javascript
 *
 * [160] Intersection of Two Linked Lists
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
var getIntersectionNode = function(nodeA, nodeB) {
  if (!nodeA || !nodeB) return null
  if (nodeA == nodeB) return nodeA
  let a = [], b = []

  do {
    if (nodeA) {
      a.push(nodeA)
      nodeA = nodeA.next
    }
    if (nodeB) {
      b.push(nodeB)
      nodeB = nodeB.next
    }
    if (a.includes(nodeB)) return nodeB
    if (b.includes(nodeA)) return nodeA
    if (nodeA === nodeB) return nodeA
  } while (nodeA || nodeB)
  return null
};
// @lc code=end

