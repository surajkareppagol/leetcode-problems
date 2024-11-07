# Author: Suraj K

# From editorial

from typing import *


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        array = [0] * 24

        # Set up array with 24 bits
        # Now check each bit position if it is set to 1
        # if yes then increment that value in array
        for i in range(0, 24):
            for num in candidates:
                if (num & (1 << i)) > 0:
                    array[i] += 1

        # Return max value
        return max(array)


solution = Solution()

print(solution.largestCombination([16, 17, 71, 62, 12, 24, 14]))
print(solution.largestCombination([8, 8]))
