from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1

        return left + 1 if nums[left] < target else left

solution = Solution()

firstTest = solution.searchInsert([1, 3, 5, 6], 5)
secondTest = solution.searchInsert([1, 3, 5, 6], 2)
thirdTest = solution.searchInsert([1, 3, 5, 6], 7)
fourthTest = solution.searchInsert([1, 3, 5, 6], 0)
fifthTest = solution.searchInsert([1], 0)

print("searchInsert([1, 3, 5, 6], 5)", " -> ", "✓" if firstTest == 2 else "✕")
print("searchInsert([1, 3, 5, 6], 2)", " -> ", "✓" if secondTest == 1 else "✕")
print("searchInsert([1, 3, 5, 6], 7)", " -> ", "✓" if thirdTest == 4 else "✕")
print("searchInsert([1, 3, 5, 6], 0)", " -> ", "✓" if fourthTest == 0 else "✕")
print("searchInsert([1], 0)", " -> ", "✓" if fifthTest == 0 else "✕")