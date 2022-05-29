class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count1 = Counter(magazine)
        count2 = Counter(ransomNote)
        
        for i in count2:
            if count1[i] < count2[i]:
                return False
        return True
