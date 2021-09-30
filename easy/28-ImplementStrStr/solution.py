class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0;

        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1

solution = Solution()

firstTest = solution.strStr("abc", "bc")
secondTest = solution.strStr("", "")
thirdTest = solution.strStr("aaaaa", "ba")

print("strStr('abc','bc')", " -> ", "✓" if firstTest == 1 else "✕")
print("strStr('','')", " -> ", "✓" if secondTest == 0 else "✕")
print("strStr('aaaaa','ba')", " -> ", "✓" if thirdTest == -1 else "✕")