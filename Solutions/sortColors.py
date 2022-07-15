class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, white, blue = [], [], []
        for i in nums:
            if i == 0:
                red.append(i)
            if i == 1:
                white.append(i)
            if i == 2:
                blue.append(i)
        nums[:] = (red+white+blue)
        return nums