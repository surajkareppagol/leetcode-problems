from typing import List


class Solution:
    def clearDigits(self, s: str) -> str:
        result = []

        for letter in s:
            if letter.isdigit() and result:
                result.pop()
                continue
            result.append(letter)

        return "".join(result)


inputs = {1: ["abc"], 2: ["cb34"], 3: ["a4vs5vv4v3"], 4: ["2323"]}

for _, input in inputs.items():
    print("---> Solution ", _)
    print(Solution().clearDigits(*input))
    print()
