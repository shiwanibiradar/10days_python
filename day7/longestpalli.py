class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPalSub = ''
        for i in range(len(s)):
            center = self.expandAroundCenter(s, i, i)
            inBetween = self.expandAroundCenter(s, i, i+1)
            longestPalSub = max(longestPalSub, center, inBetween, key = len)
        return longestPalSub
    
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]
                
