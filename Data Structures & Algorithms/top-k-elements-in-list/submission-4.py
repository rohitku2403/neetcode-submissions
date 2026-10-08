
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        res = []
        for num in nums:
            if num not in dict1:
                dict1[num]=1
            else:
                dict1[num]+=1
        for num,val in dict1.items():
            res.append([val,num])
        res.sort()
        ans = []
        while len(ans) < k:
            ans.append(res.pop()[1])
        return ans