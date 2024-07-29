# Time Complexity : O(n), where is the length of the temperatures list
# Space Complexity : O(n)

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []  # This will be the decreasing stack
        
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                ans[index] = i - index
            stack.append(i)
        
        return ans

# Example 1
temperatures1 = [73, 74, 75, 71, 69, 72, 76, 73]
solution1 = Solution()
print(solution1.dailyTemperatures(temperatures1))  # returns [1, 1, 4, 2, 1, 1, 0, 0]

# Example 2
temperatures2 = [30, 40, 50, 60]
solution2 = Solution()
print(solution2.dailyTemperatures(temperatures2))  # returns [1, 1, 1, 0]

# Example 3
temperatures3 = [30, 60, 90]
solution3 = Solution()
print(solution3.dailyTemperatures(temperatures3))  # returns [1, 1, 0]