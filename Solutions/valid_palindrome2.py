class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                leftEnd, rightEnd = s[left+1:right+1], s[left:right]
                return (leftEnd == leftEnd[::-1] or rightEnd == rightEnd[::-1])
            left, right = left+1, right-1
        return True