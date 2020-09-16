# Two pointer solution which simply move the smaller side
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans, i, j = 0, 0, len(height)-1
        while(i<j):
            if height[i] < height[j]:
                ans = max(ans, height[i]*(j-i))
                i += 1
            else:
                ans = max(ans, height[j]*(j-i))
                j -= 1
        return ans