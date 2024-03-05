# class Solution:
#     def repeatedSubstringPattern(self, s: str) -> bool:
#         # 明确原始字符串的长度
#         s_len = len(s)
#         # 遍历字符串，利用字符串切片得到新的子串new。
#         # 注意：s = "abab",  s[0:0]为“” ， s[0:1] 为 "a", 因此range(1,s_len)
#         for i in range(1,s_len):
#             new = s[0:i]
#             n_len = len(new)
#             # 重复的次数 等于 原始字符串的长度 地板除 新的子串new的长度
#             repeat_times = s_len//n_len
#             # 如果重复的次数大于1， 并且用每次得到的 新的子串new 乘以 重复的次数，判断是否会与 原始字符串相等
#             # 如果有一次可相等， 则返回True，否则False
#             if repeat_times > 1 and new * repeat_times == s:
#                 return True
#         return False


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s = len(s)
