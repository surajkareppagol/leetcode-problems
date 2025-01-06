from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answers = [0 for i in range(n)]

        ## Step 1 -- Loop over boxes and start from last ball
        for i in range(n):
            for j in range(n - 1, -1, -1):
                ## Step 2 -- Check right
                if j > i and boxes[j] == "1":
                    answers[i] += j - i

                ## Step 3 -- Check left
                elif j < i and boxes[j] == "1":
                    answers[i] += i - j

        return answers


inputs = {1: ["110"], 2: ["001011"]}

for _, input in inputs.items():
    print(Solution().minOperations(*input))
