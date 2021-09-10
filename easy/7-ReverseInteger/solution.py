class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        sign = [1, -1][x < 0]
        x *= sign

        while x != 0:
            tail = x % 10
            newResult = result * 10 + tail
            if (newResult - tail) / 10 != result:
                return 0
            result = newResult
            x //= 10

        return result * sign if -(2**31)-1 < result < 2**31 else 0


solution = Solution()

firstTest = solution.reverse(123)
secondTest = solution.reverse(-123)
thirdTest = solution.reverse(120)
fourthTest = solution.reverse(0)
fifthTest = solution.reverse(1534236469)

print("123", " -> ", "✓" if firstTest == 321 else "✕")
print("-123", " -> ", "✓" if secondTest == -321 else "✕")
print("120", " -> ", "✓" if thirdTest == 21 else "✕")
print("0", " -> ", "✓" if fourthTest == 0 else "✕")
print("123456789", " -> ", "✓" if fifthTest == 0 else "✕")