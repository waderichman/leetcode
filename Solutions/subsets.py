class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for i in nums:
            for j in range(len(result)):
                result.append(result[j] + [i])
        return result