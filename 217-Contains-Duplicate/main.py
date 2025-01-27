from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # APPROACH 1 -- BRUTEFORCE
        # n = len(nums)
        #
        # for i in range(n):
        #     current = nums[i]
        #
        #     for j in range(n):
        #         if j == i:
        #             continue
        #         if nums[j] == current:
        #             return True
        #
        # return False

        # APPROACH 2 -- KEEPING TRACK OF UNIQUE ELEMENTS
        # LISTS are slower to traverse use Set

        unique_ = set()

        for i in nums:
            if i in unique_:
                return True
            unique_.add(i)

        return False


inputs = {1: [[1, 2, 3, 1]], 2: [[1, 2, 3, 4]], 3: [[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]]}

for _, input in inputs.items():
    print("---> Solution ", _)
    print(Solution().containsDuplicate(*input))
    print()
