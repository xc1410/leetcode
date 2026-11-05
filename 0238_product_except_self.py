import time


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length=len(nums)
        answer=[1]*length

        left=1
        for i in range(length):
            answer[i]=left
            left*=nums[i]
        
        right=1
        for i in range(length-1,-1,-1):
            answer[i]*=right
            right*=nums[i]

        return answer


print(Solution().productExceptSelf([1, 2, 3, 4]))          # 期望 [24, 12, 8, 6]
print(Solution().productExceptSelf([-1, 1, 0, -3, 3]))     # 期望 [0, 0, 9, 0, 0]
print(Solution().productExceptSelf([2, 3]))                # 期望 [3, 2]
print(Solution().productExceptSelf([0, 0]))                # 期望 [0, 0]
print(Solution().productExceptSelf([0, 4, 5]))             # 期望 [20, 0, 0]
print(Solution().productExceptSelf([-2, -3, 4]))           # 期望 [-12, -8, 6]
print(Solution().productExceptSelf([5, 0, -1, 0]))         # 期望 [0, 0, 0, 0]
print(Solution().productExceptSelf([3, 3, 3, 3, 3]))       # 期望 [81, 81, 81, 81, 81]

big = [1] * 100000
big[0] = 2
big[-1] = 3
begin = time.perf_counter()
result = Solution().productExceptSelf(big)
print(time.perf_counter() - begin)
print(len(result), result[0], result[1], result[-1])   # 期望 100000 3 6 2