class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = ''
        res = 0
        for ch in s:
            if ch not in a:
                a += ch
            else:
                dup_index = a.index(ch)
                a = a[dup_index+1:]+ch
            res = max(res,len(a))
        return res

        