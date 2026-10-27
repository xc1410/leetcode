class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        result = []
        n = len(nums)
        for first in range(n - 2):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            if nums[first] > 0:
                break
            left = first + 1
            right = n - 1
            while left < right:
                total = nums[first] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    result.append([
                        nums[first], nums[left], nums[right]
                    ])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result

print(sorted(Solution().threeSum([-1, 0, 1, 2, -1, -4])))   # 期望 [[-1, -1, 2], [-1, 0, 1]]
print(sorted(Solution().threeSum([0, 1, 1])))               # 期望 []
print(sorted(Solution().threeSum([0, 0, 0])))               # 期望 [[0, 0, 0]]
print(sorted(Solution().threeSum([0, 0, 0, 0])))            # 期望 [[0, 0, 0]]   只能有一组
print(sorted(Solution().threeSum([-2, 0, 0, 2, 2])))        # 期望 [[-2, 0, 2]]  只能有一组

import time

big = list(range(1, 1001)) + [0, 0, 0]    # 1000 个正数，只有 [0, 0, 0] 一组解
begin = time.perf_counter()
print(Solution().threeSum(big))           # 期望 [[0, 0, 0]]
print(time.perf_counter() - begin)        # 期望 0.0x–0.1 秒，更快也对