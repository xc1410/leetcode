import numpy as np
def intersection(nums1,nums2):
    seen=set()
    res=[]
    nums2_set=set(nums2)
    for num1 in nums1:
        if num1 in nums2_set and num1 not in seen:
            seen.add(num1)
            res.append(num1)
    return res

print(intersection([1, 2, 2, 1], [2, 2]))          # 期望 [2]      ← 证伪数据，必须跑
print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))    # 期望 [9, 4]   ← 顺序无所谓
print(intersection([1, 2, 3], [4, 5, 6]))          # 期望 []       ← 空结果
# 造一个 (2,3,4) 的随机数组

random1=np.random.randn(2,3,4)
# reshape 成 (6,4)
random2 = random1.reshape(6,4)
# assert 它的 shape
assert random2.shape == (6,4),random2.shape