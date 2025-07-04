import itertools
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        a = list(itertools.permutations(nums))
        res = []
        seen = set()
        for i in a:
            t = tuple(i)
            if i not in seen:
                seen.add(t)
                res.append(i)
        return res