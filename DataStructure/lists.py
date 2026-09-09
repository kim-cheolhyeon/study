class ArrayList():
    def __init__(self, capacity=100):
        self.size = 0
        self.capacity = capacity
        self.array = [None] * self.capacity

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def insert(self, pos, e):
        if self.is_full():
            raise MemoryError("리스트 포화")
        
        if not (0 <= pos <= self.size):
            raise IndexError("범위를 벗어난 인덱스")

        for i in range(self.size -1, pos - 1, -1):
            self.array[i+1] = self.array[i]

        self.array[pos] = e
        self.size += 1

    def delete(self, pos):
        if self.is_empty():
            raise IndexError("빈 리스트는 삭제 불가능")

        if not (0 <= pos < self.size):
            raise IndexError("범위를 벗어난 인덱스")

        item = self.array[pos]
        for i in range(pos + 1, self.size):
            self.array[i-1] = self.array[i] 

        self.size -= 1
        self.array[self.size] = None
        return item

    def get_entry(self, pos):
        if not (0 <= pos < self.size):
            raise IndexError("범위를 벗어난 인덱스")
        return self.array[pos] 
