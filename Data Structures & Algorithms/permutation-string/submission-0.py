class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        c1,c2 = [0]*26,[0]*26
        for i in s1:
            c1[ord(i)-97] += 1
        for i in range(len(s1)):
            c2[ord(s2[i])-97] += 1
        if c1==c2:
            return True
        l=0
        for i in range(len(s1),len(s2)):
            c2[ord(s2[i])-97] +=1
            c2[ord(s2[l])-97] -=1
            if c1 == c2:
                return True
            l += 1
        return False