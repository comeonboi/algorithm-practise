class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = []
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool:
        self.stream.append(num)
        if len(self.stream[-self.k:]) >= self.k:
            if set(self.stream[-self.k:]) == {self.value}:
                return True
        return False

class DataStream2:

    def __init__(self, value: int, k: int):
        self.stream = {value}
        self.value = value
        self.k = k
        self.flag = 0

    def consec(self, num: int) -> bool:
        if {num} == self.stream:
            self.flag += 1
        else:
            # self.stream.add(num)
            self.flag = 0
        if self.flag >= self.k:
            return True
        return False

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
obj = DataStream(4, 3)
param_1 = obj.consec(4)
print(param_1)
param_1 = obj.consec(4)
print(param_1)
param_1 = obj.consec(4)
print(param_1)
param_1 = obj.consec(3)
print(param_1)
print(
)
obj2 = DataStream2(4, 3)
param_12 = obj2.consec(4)
print(param_12)
param_12 = obj2.consec(4)
print(param_12)
param_12 = obj2.consec(4)
print(param_12)
param_12 = obj2.consec(3)
print(param_12)