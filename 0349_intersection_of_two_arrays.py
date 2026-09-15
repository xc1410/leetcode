def intersection(nums1, nums2):
    nums2_set = set(nums2)  # 用于快速查找
    seen = set()            # 记录已经加入过的数字
    res = []                # 保存结果并保持 nums1 中的顺序

    for num1 in nums1:
        if num1 in nums2_set and num1 not in seen:
            res.append(num1)
            seen.add(num1)

    return res


print(intersection([1, 2, 2, 1], [2, 2]))          # 期望 [2]      ← 证伪数据，必须跑
print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))    # 期望 [9, 4]   ← 顺序无所谓
print(intersection([1, 2, 3], [4, 5, 6]))          # 期望 []       ← 空结果