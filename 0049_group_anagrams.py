# 0049 字母异位词分组｜中等｜约 49 分钟独立通过，未看题解｜9/15
# 第一道独立拿下的中等题。129/129
#
# 三版，key 的造法不同
#   v1  dict 频次表 → tuple(sorted(items()))   31 ms   5.00%
#   v2  tuple(sorted(word)) 直接当 key         17 ms  24.76%
#   v2' 仅把 seen_i 改名成 seen_key            11 ms  94.29%
#
# 31 → 17：每个词少建一个 dict，【有机制】⇒ 真实提升（约 45%）
# 17 → 11：只改了变量名，【无机制】⇒ 纯噪声（35%）
#   ⇒ 判题机读数波动 ≥±35%，本机约 ±7%
#   ⇒ 量到的差异要能用机制解释才是真的。解释不了的，先怀疑测量（4.9）
#
# list 不能当 dict 的 key，tuple 可以：
#   dict 靠哈希值定位，哈希值由内容算出；list 内容可变 ⇒ 哈希值会变 ⇒ dict 再也找不到它
#   能当 key：int str float tuple frozenset｜不能：list dict set
#   看到 TypeError: unhashable type 就是这件事
#
# 进阶解法：26 长度的计数列表转 tuple 当 key，O(n·k) 无 log
#   已口头答出，未实现
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
            
        
        
        
        