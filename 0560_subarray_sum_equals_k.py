import time


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count={0:1}
        pre=0
        res=0
        for num in nums:
            pre+=num
            res+=count.get(pre-k,0)
            count[pre]=count.get(pre,0)+1
        return res


print(Solution().subarraySum([1, 1, 1], 2))                    # 期望 2
print(Solution().subarraySum([1, 2, 3], 3))                    # 期望 2
print(Solution().subarraySum([1], 0))                          # 期望 0
print(Solution().subarraySum([1, -1, 0], 0))                   # 期望 3
print(Solution().subarraySum([0, 0, 0], 0))                    # 期望 6
print(Solution().subarraySum([3, 4, 7, 2, -3, 1, 4, 2], 7))    # 期望 4
print(Solution().subarraySum([-1, -1, 1], 0))                  # 期望 1
big = [1, -1] * 10000
begin = time.perf_counter()
print(Solution().subarraySum(big, 0))   # 期望 100000000
print(time.perf_counter() - begin)