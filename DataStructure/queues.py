class CircularQueue:
    """
    배열로 구현한 원형 큐.

    rear 위치에 원소를 삽입가능하고, front위치의 원소를 추출 가능.
    """
    def __init__(self, capacity=100):
        """
        CircularQueue를 초기화
        
        Parameters
        ----------
        capacity: int, optional
            원형 큐의 최대 용량. 기본값은 100.

        Time Complexity
        ---------------
        O(capacity)
            지정된 크기만큼 배열을 초기화.
        """
        self.capacity = capacity
        self.front = 0 
        self.rear = 0
        self.array = [None] * self.capacity
        self.size = 0

    def __len__(self):
        """
        큐의 현재 길이를 반환.
        """
        return self.size 

    def __str__(self):
        """
        큐의 현재 상태를 문자열로 반환.
        """
        if self.is_empty():
            return str(list())

        if self.rear > self.front:
            return "<-" + str(self.array[self.front:self.rear]) + "<-"
        elif self.front >= self.rear:
            arr = self.array[self.front:]
            arr.extend(self.array[:self.rear])
            return "<-" + str(arr) + "<-"

    def _calc_index(self, idx):
        """
        원형 큐의 순환 인덱스 계산을 위한 내부 메서드
        """
        return idx % self.capacity

    def is_empty(self):
        """ 
        큐가 비어있는지 검사.
        Returns
        -------
        bool
            - True: 큐가 비어 있음
            - False: 큐가 비어 있지 않음

        Time Complexity
        ---------------
        O(1)

        """
        return self.size == 0

    def is_full(self):
        """
        큐가 포화 상태인지 검사.

        Returns
        -------
        bool
            - True: 큐가 포화 상태
            - False: 큐가 포화 상태가 아님

        Time Complexity
        ---------------
        O(1)
        """
        return self.size == self.capacity

    def enqueue(self, item):
        """
        큐의 rear위치에 원소 삽입.

        Parameters
        ----------
        item: object
            삽입할 원소

        Raises
        ------
        OverflowError
            큐가 포화 상태로 원소를 추가할 수 없음
        
        Time Complexity
        ---------------
        O(1)
        """
        if self.is_full():
            raise OverflowError("큐 포화 상태.")

        self.array[self.rear] = item
        self.rear = self._calc_index(self.rear + 1)
        self.size += 1
        
    def dequeue(self):
        """
        큐의 front위치에 존재하는 원소를 삭제하고 반환

        Returns
        -------
        object
            반환할 원소

        Time Complexity
        ---------------
        O(1)
        """
        if self.is_empty():
            raise IndexError("큐가 비어있습니다.")

        item = self.array[self.front]
        self.array[self.front] = None
        self.front = self._calc_index(self.front + 1)
        self.size -= 1
        return item

    def peek(self):
        """
        큐의 front위치에 존재하는 원소를 삭제하지 않고 반환

        Returns
        -------
        object
            반환할 원소

        Time Complexity
        ---------------
        O(1)
        """
        if self.is_empty():
            raise IndexError("큐가 비어있습니다.")

        return self.array[self.front]
