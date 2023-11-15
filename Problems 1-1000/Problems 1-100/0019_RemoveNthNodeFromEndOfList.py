"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        next = head
        count = 0
        while next != None:
            count+=1
            next = next.next
        next = head
        prev = head
        for i in range(count -n):
            prev = next
            next = next.next
        prev.next = next.next
        if n == count:
            return head.next
        return head