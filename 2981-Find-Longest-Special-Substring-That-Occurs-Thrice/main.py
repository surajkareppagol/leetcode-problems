# Author: Suraj K

from pprint import pprint
from typing import *


class Solution:
    def maximumLength(self, s: str) -> int:
        frequency = {}

        n = len(s)

        for i in range(n):
            for j in range(i, n + 1):
                if i != j:
                    sub = s[i:j]

                    if sub not in frequency.keys():
                        frequency[sub] = 1
                        continue
                    frequency[sub] += 1

        answer = 0

        for key, value in frequency.items():
            if value >= 3 and len(key) > answer:
                answer = len(key)

        if answer == 0:
            return -1
        return answer


s = Solution()

print(s.maximumLength("aaaa"))
print(s.maximumLength("abcdef"))
print(s.maximumLength("abcaba"))
print(s.maximumLength("cccerrrecdcdccedecdcccddeeeddcdcddedccdceeedccecde"))
