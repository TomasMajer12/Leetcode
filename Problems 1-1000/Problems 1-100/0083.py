from Structures.linkedList import create_linked_list,print_linked_list
from typing import Optional
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = head
        if prev and prev.next:
            n = prev.next
        else:
            return head

        while n:
            if prev.val == n.val:
                prev.next = n.next
                n = n.next
            else:
                prev = n
                n = n.next
        return head


print_linked_list(Solution().deleteDuplicates(create_linked_list([1,1,2,3,3])))        