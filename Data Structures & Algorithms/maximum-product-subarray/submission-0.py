class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxp,minp,ans = nums[0],nums[0],nums[0]
        
        for i in nums[1:]:
            prev_max = maxp
            prev_min = minp

            maxp = max(i,i*prev_min,i*prev_max)
            minp = min(i,i*prev_max,i*prev_min)
            ans = max(ans,maxp)
        return ans