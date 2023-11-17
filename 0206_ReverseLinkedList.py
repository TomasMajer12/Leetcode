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
        prev = head
        curr = head.next
        while head:
            tmp = head
            head.next = prev
            prev = head
            if tmp != None:
                head = tmp

        return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
print(Solution().reverseList(head))