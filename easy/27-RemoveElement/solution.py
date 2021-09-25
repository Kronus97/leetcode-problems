from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        return k

solution = Solution()
nums = [3, 2, 2, 3]

firstTest = solution.removeElement(nums, 3)
print("[3, 2, 2, 3], 3", " -> ", "✓" if nums[:firstTest] == [2, 2] else "✕")