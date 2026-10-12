class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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

        