# 0242 有效的字母异位词
# 双 dict 计数 + 比较   11 ms / 19.23 MB
# 第一次 WA：粘贴到 LeetCode 时 seen_s[char]+=1 掉了一级缩进
def is_anagram(s, t):
    seen_s={}
    seen_t={}
    for char in s:
        if char not in seen_s:
            seen_s[char]=0
        seen_s[char]+=1
    for char in t:
        if char not in seen_t:
            seen_t[char]=0
        seen_t[char]+=1           
    return seen_s==seen_t
print(is_anagram("anagram", "nagaram"))   # 期望 True
print(is_anagram("rat", "car"))           # 期望 False
print(is_anagram("a", "ab"))              # 期望 False，长度不等
print(is_anagram("aacc", "ccac"))         # 期望 False，长度相等、字符集相同、计数不同