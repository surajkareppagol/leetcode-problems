# Author: Suraj K
# Testcases 658/718

from typing import *


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        combinations = []

        m = len(arr1)
        n = len(arr2)

        for i in range(0, m):
            for j in range(0, n):
                combinations.append([arr1[i], arr2[j]])

        highest_prefix = 0

        for combination in combinations:
            common_prefix = 0

            m, n = combination

            m, n = str(m), str(n)

            range_ = max(len(m), len(n))

            for i in range(0, range_):
                if (i < len(m) and i < len(n)) and m[i] == n[i]:
                    common_prefix += 1
                else:
                    break

            if common_prefix > highest_prefix:
                highest_prefix = common_prefix

        return highest_prefix


solution = Solution()

print(solution.longestCommonPrefix([1, 10, 100], [1000]))
print(solution.longestCommonPrefix([1, 2, 3], [4, 4, 4]))
print(solution.longestCommonPrefix([3, 26], [7, 16]))
