# Author: Suraj K
# Testcases 87/112

from typing import *


class Solution:
    def maximumSwap(self, num: int) -> int:
        nl = list(map(int, list(str(num))))

        n = len(nl)

        solution = ""

        for i in range(n):
            position = i

            if i+1 >= n:
                return int(solution + ("".join(list(map(str, nl[position:])))))

            m_ = max(nl[i+1:])
            mi_ = nl.index(m_)

            if m_ < nl[position] or mi_ == position:
                solution += str(nl[position])
                nl[position] = 0
                continue
            else:
                nl[i], nl[mi_] = nl[mi_], nl[i]
                return int(solution + ("".join(list(map(str, nl[position:])))))
        return int(solution + ("".join(list(map(str, nl[position:])))))


print(Solution().maximumSwap(2736))
print(Solution().maximumSwap(9973))
print(Solution().maximumSwap(98368))
