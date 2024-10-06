# Author: Suraj K
# Testcases 123/138

# Incomplete

from typing import *


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        len_s1 = len(sentence1)
        len_s2 = len(sentence2)

        smaller_sentence = ""
        bigger_sentence = ""

        if len_s1 < len_s2:
            smaller_sentence = sentence1.split(" ")
            bigger_sentence = sentence2.split(" ")
        else:
            smaller_sentence = sentence2.split(" ")
            bigger_sentence = sentence1.split(" ")

        if smaller_sentence[0] == bigger_sentence[0] or smaller_sentence[-1] == bigger_sentence[-1]:
            for word in smaller_sentence:
                if word in bigger_sentence:
                    continue
                else:
                    return False

            return True
        else:
            return False


solution = Solution()

print(solution.areSentencesSimilar("My name is Haley", "My Haley"))
print(solution.areSentencesSimilar("of", "A lot of words"))
print(solution.areSentencesSimilar("Eating right now", "Eating"))
