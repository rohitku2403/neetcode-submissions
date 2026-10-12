class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res=0
        li,ri = 0,len(heights)-1
        while li<ri:
            area = min(heights[li],heights[ri])*(ri-li)
            res = max(area,res)
            if li<ri:
                li+=1
            else:
                ri-=1
        return res
        