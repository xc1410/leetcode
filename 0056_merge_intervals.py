import time


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0] )
        res=[intervals[0]]
        for start,end in intervals[1:]:
            if start <=res[-1][1]:
                res[-1][1]=max(res[-1][1],end)
            else:
                res.append([start,end])
        return res


print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))     # 期望 [[1, 6], [8, 10], [15, 18]]
print(Solution().merge([[1, 4], [4, 5]]))                         # 期望 [[1, 5]]
print(Solution().merge([[1, 4], [2, 3]]))                         # 期望 [[1, 4]]
print(Solution().merge([[4, 7], [1, 4]]))                         # 期望 [[1, 7]]
print(Solution().merge([[1, 4], [0, 0]]))                         # 期望 [[0, 0], [1, 4]]
print(Solution().merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))   # 期望 [[1, 10]]
print(Solution().merge([[1, 4], [5, 6]]))                         # 期望 [[1, 4], [5, 6]]
print(Solution().merge([[5, 5]]))                                 # 期望 [[5, 5]]

big = [[i, i] for i in range(10000, 0, -1)]
begin = time.perf_counter()
result = Solution().merge(big)
print(time.perf_counter() - begin)
print(len(result), min(result), max(result))   # 期望 10000 [1, 1] [10000, 10000]