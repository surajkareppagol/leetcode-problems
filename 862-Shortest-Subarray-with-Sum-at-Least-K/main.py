# Author: Suraj K

# Approach 1: Bruteforce - 75 / 98

from typing import *


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # APPROACH 1 - Brute Force

        n = len(nums)
        shortest_length = n + 1

        for i in range(n):
            for j in range(i + 1, n + 1):
                if i != j and sum(nums[i:j]) >= k:
                    shortest_length = min(shortest_length, j - i)

        if shortest_length == n + 1:
            return -1
        else:
            return shortest_length


s = Solution()

print(s.shortestSubarray([1], 1))
print(s.shortestSubarray([1, 2], 4))
print(s.shortestSubarray([2, -1, 2], 3))
