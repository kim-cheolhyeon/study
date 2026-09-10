class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0 
        self.rear = 0
        self.array = [None] * self.capacity
        self.size = 0

    def __len__(self):
        return self.size 

    def __str__(self):
        pass

    def _calc_index(self, idx):
        return idx % self.capacity

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("큐 포화")

        self.array[self.rear] = item
        self.rear = self._calc_index(self.rear + 1)
        self.size += 1
        
    def dequeue(self):
        if self.is_empty():
            raise IndexError("큐 텅텅")

        item = self.array[self.front]
        self.array[self.front] = None
        self.front = self._calc_index(self.front + 1)
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("큐 텅텅")

        return self.array[self.front]
