class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        longest = 0 
        for i in nums_set:
            if i-1 not in nums_set:
                cur = i
                streak = 1
                while cur+1 in nums_set:
                    cur += 1
                    streak +=1
                longest = max(longest,streak)
        return longest