class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            res = ''
            for i in range(0, len(s), k):
                chunk = s[i:i+k]
                sums = sum(int(c) for c in chunk)
                res += str(sums)
            s = res
        return s
