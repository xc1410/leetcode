import time


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row=0
        col=len(matrix[0])-1
        while row < len(matrix) and col >= 0:
            current = matrix[row][col]
            if current == target:
                return True
            elif current > target:
                col -= 1
            else:
                row += 1
        return False



def check(matrix, target, expected):
    result = Solution().searchMatrix(matrix, target)
    assert result == expected, result


example = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
check(example, 5, True)
check(example, 20, False)
check(example, 1, True)
check(example, 30, True)
check(example, 18, True)
check(example, 15, True)
check(example, 0, False)
check(example, 31, False)
check(example, 17, True)
check(example, 25, False)
check([[1]], 1, True)
check([[1]], 2, False)
check([[-5]], -5, True)
check([[1, 3, 5]], 3, True)
check([[1, 3, 5]], 4, False)
check([[1], [3], [5]], 5, True)
check([[1], [3], [5]], 0, False)
check([[1, 1], [1, 1]], 1, True)
check([[1, 1], [1, 1]], 2, False)
check([[-10, -5], [-7, 0]], -7, True)
check([[1, 2], [3, 4]], 3, True)
check([[1, 4], [2, 5]], 3, False)
print('全部用例通过')

for run in range(3):
    matrix = [[i_row * 2 + i_col * 2 for i_col in range(1000)] for i_row in range(1000)]
    begin = time.perf_counter()
    found = 0
    for target in range(0, 4000, 7):
        if Solution().searchMatrix(matrix, target):
            found += 1
    seconds = time.perf_counter() - begin
    assert found == 286, found
    print(seconds)