# Author: Suraj K

from typing import *


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        repeated = set()
        repeated.add(nums[0])

        n = len(nums)

        for i in range(1, n):
            if nums[i] in repeated:
                repeated.remove(nums[i])
            else:
                repeated.add(nums[i])

        return list(repeated)[0]


s = Solution()

print(s.singleNumber([2, 2, 1]))
print(s.singleNumber([4, 1, 2, 1, 2]))
print(s.singleNumber([1]))
