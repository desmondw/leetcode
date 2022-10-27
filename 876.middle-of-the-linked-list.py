#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def middleNode(self, head: Optional[ListNode], count=0) -> Optional[ListNode]:
        if not head:
            return math.ceil((count-1)/2)
        target = self.middleNode(head.next, count+1)

        # check if this node
        if target == count:
            return head

        # else continue search
        return target

# @lc code=end

