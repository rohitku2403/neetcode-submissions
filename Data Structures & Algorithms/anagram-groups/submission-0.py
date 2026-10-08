
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==1:
            return [strs]
        res = {}
        for val in strs:
            str1 = str(sorted(val))
            if str1 not in res:
                res[str1]=[val]
            else:
                res[str1].append(val)
        return list(res.values())