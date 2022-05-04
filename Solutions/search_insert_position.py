class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for i in range(0,len(nums)):
                if nums[i] < target:
                    continue
                else:
                    return i
                    break
            return len(nums)