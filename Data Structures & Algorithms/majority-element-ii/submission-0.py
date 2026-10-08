class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        length = len(nums)//3
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0)+1
            if freq[i]>length and i not in ans:
                ans.append(i)
        return ans