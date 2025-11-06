"""
Given the head of a linked list and an integer val, 
remove all the nodes of the linked list that has 
Node.val == val, and return the new head.
"""
from typing import Optional
from Structures.linkedList import create_linked_list, print_linked_list
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next

        
                

print_linked_list(Solution().removeElements(create_linked_list([1,2,6,3,4,5,6]), 6)) 