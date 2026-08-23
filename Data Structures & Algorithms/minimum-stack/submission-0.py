class MinStack:

    def __init__(self):
        self.stack = [] # (val, min)
        

    def push(self, val: int) -> None:
        
        min = val

        if self.stack:
            top_tuple =  self.stack[-1]
            top_tuple_min = top_tuple[1]

            if val > top_tuple_min:
                min = top_tuple_min
        
        self.stack.append((val, min))

    def pop(self) -> None:
        self.stack.pop()        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
