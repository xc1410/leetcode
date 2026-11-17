import time


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        side=len(matrix)
        for i in range(side):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        left=0
        right=len(matrix)-1
        side=len(matrix)
        while left<right:
            for i in range(side):
                matrix[i][left],matrix[i][right]=matrix[i][right],matrix[i][left]
            left+=1
            right-=1
        


def check(matrix, expected):
    Solution().rotate(matrix)
    assert matrix == expected, matrix


check([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
check([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]], [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]])
check([[1]], [[1]])
check([[1, 2], [3, 4]], [[3, 1], [4, 2]])
check([[1, 1], [1, 1]], [[1, 1], [1, 1]])
check([[-1, -2], [-3, -4]], [[-3, -1], [-4, -2]])
check([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], [[21, 16, 11, 6, 1], [22, 17, 12, 7, 2], [23, 18, 13, 8, 3], [24, 19, 14, 9, 4], [25, 20, 15, 10, 5]])
check([[0, 0, 1], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 1]])
check([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]])
check([[1, 2, 1], [2, 1, 2], [1, 2, 1]], [[1, 2, 1], [2, 1, 2], [1, 2, 1]])
check([[7, 7, 8], [7, 9, 8], [8, 8, 9]], [[8, 7, 7], [8, 9, 7], [9, 8, 8]])
check([[1, 0], [0, 0]], [[0, 1], [0, 0]])
print('全部用例通过')

for run in range(3):
    matrix = [[i_row * 300 + i_col for i_col in range(300)] for i_row in range(300)]
    begin = time.perf_counter()
    Solution().rotate(matrix)
    seconds = time.perf_counter() - begin
    total = sum([matrix[i_row][i_col] * (i_row + 2 * i_col) for i_row in range(300) for i_col in range(300)])
    assert total == 1412084310000, total
    print(seconds)