class MyQueue:

    def __init__(self):
        self.MyQueue = []

    def push(self, x: int) -> None:
        self.MyQueue.append(x)
        return None

    def pop(self) -> int:
        a = self.MyQueue[0]
        self.MyQueue.remove(self.MyQueue[0])
        return a

    def peek(self) -> int:
        return self.MyQueue[0]


    def empty(self) -> bool:
        return not self.MyQueue