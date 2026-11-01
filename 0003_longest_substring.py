import time
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=len(s)
        start=0
        result=0
        while start < length :
            seen=set()
            for begin in range(start,length):
                if s[begin] not in seen:
                    seen.add(s[begin] )
                    result=max(result,len(seen))
                else:
                    break
            start+=1
        return result


print(Solution().lengthOfLongestSubstring("abcabcbb"))   # 期望 3   "abc"
print(Solution().lengthOfLongestSubstring("bbbbb"))      # 期望 1
print(Solution().lengthOfLongestSubstring("pwwkew"))     # 期望 3   "wke"
print(Solution().lengthOfLongestSubstring(""))           # 期望 0
print(Solution().lengthOfLongestSubstring(" "))          # 期望 1   空格也是字符
print(Solution().lengthOfLongestSubstring("abba"))       # 期望 2
print(Solution().lengthOfLongestSubstring("dvdf"))       # 期望 3
big = "abcdefghij" * 300
begin = time.perf_counter()
print(Solution().lengthOfLongestSubstring(big))   # 期望 10
print(time.perf_counter() - begin)                # 期望 0.00x 秒