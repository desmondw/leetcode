#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode()
        cur = l3

        while not (l1 is None and l2 is None):
            if l2 is None or (l1 is not None and l1.val <= l2.val):
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next
        
        l3 = l3.next
        return l3
# @lc code=end

sol = Solution()
print(sol.mergeTwoLists([1,2,4],[1,3,4]))