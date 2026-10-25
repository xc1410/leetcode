class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen=set(nums)
        max_length=0
        for num in seen:
            if num-1 not in seen:
                start = num
                length=1
                while start+1 in seen:
                    length+=1
                    start+=1
                max_length=max(length,max_length)
        return max_length
    
print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))           # 期望 4
print(Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))   # 期望 9
print(Solution().longestConsecutive([]))                                # 期望 0
print(Solution().longestConsecutive([1, 0, 1, 2]))                      # 期望 3
print(Solution().longestConsecutive([7]))   # 期望 1

import time

big = list(range(5000)) + [0] * 5000     # 0~4999 各一个，再加 5000 个 0
begin = time.perf_counter()
print(Solution().longestConsecutive(big))      # 期望 5000
elapsed = time.perf_counter() - begin
print(elapsed)                                 # 期望 0.00x 秒（千分之一秒量级）
                    