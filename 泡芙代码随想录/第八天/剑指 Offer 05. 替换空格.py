class Solution:
    def replaceSpace(self, s: str) -> str:
        s_list = s.split(" ")
        result = ""
        for i in range(len(s_list)):
            if i != len(s_list)-1:
                result+=s_list[i]
                result+="%20"
            else:
                result+=s_list[i]
        return result
