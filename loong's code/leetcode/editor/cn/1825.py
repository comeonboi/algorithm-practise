class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.list1 = []

    def addElement(self, num: int) -> None:
        self.list1.append(num)

    def calculateMKAverage(self) -> int:
        if len(self.list1) < self.m:
            return -1
        else:
            list2 = self.list1[-1:-self.m-1:-1]
            list2 = sorted(list2)
            list2 = list2[self.k:len(list2) - self.k]
        return sum(list2) // len(list2)


# Your MKAverage object will be instantiated and called as such:
obj = MKAverage(3, 1)
obj.addElement(3)
obj.addElement(1)
param_2 = obj.calculateMKAverage()
print(param_2)
obj.addElement(10)
param_2 = obj.calculateMKAverage()
print(param_2)
obj.addElement(5)
obj.addElement(5)
obj.addElement(5)
param_2 = obj.calculateMKAverage()
print(param_2)
