class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=='':
            return 0
        res = []
        a=''
        for i in s:
            if i not in a:
                a+=i
            else:
                res.append(len(a))
                a=''
                a+=i
        return max(res)

        