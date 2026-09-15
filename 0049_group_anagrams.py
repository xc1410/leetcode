# 0049 字母异位词分组
# v1 dict 频次表 → tuple(sorted(items))   31 ms  击败 5%
# v2 tuple(sorted(word)) 直接当 key       17 ms  击败 24.76%
# v2' 仅改变量名 seen_i → seen_key        11 ms  击败 94.29%
#
# 三次读数的结论：v1→v2 有机制（每词少建一个 dict），45% 提速可信；
# v2→v2' 只改了名字，17→11 的 35% 差距纯属判题机噪声。
# ⇒ LeetCode 单次耗时波动 ≥±35%，小于这个幅度的差异读不出来。
#
# 进阶：26 长度的计数列表转 tuple 当 key，O(n·k) 无 log，
#       但每词固定造 26 格，k 小时未必更快。
# 坑：list 不能当 dict 的 key（可变 → 哈希值会变）
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res={}
        final_res=[]
        for word in strs:
            seen_i = tuple(sorted(word))
            if seen_i not in res:
                res[seen_i]=[]
            res[seen_i].append(word)
        for value in res.values():
            final_res.append(value)
        return final_res
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res={}
        final_res=[]
        for word in strs:
            seen_key = tuple(sorted(word))
            if seen_key not in res:
                res[seen_key]=[]
            res[seen_key].append(word)
        for value in res.values():
            final_res.append(value)
        return final_res
            
        
        
        
        