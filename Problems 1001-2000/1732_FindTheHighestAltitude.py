"""
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. 
The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points 
i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
"""

from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAltitude = 0
        altitude = 0
        for num in gain:
            altitude+=num
            maxAltitude = max(maxAltitude,altitude)
        return maxAltitude
print(Solution().largestAltitude(gain = [-5,1,5,0,-7]))