// https://leetcode.com/problems/implement-queue-using-stacks

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack1:
            return self.stack2.pop()
        elif not self.stack2:
            self.shift()
        return self.stack2.pop()

        

    def peek(self) -> int:
        if not self.stack1:
            return self.stack2[-1]
        elif not self.stack2:
            self.shift()
        return self.stack2[-1]
        

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2
    
    def shift(self) -> None:
        while self.stack1:
            x = self.stack1.pop()
            self.stack2.append(x)
                


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

