"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            if tmp:
                curr = tmp   
            else:
                break         
        return curr

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
sol = Solution().reverseList(head)
while sol:
    print(sol.val)
    sol = sol.next