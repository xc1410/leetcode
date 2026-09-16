# 0242 有效的字母异位词｜双 dict 计数后直接比较｜9/15
#
# 本地四组全过，线上第一次 WA，44/55，挂在 s="ab", t="ba"
# 分诊（14.2）：本地过、线上挂 ⇒ 搬运 bug，不是逻辑 bug，先逐行比对两份代码
# 根因：粘贴进 LeetCode 时 seen_s[char] += 1 掉了一级缩进，跑到 for 外面
#   ⇒ Python 缩进错位经常不报语法错误，只是悄悄改变语义
#   ⇒ "我提交的东西"和"我写的东西"之间，永远有一个可能出错的搬运环节
#
# 第一版手动遍历比对跑出 KeyError: 't'，被第二组测试数据 ("rat","car") 抓到
# 最终 55/55，11 ms 击败 74.27% / 19.23 MB 击败 54.63%
#
# 空间复杂度 O(1)：题面限定小写字母，dict 最多 26 个 key，是常数
#   对照 0349 允许任意整数 ⇒ set 真的跟着输入涨 ⇒ O(n)
#   ⇒ 同样是"开一个容器计数"，差别不在代码，在题面条件
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