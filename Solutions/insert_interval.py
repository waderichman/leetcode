class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        for index, num in enumerate(intervals):
            if num[1] < newInterval[0]:
                ans.append(num)
            elif newInterval[1] < num[0]:
                ans.append(newInterval)
                return ans+intervals[index:]
            else:
                 newInterval[0] = min(newInterval[0], num[0])
                 newInterval[1] = max(newInterval[1], num[1])
        ans.append(newInterval)
        return ans