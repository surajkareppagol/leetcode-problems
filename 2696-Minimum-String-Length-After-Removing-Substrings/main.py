# Author: Suraj K
# Could have used Stack

from typing import *


class Solution:
    def minLength(self, s: str) -> int:
        while "AB" in s or "CD" in s:
            index = s.index("AB") if "AB" in s else s.index("CD")

            string = list(s)
            string.pop(index)
            string.pop(index)

            s = "".join(string)

        return len(s)


solution = Solution()

print(solution.minLength("ABFCACDB"))
print(solution.minLength("ACBBD"))
