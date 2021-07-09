/*
 * @lc app=leetcode id=19 lang=javascript
 *
 * [19] Remove Nth Node From End of List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    let list = []
    let node = head
    while (node) {
      list.push(node)
      node = node.next
    }

    node = list[list.length-n]
    if (node.next) {
      node.val = node.next.val
      node.next = node.next.next
    } else if (list.length-n-1 >= 0) {
      prev = list[list.length-n-1]
      prev.next = null
    } else {
      return null
    }
    
    return head
};
// @lc code=end

