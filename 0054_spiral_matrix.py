import time


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        top=0
        bottom=len(matrix)-1
        left=0
        right=len(matrix[0])-1
        res=[]
        while left<=right and top<=bottom:
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top+=1
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right-=1 
            if top<=bottom:
                for i in range(right,left-1,-1):
                    res.append(matrix[bottom][i])   
                bottom-=1            
            if left<=right:
                for i in range(bottom,top-1,-1):
                    res.append(matrix[i][left])
                left+=1
        return res
        


def check(matrix, expected):
    result = Solution().spiralOrder(matrix)
    assert result == expected, result


check([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5])
check([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
check([[7]], [7])
check([[1, 2, 3, 4]], [1, 2, 3, 4])
check([[1], [2], [3], [4]], [1, 2, 3, 4])
check([[1, 2], [3, 4]], [1, 2, 4, 3])
check([[1, 2], [3, 4], [5, 6]], [1, 2, 4, 6, 5, 3])
check([[1, 2, 3], [4, 5, 6]], [1, 2, 3, 6, 5, 4])
check([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10])
check([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8])
check([[0, 0], [0, 0]], [0, 0, 0, 0])
check([[-1, 5, -1], [2, 2, 2]], [-1, 5, -1, 2, 2, 2])
print('全部用例通过')

for run in range(3):
    matrix = [[i * 300 + j for j in range(300)] for i in range(300)]
    begin = time.perf_counter()
    result = Solution().spiralOrder(matrix)
    seconds = time.perf_counter() - begin
    assert len(result) == 90000, len(result)
    assert sum(result) == 4049955000, sum(result)
    assert result[:5] == [0, 1, 2, 3, 4], result[:5]
    assert result[-1] == 45149, result[-1]
    print(seconds)