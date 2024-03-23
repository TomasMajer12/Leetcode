

# Definition for singly-linked list.

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        linkedList = []
        while head:
            linkedList.append(head.val)
            head = head.next
        return linkedList == linkedList[::-1]

print(Solution().isPalindrome(create_linked_list([1,2,2,1])))
print(Solution().isPalindrome(create_linked_list([1,2,1,1])))