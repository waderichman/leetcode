class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if set(s) != set(t):
            return False
        if len(s) != len(t):
            return False
        for i in set(t):
            if s.count(i) != t.count(i):
                return False
        return True
    