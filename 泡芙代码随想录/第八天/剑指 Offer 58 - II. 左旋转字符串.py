class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        i = 0
        while(i<n):
            s+=s[i]
            i+=1
        return s[n:]