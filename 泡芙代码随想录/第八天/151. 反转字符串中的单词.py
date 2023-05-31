class Solution:
    def reverseWords(self, s: str) -> str:
        print(s.strip())
        s_list = (s.strip()).split()
        i = 0
        j = len(s_list)-1
        while i<j:
            s_list[i],s_list[j] = s_list[j],s_list[i]
            i+=1
            j-=1
        result = ""
        for i in range(len(s_list)):
            if i != len(s_list)-1 :
                result+= s_list[i]
                result += " "
            elif i == len(s_list)-1 and s_list[i]!= ' ':
                result+= s_list[i]
            else:
                continue
        return result