def intersection(nums1, nums2):
    pass                       # ← 现在不写


print(intersection([1, 2, 2, 1], [2, 2]))          # 期望 [2]      ← 证伪数据，必须跑
print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))    # 期望 [9, 4]   ← 顺序无所谓
print(intersection([1, 2, 3], [4, 5, 6]))          # 期望 []       ← 空结果