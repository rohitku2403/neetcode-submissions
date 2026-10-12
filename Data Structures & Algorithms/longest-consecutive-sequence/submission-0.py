class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            swapped= False
            for j in range(n-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
                    swapped = True
                    if not swapped:
                        break
        b = []
        for i in nums:
            if i not in b:
                b.append(i)

        a = 0
        res = 1
        for i in range(1,n):
            if nums[i]==nums[a]+1:
                res+=1
                a+=1
            else:
                a+=1

        return res

        