import time


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        length = len(nums)
        k %= length
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, length - 1)
        reverse(0, k - 1)
        reverse(k, length - 1)

def after_rotate(nums, k):
    Solution().rotate(nums, k)
    return nums

print(after_rotate([1, 2, 3, 4, 5, 6, 7], 3))   # 期望 [5, 6, 7, 1, 2, 3, 4]
print(after_rotate([-1, -100, 3, 99], 2))       # 期望 [3, 99, -1, -100]
print(after_rotate([1, 2], 3))                  # 期望 [2, 1]
print(after_rotate([1], 0))                     # 期望 [1]
print(after_rotate([1, 2, 3], 0))               # 期望 [1, 2, 3]
print(after_rotate([1, 2, 3], 3))               # 期望 [1, 2, 3]
print(after_rotate([1, 2, 3, 4, 5, 6], 4))      # 期望 [3, 4, 5, 6, 1, 2]
print(after_rotate([1, 2, 3, 4, 5], 12))        # 期望 [4, 5, 1, 2, 3]

big = list(range(100000))
begin = time.perf_counter()
Solution().rotate(big, 12345)
print(time.perf_counter() - begin)
print(len(big), big[0], big[12344], big[12345], big[-1])   # 期望 100000 87655 99999 0 87654