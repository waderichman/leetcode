class Solution:
    def maxArea(self, height: List[int]) -> int:
        beginning = 0
        end = len(height)-1
        maxArea = 0
        
        while beginning < end:
            leftHeight = height[beginning]
            rightHeight = height[end]
            area = min(leftHeight,rightHeight)*(end-beginning)
            maxArea = max(area, maxArea)
            if leftHeight < rightHeight:
                beginning = beginning + 1
            else:
                end = end - 1
        return maxArea
            