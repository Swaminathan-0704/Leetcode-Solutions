class Solution:
    def totalMoney(self, n: int) -> int:
        k = n // 7
        r = n % 7
        return (7 * k * (k + 1)) // 2 + 21 * k + (r * (2 * k + r + 1)) // 2


