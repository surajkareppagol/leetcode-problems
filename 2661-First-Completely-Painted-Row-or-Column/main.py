# 1055 / 1058 testcases passed

from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        """BRUTE-FORCE
        # Painted = 0
        columns = len(mat[0])
        rows = len(mat)

        def rows_columns_painted(row, column):
            # print(f"[DBG] ROW: {row}, COLUMN: {column}, I: {index}")

            # ************** ROW **************#
            rows_painted = True

            current_row = mat[row]
            for i in range(columns):
                if current_row[i] != 0:
                    rows_painted = False
                    break

            if rows_painted:
                return True

            # ************** COLUMNS **************#
            columns_painted = True

            for i in range(rows):
                # print(f"[DBG] ERROR I: {i}")
                if mat[i][column] != 0:
                    columns_painted = False
                    break

            # ************** RETURN **************#

            if columns_painted:
                return True

            return False

        for index, i in enumerate(arr):
            for row_index, row in enumerate(mat):
                if i in row:
                    column_index = row.index(i)
                    row[column_index] = 0
                    # print(f"[DBG] I: {i} --- INDEX: {index} - ROW: {row}")

                    if rows_columns_painted(row_index, column_index):
                        return index

                    break
        """

        # Painted = 0
        total_columns = len(mat[0])
        total_rows = len(mat)

        rows = [total_columns] * total_rows
        columns = [total_rows] * total_columns

        # print(f"[DBG] C: {columns} R: {rows}")

        def rows_columns_painted(row_index, column_index):
            if columns[column_index] == 0:
                return True

            if rows[row_index] == 0:
                return True

            return False

        for index, i in enumerate(arr):
            for row_index, row in enumerate(mat):
                if i in row:
                    column_index = row.index(i)

                    # print(f"[DBG] C: {columns} R: {rows}")
                    # print(f"[DBG] RI: {row_index}, L: {len(rows)}")
                    rows[row_index] -= 1
                    columns[column_index] -= 1

                    if rows_columns_painted(row_index, column_index):
                        return index

                    break


inputs = {
    1: [[1, 3, 4, 2], [[1, 4], [2, 3]]],
    2: [[2, 8, 7, 4, 1, 3, 5, 6, 9], [[3, 2, 5], [1, 4, 6], [8, 7, 9]]],
    3: [[1, 4, 5, 2, 6, 3], [[4, 3, 5], [1, 2, 6]]],
    4: [[6, 2, 3, 1, 4, 5], [[5, 1], [2, 4], [6, 3]]],
}

"""
[5, 1]
[2, 4]
[6, 3]
"""

for _, input in inputs.items():
    print("---> Solution ", _)
    print(Solution().firstCompleteIndex(*input))
    print()
