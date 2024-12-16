from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Brute-force
        nums_s = [str(i) for i in nums]

        nums_s.sort(key=lambda a: a * 10, reverse=True)

        if not nums_s[0] == "0":
            return "0"

        return "".join(nums_s)


inputs = {
    1: [
        [10, 2],
    ],
    2: [[3, 30, 34, 5, 9]],
}

for _, input in inputs.items():
    print(Solution().largestNumber(*input))
