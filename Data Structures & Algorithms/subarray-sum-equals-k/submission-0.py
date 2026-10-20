class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_freq = {0:1}
        ans=0
        prefix_sum = 0
        for i in nums:
            prefix_sum += i
            ans+= prefix_freq.get(prefix_sum-k,0)
            prefix_freq[prefix_sum] = prefix_freq.get(prefix_sum,0)+1
        return ans
        