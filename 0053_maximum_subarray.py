import time


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cur=nums[0]
        best=nums[0]
        for x in nums[1:]:
            cur=max(x,cur+x)
            best=max(cur,best)
        return best


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))   # 期望 6
print(Solution().maxSubArray([1]))                               # 期望 1
print(Solution().maxSubArray([5, 4, -1, 7, 8]))                  # 期望 23
print(Solution().maxSubArray([-3, -1, -2]))                      # 期望 -1
print(Solution().maxSubArray([-1, 0, -2]))                       # 期望 0
print(Solution().maxSubArray([2, -1, 2, -1, 2]))                 # 期望 4
print(Solution().maxSubArray([8, -19, 5, -4, 20]))               # 期望 21

big = list(range(-50000, 50000))
begin = time.perf_counter()
print(Solution().maxSubArray(big))   # 期望 1249975000
print(time.perf_counter() - begin)