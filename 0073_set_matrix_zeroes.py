import time


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])
        first_row=False
        for i in range(n):
            if matrix[0][i]==0:
                first_row=True
        first_colmun=False
        for i in range(m):
            if matrix[i][0]==0:
                first_colmun=True

        for i_row in range(1,m):
            for i_col in range(1,n):
                if matrix[i_row][i_col]==0:
                    matrix[i_row][0]=0

        for i_col in range(1,n):
            for i_row in range(1,m):
                if matrix[i_row][i_col]==0:
                    matrix[0][i_col]=0

        for i_row in range(1,m):
            for i_col in range(1,n):
                if matrix[i_row][0]==0 or matrix[0][i_col]==0:
                    matrix[i_row][i_col]=0     
        
        if first_colmun==True:
            for i in range(m):
                matrix[i][0]=0
        
        if first_row==True:
            for i in range(n):
                matrix[0][i]=0


def check(matrix, expected):
    Solution().setZeroes(matrix)
    assert matrix == expected, matrix


check([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]])
check([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]], [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])
check([[1]], [[1]])
check([[0]], [[0]])
check([[1, 2], [3, 4]], [[1, 2], [3, 4]])
check([[-1, 2], [3, -4]], [[-1, 2], [3, -4]])
check([[1, 0], [1, 1], [0, 1]], [[0, 0], [0, 0], [0, 0]])
check([[1, 2, 3], [4, 5, 6], [7, 8, 0]], [[1, 2, 0], [4, 5, 0], [0, 0, 0]])
check([[0, 0, 1], [1, 1, 1]], [[0, 0, 0], [0, 0, 1]])
check([[1, 0, 1, 1]], [[0, 0, 0, 0]])
check([[1], [0], [1]], [[0], [0], [0]])
check([[1, 2], [0, 3]], [[0, 2], [0, 0]])
check([[1, 0], [2, 3]], [[0, 0], [2, 0]])
check([[1, 2, 3], [4, 0, 6], [7, 8, 9], [0, 1, 1]], [[0, 0, 3], [0, 0, 0], [0, 0, 9], [0, 0, 0]])
print('全部用例通过')

for run in range(3):
    matrix = [[1] * 300 for i in range(300)]
    matrix[100][200] = 0
    matrix[250][50] = 0
    begin = time.perf_counter()
    Solution().setZeroes(matrix)
    seconds = time.perf_counter() - begin
    total = sum([sum(row) for row in matrix])
    assert total == 88804, total
    print(seconds)