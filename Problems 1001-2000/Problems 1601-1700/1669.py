

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr = list1
        for _ in range(a - 1):
            curr = curr.next
        
        qtr = curr.next
        for _ in range(b - a + 1):
            qtr = qtr.next
        
        curr.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = qtr
        
        return list1
    
    
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head



print_linked_list(Solution().mergeInBetween(create_linked_list([10, 1, 13, 6, 9, 5]),3,4,create_linked_list([1000000,1000001,1000002])))