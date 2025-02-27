#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hash = {}
        while headA:
            if headA.val not in hash: hash[headA.val] = []
            hash[headA.val].append(headA)
            headA = headA.next
        while headB:
            if headB.val in hash and headB in hash[headB.val]:
                return headB
            headB = headB.next
        return None
# @lc code=end

