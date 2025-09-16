

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        size = 1
        tail = head
        while tail.next:
            tail = tail.next
            size += 1
        
        k = k % size
        if k == 0:
            return head 
        

        prev = head
        for _ in range(size - k - 1):
            prev = prev.next
        
        new_head = prev.next
        prev.next = None  
        tail.next = head  
        
        return new_head
    
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
print_linked_list(Solution().rotateRight(create_linked_list([0,1,2]),4))