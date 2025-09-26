

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <2:
            return 0

        sieve = [ True] * (n)

        sieve[0] = False
        sieve[1] = False

        p = 2

        while p*p <= n:
            if sieve[p]:
                for i in range(p*p, n,p):
                    sieve[i] = False
            p+=1
        return sum(sieve)

    
print(Solution().countPrimes(10))

