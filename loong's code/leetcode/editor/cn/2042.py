class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        digital = ''
        list1=[]
        for i in s:
            if i.isdigit():
                digital += i
            else:
                if digital != '':
                    list1.append(digital)
                    digital = ''
        if digital != '':
            list1.append(digital)
        for i in range(1, len(list1)):
            if int(list1[i]) <= int(list1[i-1]):
                return False
        return True
print(Solution.areNumbersAscending(Solution,s = "hello world 5 x 5"))