class SolutionSort:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen = sorted(set(nums))
        longest=1
        length=1
        if len(seen) <=1 :
            return len(seen)
        for i in range(1,len(seen)):
            if seen[i]-seen[i-1]==1:
                length+=1
            else:
                length=1
            longest=max(longest,length)

        return longest


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen=set(nums)
        length=0
        max_len=0
        for num in seen:
            if num-1 not in seen:
                length=1
                start =num
                while (start+1) in seen:
                    length+=1
                    start+=1
                max_len=max(length,max_len)
        return max_len
                    
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
print(SolutionSort().longestConsecutive(big))  # 期望 5000，也是毫秒级


        