def two_sum(nums,target):
    seen={}
    for idx in range(len(nums)):
        if target-nums[idx] not in seen:
            seen[nums[idx]]=idx
        elif target-nums[idx]  in seen:
            return [seen[target-nums[idx]],idx]
        
print(two_sum([2, 7, 11, 15], 9))   # 期望 [0, 1]
print(two_sum([3, 2, 4], 6))        # 期望 [1, 2]
print(two_sum([3, 3], 6))           # 期望 [0, 1]
print(two_sum([3, 3, 4], 7))        # 期望 [1, 2]