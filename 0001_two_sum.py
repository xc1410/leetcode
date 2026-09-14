def two_sum_hash(nums, target):
    seen={}
    for idx in range(len(nums)):
        if target-nums[idx] not in seen:
            seen[(nums[idx])]=idx
        elif target-nums[idx]  in seen:
            return [seen[target-nums[idx]],idx]
        

    
    


print(two_sum_hash([2, 7, 11, 15], 9))   # 期望 [0, 1]
print(two_sum_hash([3, 2, 4], 6))        # 期望 [1, 2]
print(two_sum_hash([3, 3], 6))           # 期望 [0, 1]
print(two_sum_hash([3, 3, 4], 7))        # 期望 [1, 2]
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for c in range(i+1,len(nums)):
                if nums[i]+nums[c]==target :
                    b=[i,c]
                    return b



    
        