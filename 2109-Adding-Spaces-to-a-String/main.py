# Author: Suraj K

from typing import *


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # Works, but worst code
        n = len(spaces)
        space_index = 0

        result = ""
        for index, letter in enumerate(s):
            if space_index < n and index == spaces[space_index]:
                space_index += 1

                result += " "
                result += letter
                continue
            result += letter
        return result


s = Solution()

print(s.addSpaces("LeetcodeHelpsMeLearn", [8, 13, 15]))
print(s.addSpaces("icodeinpython", [1, 5, 7, 9]))
print(s.addSpaces("spacing", [0, 1, 2, 3, 4, 5, 6]))
