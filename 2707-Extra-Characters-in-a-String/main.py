# Author: Suraj K
# Testcases 325/2028

from typing import *


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        substrings_length = 0

        for i in range(0, n):
            for j in range(i + 1, n + 1):
                if i != j and s[i:j] in dictionary:
                    substrings_length += (j + 1) - (i + 1)
                    i = j

            if i == n:
                break

        return n - substrings_length


solution = Solution()

print(solution.minExtraChar("leetscode", ["leet", "code", "leetcode"]))
print(solution.minExtraChar("sayhelloworld", ["hello", "world"]))
