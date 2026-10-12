from typing import List
class Solution:
    def encode(self, strs: List[str]) -> str:
        lens = [str(len(s)) for s in strs]
        return str(len(lens)) + '#' + '#'.join(lens) + '#' + ''.join(strs)

    def decode(self, s: str) -> List[str]:
        i = s.index('#')
        n = int(s[:i])  # number of words
        s = s[i+1:]
        parts = s.split('#', n+1)
        lengths = list(map(int, parts[:n]))
        s = parts[n]
        res = []
        for l in lengths:
            res.append(s[:l])
            s = s[l:]
        return res