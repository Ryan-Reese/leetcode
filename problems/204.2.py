# Sieve of Eratosthenesj
class Solution:
    def countPrimes(self, n: int) -> int:
        if n in [0, 1, 2]:
            return 0
        prime_dict = {num: 1 for num in range(2, n)}
        prime = 2
        while True:
            for composite in range(2*prime, n, prime):
                prime_dict[composite] = 0

            for num in range(prime+1, n+1):
                if num >= n:
                    return sum(list(prime_dict.values()))
                elif prime_dict[num] == 1:
                    prime = num
                    break

test = Solution()
print(test.countPrimes(100000))

