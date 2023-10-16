"""
You are given two non-empty linked lists representing two non-negative integers.
 The digits are stored in reverse order, and each of their nodes contains a single digit. 
 Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        exp = 1
        num1,num2 = 0,0

        while l1:
            num1 = num1 + l1.val * exp
            exp*=10
            l1 = l1.next
        exp = 1
        while l2:
            num2 = num2 + l2.val*exp
            exp*=10
            l2 = l2.next
        val = num1+num2

        prev = None
        exp = 10**(len(str(val))-1)
        while exp > 0 :
            num = val//exp
            node = ListNode(num,prev)
            val%=exp
            exp//=10
            prev = node
        return prev
    
l1 = ListNode(2, ListNode(4, ListNode(3)))

l2 = ListNode(5, ListNode(6, ListNode(4)))   

print(Solution().addTwoNumbers(l1,l2))