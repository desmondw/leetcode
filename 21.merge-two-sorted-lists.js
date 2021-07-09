/*
 * @lc app=leetcode id=21 lang=javascript
 *
 * [21] Merge Two Sorted Lists
 */

// @lc code=start
class ListNode{
  constructor (val, next) {
     this.val = (val===undefined ? 0 : val)
     this.next = (next===undefined ? null : next)
 }
}
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
  let l3 = new ListNode()
  let cur = l3

  while (l1 || l2) {
    if (!l2 || (l1 && l1.val <= l2.val)) {
      cur.next = l1
      cur = cur.next
      l1 = l1.next
    } else {
      cur.next = l2
      cur = cur.next
      l2 = l2.next
    }
  }

  l3 = l3.next
  return l3
}
// @lc code=end

