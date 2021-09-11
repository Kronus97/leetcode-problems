class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10 
            x //= 10

        return x == revertedNumber or x == revertedNumber // 10


solution = Solution()

firstTest = solution.isPalindrome(121)
secondTest = solution.isPalindrome(-121)
thirdTest = solution.isPalindrome(10)
fourthTest = solution.isPalindrome(0)

print("121", " -> ", "✓" if firstTest == True else "✕")
print("-121", " -> ", "✓" if secondTest == False else "✕")
print("10", " -> ", "✓" if thirdTest == False else "✕")
print("0", " -> ", "✓" if fourthTest == True else "✕")
