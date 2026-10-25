class Solution:
    def maxArea(self, height: list[int]) -> int:
        left=0
        right=len(height)-1
        max_volume=0
        while left<right:
            volume=min(height[left],height[right])*(right-left)
            max_volume=max(max_volume,volume)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_volume


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))   # 期望 49
print(Solution().maxArea([1, 1]))                         # 期望 1   ← 宽度是 1，不是 2
print(Solution().maxArea([4, 3, 2, 1, 4]))                # 期望 16  ← 最优就在两端
print(Solution().maxArea([1, 2, 1]))                      # 期望 2

import time

big = list(range(1, 5001))                 # 高度 1, 2, ..., 5000
begin = time.perf_counter()
print(Solution().maxArea(big))             # 期望 6250000
print(time.perf_counter() - begin)         # 期望 0.00x 秒