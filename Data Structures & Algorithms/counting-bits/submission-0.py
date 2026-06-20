class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        def count(n):
            res = 0

            while n:
                res += n & 1
                n >>= 1
            return res

        for i in range(0, n + 1):
            res.append(count(i))

        return res