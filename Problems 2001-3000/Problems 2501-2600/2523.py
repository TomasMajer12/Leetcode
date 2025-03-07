

from typing import List

def SieveOfEratosthenes(n):

    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):

            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return prime

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = SieveOfEratosthenes(1000000)
        betweenPrimes = []
        for i in range(left,right+1):
            if primes[i] and i != 1:
                betweenPrimes.append(i)

        if len(betweenPrimes) <= 1:
            return [-1,-1]
        
        currentMin = 9999999
        ret = [-1,-1]
        for i in range(len(betweenPrimes) - 1):
            if betweenPrimes[i+1] - betweenPrimes[i] < currentMin:
                currentMin = betweenPrimes[i+1] - betweenPrimes[i]
                ret[0] = betweenPrimes[i]
                ret[1] = betweenPrimes[i+1]
        return ret

print(Solution().closestPrimes(10,19))
