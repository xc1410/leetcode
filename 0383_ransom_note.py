# 0383 赎金信｜单 dict 扣库存｜9/15
#
# 三版，130/130，全程无 WA
#   v1  双 dict 交叉比对，三次遍历      47 ms   5.11%
#   v1' 先建 magazine 表，三次改两次    29 ms  20.89%
#   v2  单 dict 扣库存                  35 ms  10.20%
#
# 29 → 35 ms：遍历次数不变，没有机制 ⇒ 噪声，不是退步（4.9）
#
# v1 的 seen_ransomNote[char] + 1 < seen_magazine[char]：
#   那个 < 因为计数从 0 开始的偏移，恰好等价于正常写法的 <= ，130/130 全过，
#   但对得莫名其妙 ⇒ 名字骗了自己：以为它装"用了几个"，实际装"用了几个减一"
#   v2 改成扣库存后歧义消失
#   ⇒ 4.1 第 3 条：seen 不是"dict 的默认名字"，它有具体含义
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        seen_ransomNote={}
        seen_magazine={}
        for char in ransomNote:
            if char not in seen_ransomNote:
                seen_ransomNote[char]=0
            seen_ransomNote[char]+=1
        for char in magazine:
            if char not in seen_magazine:
                seen_magazine[char]=0
            seen_magazine[char]+=1
        for key,value in seen_ransomNote.items():
            if key not in seen_magazine:
                return False
            elif value>seen_magazine[key]:
                return False
        return True
        class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        seen_ransomNote={}
        seen_magazine={}
        for char in magazine:
            if char not in seen_magazine:
                seen_magazine[char]=0
            seen_magazine[char]+=1
        for char in ransomNote:
            if char not in seen_ransomNote and char in seen_magazine:
                seen_ransomNote[char]=0
            elif char  in seen_ransomNote and char not in seen_magazine:
                return False
            elif char  in seen_ransomNote and seen_ransomNote[char]+1<seen_magazine[char]:
                seen_ransomNote[char]+=1
            else:
                return False
        
            

      
        return True
        
        
        