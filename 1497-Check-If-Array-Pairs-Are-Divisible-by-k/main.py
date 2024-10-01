# Author: Suraj K
# Testcases 44/98

# Incomplete

from typing import *


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        pairs = len(arr) // 2
        pairs_set = set()

        for i in range(0, len(arr)):
            for j in range(i + 1, len(arr)):
                if (arr[i] + arr[j]) % k == 0:
                    pairs_set.add((arr[i], arr[j]))

        if len(pairs_set) >= pairs:
            return True
        return False


solution = Solution()

print(solution.canArrange([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5))
print(solution.canArrange([1, 2, 3, 4, 5, 6], 7))
print(solution.canArrange([1, 2, 3, 4, 5, 6], 10))
print(solution.canArrange([3, 8, 17, 2, 5, 6], 10))
