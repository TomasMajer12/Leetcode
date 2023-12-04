"""
You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].
Implement the SmallestInfiniteSet class:
SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int popSmallest() Removes and returns the smallest integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.
"""

import queue
class SmallestInfiniteSet:

    def __init__(self):
        self.queue = queue.PriorityQueue()
        self.queue.put(1,1)
        self.s = set([1]) 
        self.next = 2
    def popSmallest(self) -> int:
        # Pop the smallest element from the priority queue
        num = self.queue.get()

        # If the popped element is the expected next element, add it to the set and update next
        if num == self.next-1:
            self.queue.put(self.next,self.next)
            self.s.add(self.next)
            self.next+=1
        self.s.remove(num)
        return num

    def addBack(self, num: int) -> None:
        # Check if the given element is smaller than the expected next element
        # and not already present in the set
        if num < self.next and num not in self.s:
            self.s.add(num)
            self.queue.put(num,num)
            


obj = SmallestInfiniteSet()
param_1 = print(obj.popSmallest())
param_1 = print(obj.popSmallest())
param_1 = print(obj.popSmallest())
param_1 = print(obj.popSmallest())
param_1 = print(obj.popSmallest())
param_1 = print(obj.popSmallest())

obj.addBack(4)
param_1 = print(obj.popSmallest())
param_1 = print(obj.popSmallest())