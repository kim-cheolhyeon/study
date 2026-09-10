class ArraySet():
    """
    순서대로 항상정렬해 놓으면 원소 찾아야하는 상황에서 아주 유용하지만, 일단은 구현하지 않음.
    
    추가 고려 사항
    ---
    - 합집합을 만드는 경우 지금은 기본용량 100으로 만들기 때문에 용량을 초과하는 문제가 생길 수 있음

    """
    def __init__(self, capacity=100):
        self.size = 0
        self.capacity = capacity
        self.array = [None] * capacity

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def find_index(self, e):
        for i in range(0, self.size):
            if self.array[i] == e:
                return i 

        return None

    def is_contain(self, e):
        return self.find_index(e) is not None

    def insert(self, e):
        if self.is_full():
            raise OverflowError("용량 포화")

        if self.is_contain(e):
            return

        self.array[self.size] = e
        self.size += 1

    def delete(self, e):
        idx = self.find_index(e)
        if idx is None:
            raise KeyError("존재하지 않는 원소")
        item = self.array[idx]
        self.array[idx], self.array[self.size - 1] = self.array[self.size - 1], None
        self.size -= 1
        return item

    def union(self, setB:ArraySet):
        union = ArraySet()
        for idx in range(self.size):
            union.insert(self.array[idx])

        for idx in range(setB.size):
            union.insert(setB.array[idx])
        return union

    def intersect(self, setB: ArraySet):
        inter = ArraySet()
        for idx in range(self.size):
            item = self.array[idx]
            if setB.is_contain(item):
                inter.insert(item)
        return inter

    def difference(self, setB: ArraySet):
        diff = ArraySet()
        for idx in range(self.size):
            item = self.array[idx]

            if not setB.is_contain(item):
                diff.insert(item)
        return diff
