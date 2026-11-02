import time


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        need=[0]*26
        win=[0]*26
        n=len(s)
        m=len(p)
        if n<m:
            return []
        for char in p:
            need[ord(char)-97]+=1
        res=[]
        for i,c in enumerate(s):
            win[ord(c)-97]+=1
            if i>=m:
                win[ord(s[i-m])-97]-=1
            if i>=m-1 and win==need:
                res.append(i-m+1) 
        return res


print(sorted(Solution().findAnagrams("cbaebabacd", "abc")))   # 期望 [0, 6]
print(sorted(Solution().findAnagrams("abab", "ab")))          # 期望 [0, 1, 2]
print(sorted(Solution().findAnagrams("a", "ab")))             # 期望 []
print(sorted(Solution().findAnagrams("baa", "aa")))           # 期望 [1]
print(sorted(Solution().findAnagrams("abb", "aab")))          # 期望 []
print(sorted(Solution().findAnagrams("aaaa", "aa")))          # 期望 [0, 1, 2]
print(sorted(Solution().findAnagrams("abacbabc", "abc")))     # 期望 [1, 2, 3, 5]

big_s = "abcdefghij" * 3000
big_p = "abcdefghij" * 50
begin = time.perf_counter()
print(len(Solution().findAnagrams(big_s, big_p)))   # 期望 29501
print(time.perf_counter() - begin)