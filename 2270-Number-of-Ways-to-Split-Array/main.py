from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        splits = 0

        ## Step 6: Initially calculate the sum
        sum_left = nums[0]
        sum_right = sum(nums[1:])

        if sum_left >= sum_right:
            splits += 1

        ## Step 1: Split the nums at each index
        for i in range(1, n):
            if i == n - 1:
                continue
            ## Step 2: Calculate the sum
            sum_left += nums[i]
            sum_right -= nums[i]

            # print(f"[dbg] {sum_left} >= {sum_right} == {sum_left >= sum_right}")

            ## Step 3: Check if split is possible
            if sum_left >= sum_right:
                splits += 1

        ## Step 4: Return the total splits
        return splits


inputs = {1: [[10, 4, -8, 7]], 2: [[2, 3, 1, 0]]}

for _, input in inputs.items():
    print(Solution().waysToSplitArray(*input))
