class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        max_seen, min_seen = float("-inf"), float("inf")
        start_subarray, end_subarray = 0, -1        
        left, right = 0, len(nums) - 1
        
        while right >= 0:
            max_seen = max(max_seen, nums[left])
            if nums[left] < max_seen:
                end_subarray = left
            left += 1
			
			
            min_seen = min(min_seen, nums[right])
            if nums[right] > min_seen:
                start_subarray = right
            right -= 1

        return end_subarray - start_subarray + 1