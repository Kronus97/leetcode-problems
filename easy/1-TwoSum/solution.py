from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index, num in enumerate(nums):
            if target - num in dict:
                return [dict[target - num], index]
            dict[num] = index


solution = Solution()

firstTest = solution.twoSum([2, 7, 11, 15, 9], 9)
secondTest = solution.twoSum([3, 2, 4], 6)
thirdTest = solution.twoSum([3, 3], 6)

print(firstTest, " -> ", "✓" if firstTest == [0, 1] else "✕")
print(secondTest, " -> ", "✓" if secondTest == [1, 2] else "✕")
print(thirdTest, " -> ", "✓" if thirdTest == [0, 1] else "✕")