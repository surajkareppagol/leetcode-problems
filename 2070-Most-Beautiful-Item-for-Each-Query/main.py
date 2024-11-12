# Author: Suraj K
# Testcases 33/35

from typing import *


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # APPROACH 1

        n = len(queries)
        m = len(items)

        solution = [0] * n

        for inx, query in enumerate(queries, start=0):
            for i in range(m):
                if items[i][0] <= query and items[i][1] > solution[inx]:
                    solution[inx] = items[i][1]

        return solution


s = Solution()

print(s.maximumBeauty([[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], [1, 2, 3, 4, 5, 6]))
print(s.maximumBeauty([[1, 2], [1, 2], [1, 3], [1, 4]], [1]))
print(s.maximumBeauty([[10, 1000]], [5]))
