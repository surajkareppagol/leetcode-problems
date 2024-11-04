# Author: Suraj K
# Accepted

from typing import *


class Solution:
    def compressedString(self, word: str) -> str:
        count = 1
        comp = ''

        current = word[0]
        for letter in word[1:]:
            if letter == current and count < 9:
                count += 1
            elif letter != current or count >= 9:
                comp += f"{str(count)}{current}"
                current = letter
                count = 1

        if current == word[-1]:
            comp += f"{str(count)}{current}"
        else:
            comp += f"{str(count)}{current}"
            comp += f"1{word[-1]}"

        return comp


solution = Solution()

print(solution.compressedString("abcde"))
print(solution.compressedString("aaaaaaaaaaaaaabb"))
