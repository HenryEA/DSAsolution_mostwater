class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        maxArea = 0

        while l < r:
            curArea = min(height[l], height[r]) *(r-l)
            maxArea = max(curArea, maxArea)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1

        return maxArea