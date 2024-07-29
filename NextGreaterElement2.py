# Time Complexity : O(n)
# Space Complexity : O(n)
from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        n = len(nums)
        result = [-1] * n  # Fill the result with -1, which is the default value
        stack = []

        for i in range(n * 2):  # Since it is a circular array, we are iterating till n*2
            while stack and nums[stack[-1]] < nums[i % n]:
                result[stack.pop()] = nums[i % n]
            if i < n:
                stack.append(i)

        return result

# Examples
sol = Solution()

# Example 1
nums1 = [1, 2, 1]
print("Example 1: nums =", nums1)
print("Output:", sol.nextGreaterElements(nums1))
# Expected Output: [2, -1, 2]

# Example 2
nums2 = [3, 8, 4, 1, 2]
print("Example 2: nums =", nums2)
print("Output:", sol.nextGreaterElements(nums2))
# Expected Output: [8, -1, 8, 2, 3]

# Example 3
nums3 = [6, 5, 4, 3, 2, 1]
print("Example 3: nums =", nums3)
print("Output:", sol.nextGreaterElements(nums3))
# Expected Output: [-1, 6, 6, 6, 6, 6]