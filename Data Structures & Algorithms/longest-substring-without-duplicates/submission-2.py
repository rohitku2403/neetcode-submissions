class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        b=''
        c=[]
        for i in s:
            if i not in b:
                b+=i
            else:
                c.append(len(b))
                b=''
                b+=i
        return(max(c))

        