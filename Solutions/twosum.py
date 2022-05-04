class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, v in enumerate(nums):
            difference = target - v
            if difference in map: 
                return [i, map[difference]]
            map[v] = i