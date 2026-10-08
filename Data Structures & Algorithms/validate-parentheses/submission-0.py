class Solution:
    def isValid(self, s: str) -> bool:
        lisst=[]
        dict1={'}':'{',']':'[',')':'('}
        for i in s:
            if i in dict1:
                inp_ele = lisst.pop() if lisst else "#"
                if inp_ele!=dict1[i]:
                    return False
            else:
                lisst.append(i)
        return not lisst