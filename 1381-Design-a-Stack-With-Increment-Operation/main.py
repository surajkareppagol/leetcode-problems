# Author: Suraj K

from typing import *


class CustomStack:
    def __init__(self, maxSize: int):
        self.maxSize = max(maxSize, 0)

        self.stack = []
        self.current_size = -1

    def push(self, x: int) -> None:
        if self.current_size < self.maxSize - 1:
            self.stack.append(x)
            self.current_size += 1

    def pop(self) -> int:
        if self.current_size >= 0:
            value = self.stack.pop()
            self.current_size -= 1
            return value
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(0, k):
            if i <= self.current_size and i < self.maxSize:
                self.stack[i] += val


stk = CustomStack(3)

while True:
    choice = int(input("1. Push, 2. Pop, 3. Increment\n> "))

    match choice:
        case 1:
            x = int(input("Enter value: "))
            stk.push(x)
            print(stk.stack)
        case 2:
            x = stk.pop()
            print(stk.stack, x)
        case 3:
            x = int(input("Enter a: "))
            y = int(input("Enter b: "))
            stk.increment(x, y)
            print(stk.stack)
