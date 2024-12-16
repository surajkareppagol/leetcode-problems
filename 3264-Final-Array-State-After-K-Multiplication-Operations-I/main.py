from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            m = nums.index(min(nums))
            nums[m] *= multiplier

        return nums


inputs = {1: [[2, 1, 3, 5, 6], 5, 2], 2: [[1, 2], 3, 4]}

for _, input in inputs.items():
    print(Solution().getFinalState(*input))
