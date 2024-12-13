# 1036 / 1044 testcases passed
# Time Limit Exceeded

from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0

        def smallest():
            s_v = 0
            index = 0

            for i in range(len(nums)):
                if nums[i] == -1:
                    continue
                s_v = nums[i]
                index = i
                break

            for i, v in enumerate(nums):
                if v != -1 and v < s_v:
                    s_v = v
                    index = i

            return index

        while True:
            small = smallest()
            score += nums[small]

            if small - 1 >= 0:
                nums[small - 1] = -1
            if small + 1 < len(nums):
                nums[small + 1] = -1

            nums[small] = -1

            if nums.count(-1) == len(nums):
                break

        return score


solution = Solution()

s = solution.findScore([2, 1, 3, 4, 5, 2])  # 7
print(s)

s = solution.findScore([2, 3, 5, 1, 3, 2])  # 5
print(s)

s = solution.findScore(
    [10, 44, 10, 8, 48, 30, 17, 38, 41, 27, 16, 33, 45, 45, 34, 30, 22, 3, 42, 42]
)  # 212
print(s)
