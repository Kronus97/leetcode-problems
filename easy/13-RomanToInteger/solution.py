class Solution:
    def romanToInt(self, s: str) -> int:
        romanValues = { "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1 }
        result = 0

        for i in range(0, len(s) - 1):
            if romanValues[s[i]] > romanValues[s[i+1]] or romanValues[s[i]] == romanValues[s[i+1]]:
                result += romanValues[s[i]]
            else:
                result -= romanValues[s[i]]

        return result + romanValues[s[-1]]


solution = Solution()

firstTest = solution.romanToInt("III")
secondTest = solution.romanToInt("IV")
thirdTest = solution.romanToInt("IX")
fourthTest = solution.romanToInt("LVIII")
fifthTest = solution.romanToInt("MCMXCIV")

print("III", " -> ", "✓" if firstTest == 3 else "✕")
print("IV", " -> ", "✓" if secondTest == 4 else "✕")
print("IX", " -> ", "✓" if thirdTest == 9 else "✕")
print("LVIII" " -> ", "✓" if fourthTest == 58 else "✕")
print("MCMXCIV", " -> ", "✓" if fifthTest == 1994 else "✕")