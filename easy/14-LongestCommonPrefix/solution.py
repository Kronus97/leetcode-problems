from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 

solution = Solution()

firstTest = solution.longestCommonPrefix(["flower", "flow", "flight"])
secondTest = solution.longestCommonPrefix(["dog", "racecar", "car"])

print("['flower', 'flow', 'flight']", " -> ", "✓" if firstTest == "fl" else "✕")
print("['dog', 'racecar', 'car']", " -> ", "✓" if secondTest == "" else "✕")