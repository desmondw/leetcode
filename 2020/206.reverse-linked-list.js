/*
 * @lc app=leetcode id=206 lang=javascript
 *
 * [206] Reverse Linked List
 */

class ListNode{
  constructor (val, next) {
     this.val = (val===undefined ? 0 : val)
     this.next = (next===undefined ? null : next)
 }
}
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
  let list = []
  let node = head
  while (node) {
    list.unshift(node.val)
    node = node.next
  }

  head = list.length ? new ListNode(list[0],null) : null
  node = head
  for (let i=1;i<list.length;i++) {
    let swap = new ListNode(list[i],null)
    node.next = swap
    node = node.next
  }
  return head
};
// @lc code=end

