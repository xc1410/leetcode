class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        zero_count=0
        for idx in range(len(nums)):
            if nums[idx]==0:
                zero_count+=1
            else:
                nums[idx-zero_count],nums[idx]=nums[idx],nums[idx-zero_count]
    


for nums in [[0, 1, 0, 3, 12], [2, 1, 0], [0, 0, 1], [0]]:
    Solution().moveZeroes(nums)
    print(nums)
# 期望 [1, 3, 12, 0, 0] / [2, 1, 0] / [1, 0, 0] / [0]