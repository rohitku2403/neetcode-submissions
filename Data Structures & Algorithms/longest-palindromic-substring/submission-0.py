class Solution:
    def longestPalindrome(self, s: str) -> str:
        n= len(s)
        res = ""
        for i in range(n):
            left,right = i,i
            while left>=0 and right<n and s[left]==s[right]:
                left-=1
                right+=1
            palindrome = s[left+1:right]
            if len(palindrome)>len(res):
                res= palindrome
            
            left,right = i,i+1
            while left>=0 and right<n and s[left]==s[right]:
                left-=1
                right+=1
            palindrome = s[left+1:right]
            if len(palindrome)>len(res):
                res= palindrome
        return res