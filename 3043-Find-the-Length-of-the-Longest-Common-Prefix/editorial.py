from typing import *


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()

        for value in arr1:
            while value not in prefixes and value > 0:
                prefixes.add(value)
                value //= 10

        longest_common_prefix = 0

        for value in arr2:
            while value not in prefixes and value > 0:
                value //= 10

            if value > 0:
                longest_common_prefix = max(
                    longest_common_prefix, len(str(value)))

        return longest_common_prefix


solution = Solution()

print(solution.longestCommonPrefix([1, 10, 100], [1000]))
print(solution.longestCommonPrefix([1, 2, 3], [4, 4, 4]))
print(solution.longestCommonPrefix([3, 26], [7, 16]))
