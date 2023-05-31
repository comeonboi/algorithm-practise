class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        result =""
        is_reverse = 1
        if k >= len(s):
            return s[::-1]
        for i in range(n):
            if (i+1) % k == 0 and is_reverse == 1:
                if i == k-1:
                    result += s[i::-1]
                else:
                    result += s[i:i-k:-1]
                is_reverse = 0
            elif (i+1) % k == 0 and is_reverse == 0:
                result += s[i+1-k:i+1]
                is_reverse = 1
        if len(result)<n and is_reverse==0:
            result+=s[len(result):]
        else:
            result+=s[n-1:len(result)-1:-1]
        return result