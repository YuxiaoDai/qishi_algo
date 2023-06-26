class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True

        if n%2 == 1:
            return False
        else:
            n_half = n / 2
            return self.isPowerOfTwo(n_half)

