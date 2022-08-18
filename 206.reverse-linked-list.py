#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode], prev=None) -> Optional[ListNode]:
        if head is None: return None

        oldNext = head.next
        head.next = prev
        if oldNext is None:
            return head
        return self.reverseList(oldNext, head)

# @lc code=end

