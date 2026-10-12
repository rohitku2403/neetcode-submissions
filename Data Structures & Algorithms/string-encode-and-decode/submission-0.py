class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ''
        lenn=''
        for i in strs:
            lenn += str(len(i))
            res +=  i
        return str(len(lenn))+lenn+res

    def decode(self, s: str) -> List[str]:
        count = int(s[0])
        len_word=[]
        for i in range(1,count+1):
            len_word.append(int(s[i]))
        s = s[count+1:]
        res=[]
        for i in len_word:
            ans = s[0:i]
            res.append(ans)
            s=s[i:]
        return res