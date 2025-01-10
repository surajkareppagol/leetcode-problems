# 45 / 56 testcases passed

from collections import Counter
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Subset including multiplicity
        # Universal - A in words1 is Universal if every B in words2, B is
        # subset of A

        universal = []
        word_counts = []

        words1 = set(words1)
        words2 = set(words2)

        for word in words2:
            word_counts.append(Counter(word))

        for word1 in words1:
            # Check if all the strings in words2 is subset of word1
            # if yes add it to the universal
            current_subset_length = 0

            for word2 in word_counts:
                # Check if word2 present in word1
                letter_present = 0

                for key in word2.keys():
                    word1_count = word1.count(key)

                    if word1_count >= word2[key]:
                        letter_present += 1
                    else:
                        break

                if letter_present == len(word2.keys()):
                    current_subset_length += 1

            if current_subset_length == len(words2):
                universal.append(word1)

        return universal


inputs = {
    1: [["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"]],
    2: [["amazon", "apple", "facebook", "google", "leetcode"], ["l", "e"]],
}

for _, input in inputs.items():
    print(Solution().wordSubsets(*input))
