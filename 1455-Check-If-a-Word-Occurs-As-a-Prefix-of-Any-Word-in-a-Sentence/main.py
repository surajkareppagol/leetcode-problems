# Author: Suraj K

from typing import *


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for index, word in enumerate(sentence.split(" "), start=1):
            if searchWord in word and word.index(searchWord) == 0:
                return index
        return -1


s = Solution()

print(s.isPrefixOfWord("i love eating burger", "burg"))
print(s.isPrefixOfWord("this problem is an easy problem", "pro"))
print(s.isPrefixOfWord("i am tired", "you"))
print(s.isPrefixOfWord("i am tired", "ed"))
