# 0202 快乐数｜set 判环｜9/16
#
# 三版：
#   v1  seen 是 list，if n in seen                     O(n) 查
#   v2  seen 仍是 list，每轮 set(seen) 再查            ← 反而更差：每轮 O(n) 重建哈希表
#   v3  seen 从一开始就是 set()，add + in             O(1) 查
#   ⇒ set 的快不来自"类型是 set"，来自哈希表在【插入那一刻】就建好了
#   ⇒ 每轮重建 = 把建好的东西扔掉再建一遍，等于没换
#
# 耗时读数（0 ms / 3 ms / 0 ms）在这题上没有分辨率：输入是单个整数，
#   计算量小到判题机量不出来。三版的差异【不能】用这些数字证明（4.9）
class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n != 1:
            seen.add(n)
            next_num=0
            while n != 0:
                last_num=n%10
                next_num+=last_num**2
                n=n//10
            if next_num in seen:
                return False
            n=next_num
        return True

print(Solution().isHappy(19))   # 期望 True
print(Solution().isHappy(2))    # 期望 False   ← 会进环，没有这组等于没测
print(Solution().isHappy(1))    # 期望 True    ← 边界，一步不用走
print(Solution().isHappy(7))    # 期望 True    ← 要绕好几圈才到 1

            
            
            

