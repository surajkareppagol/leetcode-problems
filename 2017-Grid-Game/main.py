# 6 / 109 testcases passed

from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        # ************** CALCULATE ALL MAXIMUM PATHS **************#

        def calculate_cost():
            paths = {}
            cost = [0] * columns
            change_row = 0

            for i in range(columns):
                row = 0
                column = 0

                visited = []

                for j in range(columns + 1):
                    visited.append([row, column])
                    cost[i] += grid[row][column]

                    if j == change_row:
                        row += 1
                        continue

                    column += 1

                change_row += 1

                paths[i] = visited

            return cost, paths

        # ************** ZERO OUT MAX PATH **************#

        cost, paths = calculate_cost()

        max_path = cost.index(max(cost))

        for i, j in paths[max_path]:
            grid[i][j] = 0

        # ************** CALCULATE ALL MINIMUM PATHS **************#

        cost, path = calculate_cost()
        return max(cost)


inputs = {
    1: [[[2, 5, 4], [1, 5, 1]]],
    2: [[[3, 3, 1], [8, 5, 2]]],
    3: [[[1, 3, 1, 15], [1, 3, 3, 1]]],
}

for _, input in inputs.items():
    print("---> Solution ", _)
    print(Solution().gridGame(*input))
    print()
