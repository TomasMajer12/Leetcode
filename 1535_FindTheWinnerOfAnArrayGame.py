"""
Given an integer array arr of distinct integers and an integer k.

A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). 
In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0, and the smaller integer moves to the end of the array. 
The game ends when an integer wins k consecutive rounds.

Return the integer which will win the game.

It is guaranteed that there will be a winner of the game.
"""

from typing import List
import queue
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr): #if k > lenght of array --> return max, because he has to win over every number
            return max(arr)
        myQueue = queue.Queue() 
        for i in arr:
            myQueue.put(i) #initialize queue
        currentStreak = 0
        startNumber = myQueue.get()
        while True:
            currentNumber = myQueue.get() #get fight element
            if startNumber >  currentNumber: #current number is bigger --> add to streak
                currentStreak+=1
                if currentStreak == k:
                    return startNumber
                myQueue.put(currentNumber)
            else:
                myQueue.put(startNumber)
                startNumber = currentNumber
                currentStreak = 1
                if currentStreak == k: #k==1 case
                    return startNumber

print(Solution().getWinner(arr = [2,1,3,5,4,6,7], k = 2))
print(Solution().getWinner(arr = [3,2,1], k = 10))
