
/*
 * @lc app=leetcode id=328 lang=javascript
 *
 * [328] Odd Even Linked List
 */

// class ListNode {
//   constructor (val, next) {
//       this.val = (val===undefined ? 0 : val)
//       this.next = (next===undefined ? null : next)
//   }
// } 
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
 * @return {ListNode}
 */
var oddEvenList = function(head) {
  if (!head) return head
  let evenHead = head.next

  let oddNode = head
  let evenNode = head.next
  oddNode.next = evenHead

  let curOddNode = evenNode ? evenNode.next : null
  let curEvenNode, nextOddNode
  while (curOddNode) {
    curEvenNode = curOddNode.next
    nextOddNode = curEvenNode ? curEvenNode.next : null

    oddNode.next = curOddNode
    oddNode = oddNode.next
    oddNode.next = evenHead

    if (curEvenNode) {
      evenNode.next = curEvenNode
      evenNode = evenNode.next
      evenNode.next = null
    }

    curOddNode = nextOddNode
  }

  if (evenNode) evenNode.next = null
  return head
};

function getNodeArray(node) {
  let vals = []
  while (node) {
    vals.push(node.val)
    node = node.next
  }
  return vals
}

// // @lc code=end
