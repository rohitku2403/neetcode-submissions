class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for ind,i in enumerate(nums):
            if target-i in nums and ind!=nums.index(target-i):
                return ([ind,nums.index(target-i)])
                
        