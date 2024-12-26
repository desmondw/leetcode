#
# @lc app=leetcode id=2181 lang=python3
#
# [2181] Merge Nodes in Between Zeros
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node and node.next:
            if node.next.val != 0:
                node.val += node.next.val
                node.next = node.next.next
            elif node.next.next:
                node = node.next
            else:
                node.next = None

        return head
# @lc code=end

