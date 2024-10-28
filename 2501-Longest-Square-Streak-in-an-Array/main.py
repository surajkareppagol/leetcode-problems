# Author: Suraj K
# 66 / 92 testcases passed

from typing import *
from math import sqrt


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        nums.reverse()

        long_ss = -1

        for n in nums:
            cur = sqrt(n)
            count = 1

            while cur in nums:
                count += 1
                cur = sqrt(cur)

            if count >= 2 and count > long_ss:
                long_ss = count

        return long_ss


solution = Solution()

print(solution.longestSquareStreak([4, 3, 6, 16, 8, 2]))
print(solution.longestSquareStreak([2, 3, 5, 6, 7]))
print(solution.longestSquareStreak([2, 4]))
print(solution.longestSquareStreak([2, 4, 3, 5]))
