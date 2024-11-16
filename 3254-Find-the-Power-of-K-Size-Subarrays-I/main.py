# Author: Suraj K

from typing import *


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        def check_sort_order(start: int, stop: int):
            for i in range(start, stop - 1):
                if i + 1 < n and nums[i] + 1 != nums[i + 1]:
                    return False
                continue

            return True

        result = []

        # Step 1: Create sub-arrays
        start = 0
        stop = k

        n = len(nums)

        while True:
            if stop <= n:
                # Step 2: Check the sort order
                if check_sort_order(start, stop):
                    # Step 3: Add to array
                    result.append(nums[stop - 1])
                else:
                    result.append(-1)

                start += 1
                stop += 1

                continue

            break

        return result


s = Solution()

print(s.resultsArray([1, 2, 3, 4, 3, 2, 5], 3))
print(s.resultsArray([2, 2, 2, 2, 2], 4))
print(s.resultsArray([3, 2, 3, 2, 3, 2], 2))
print(s.resultsArray([1, 3, 4], 2))
