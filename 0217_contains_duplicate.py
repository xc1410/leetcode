def contains_duplicate(nums):
    unique=set(nums)
    if len(unique)==len(nums):
        return False
    else :
        return True


print(contains_duplicate([1, 2, 3, 4]))     # 期望 False
print(contains_duplicate([1, 2, 3, 1]))     # 期望 True
print(contains_duplicate([1]))              # 期望 False  ← 边界