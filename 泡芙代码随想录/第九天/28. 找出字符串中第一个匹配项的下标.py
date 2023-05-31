class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        pre_list = [0 for i in range(len(needle))]
        j = 0
        for i in range(1,len(needle)):
            while j > 0 and needle[i] != needle[j]:
                j = pre_list[j-1]
            if needle[i] == needle[j]:
                j+=1
            pre_list[i]=j
        i = 0
        j = 0
        while j < len(needle) and i <len(haystack):
            print(i,j,pre_list)
            if (haystack[i] == needle[j] and j == (len(needle)-1)):
                return i-len(needle)+1
            elif (haystack[i] == needle[j]):
                i+=1
                j+=1
            else:
                if j == 0:
                    i+=1
                else:
                    j = pre_list[j-1]
        return -1