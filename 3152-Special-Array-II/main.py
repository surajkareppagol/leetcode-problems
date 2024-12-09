# Author: Suraj K

# TestCases Passed : 440 / 536

from typing import *


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        answers = []

        def check_parity(left=None, right=None):
            def check(a, b):
                if a == -1 or b == -1:
                    return True

                if a % 2 == 0 and b % 2 != 0:
                    return True
                elif b % 2 == 0 and a % 2 != 0:
                    return True

                return False

            diff = False

            if left is not None:
                a, b = left
                diff = check(a, b)

            if diff is False:
                return diff

            if right is not None:
                a, b = right
                diff = check(a, b)

            if diff is False:
                return diff

            return diff

        for i, j in queries:
            array = nums[i : j + 1]
            len_array = len(array)
            result = []

            # When array length is 2
            if len_array == 2:
                a, b = array

                if a % 2 == 0 and b % 2 != 0:
                    answers.append(True)
                elif b % 2 == 0 and a % 2 != 0:
                    answers.append(True)
                else:
                    answers.append(False)

                continue

            # When array length is 0
            if len_array == 0 or len_array == 1:
                answers.append(True)
                continue

            # Main loop
            for index, _ in enumerate(array):
                left = None
                right = None

                if index > 0:
                    left = (
                        array[index - 2 : index]
                        if index + 1 > 2
                        else [-1, array[index - 1]]
                    )

                if index < len_array - 1:
                    right = (
                        array[index + 1 : index + 3]
                        if len(array) - index > 2
                        else [array[index + 1], -1]
                    )

                parity = check_parity(left, right)
                # print(array, left, right, parity)
                # print()

                result.append(parity)

            if False in result:
                answers.append(False)
            else:
                answers.append(True)

            result.clear()

        return answers


s = Solution()

print(s.isArraySpecial([3, 4, 1, 2, 6], [[0, 4]]))
print(s.isArraySpecial([4, 3, 1, 6], [[0, 2], [2, 3]]))
print(s.isArraySpecial([1, 1], [[0, 1]]))
print(s.isArraySpecial([3, 7, 4, 5], [[0, 3]]))
