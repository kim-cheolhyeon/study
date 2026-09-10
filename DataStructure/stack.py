class ArrayStack:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, e):
        if self.is_full():
            raise OverflowError("스택 용량 포화")

        self.top += 1
        self.array[self.top] = e

    def pop(self):
        if self.is_empty():
            raise IndexError("스택이 텅텅")

        item = self.array[self.top]
        self.array[self.top] = None
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("스택이 텅텅")

        return self.array[self.top]

    def __str__(self):
        return str(self.array[:self.top+1])

    def __len__(self):
        return self.top + 1
