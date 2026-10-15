class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def count(nums,k):
            if k==0:
                return 0
            left = 0
            ans = 0
            freq = {}
            for right in range(len(nums)):
                freq[nums[right]] = freq.get(nums[right],0)+1
                while len(freq)>k:
                    freq[nums[left]]-=1
                    if freq[nums[left]] == 0:
                        del freq[nums[left]]       
                    left+=1
                ans += (right-left+1)
            return ans
        return count(nums,k)-count(nums,k-1) 