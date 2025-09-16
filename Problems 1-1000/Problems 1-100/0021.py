# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        head = None

        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        curr = head
        while True:
            if list1 == None and list2 == None:
                break

            if list1 == None and list2 != None:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
                curr.next = None
            elif list2 == None and list1 != None:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
                curr.next = None       
            else:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                    curr = curr.next
                    curr.next = None  
                else:
                    curr.next = list2
                    list2 = list2.next
                    curr = curr.next
                    curr.next = None                                                 
        return head
        


def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


print_linked_list(Solution().mergeTwoLists(create_linked_list([1]),create_linked_list([2])))