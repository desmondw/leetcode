#
# @lc app=leetcode id=1290 lang=python3
#
# [1290] Convert Binary Number in a Linked List to Integer
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        b = ''
        if not head or not head.val:
            b += '0'
        while head and head.val != None:
            b += str(head.val)
            head = head.next
        return int(b, 2)
# @lc code=end

