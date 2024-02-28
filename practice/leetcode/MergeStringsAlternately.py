class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        j = 0
        str1 = ""
        if len(word1) > len(word2):
            for i in word1:
                str1 += i
                if j < len(word2):
                    str1 += word2[j]
                    j += 1
        else:
            for i in word2:
                if j < len(word1):
                    str1 += word1[j]
                    j += 1
                str1 += i
        return str1


s = Solution()
a = "asdasd"
b = "asdss"
print(s.mergeAlternately(a, b))
