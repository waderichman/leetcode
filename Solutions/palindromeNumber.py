class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans = str(x)
        return ans == ans[::-1]