class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = [0]
        dict = { 0: None, "[": "]", "{": "}", "(": ")" }
        for char in s:
            if char in dict:
                stack.append(char)
            else:
                if dict[stack.pop()] != char: return False
        
        return stack == [0]

solution = Solution()

firstTest = solution.isValid("()")
secondTest = solution.isValid("()[]{}")
thirdTest = solution.isValid("(]")
fourthTest = solution.isValid("([)]")
fifthTest = solution.isValid("{[]}")

print("()", " -> ", "✓" if firstTest == True else "✕")
print("()[]{}", " -> ", "✓" if secondTest == True else "✕")
print("(]", " -> ", "✓" if thirdTest == False else "✕")
print("([)]" " -> ", "✓" if fourthTest == False else "✕")
print("{[]}", " -> ", "✓" if fifthTest == True else "✕")