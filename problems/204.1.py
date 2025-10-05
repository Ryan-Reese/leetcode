# naive approach - O(n^2)
class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        for test_num in range(2, n):
            if isPrime(test_num):
                count += 1
        return count

def isPrime(test_num: int) -> bool:
    for test_divisor in range(2, int(test_num+1/2)):
        if (test_num%test_divisor == 0) and (test_num!=test_divisor):
            return False
    return True

