class Solution:
    def isPalindrome(self, s: str) -> bool:
        b='abcdefghijklmnopqrstuvwxyz'
        c='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        d='0123456789'
        a = ''
        for i in s:
            if i in b or i in c or i in d:
                a+=i
        if a.lower()==a[::-1].lower():
            return True
        return False

        