class CircularBuffer:
    """
    배열 원형 큐와 배열 원형 덱의 공통 기능을 제공하는 부모 클래스.
    """
    def __init__(self, capacity=100):
        """
        클래스를 초기화
        
        Parameters
        ----------
        capacity: int, optional
            원형 배열의 최대 용량. 기본값은 100.

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
        원형 배열의 현재 길이를 반환.
        """
        return self.size 

    def _calc_index(self, idx):
        """
        순환 인덱스 계산을 위한 내부 메서드
        """
        return idx % self.capacity

    def is_empty(self):
        """ 
        원형 배열이 비어있는지 검사.
        Returns
        -------
        bool
            - True: 배열이 비어 있음
            - False: 배열이 비어 있지 않음

        Time Complexity
        ---------------
        O(1)

        """
        return self.size == 0

    def is_full(self):
        """
        원형 배열이 포화 상태인지 검사.

        Returns
        -------
        bool
            - True: 배열이 포화 상태
            - False: 배열이 포화 상태가 아님

        Time Complexity
        ---------------
        O(1)
        """
        return self.size == self.capacity


class CircularQueue(CircularBuffer):
    """
    배열로 구현한 원형 큐.

    Attributes
    ----------
    front : int
        현재 가장 앞쪽 원소가 저장된 인덱스.
    rear : int
        다음 원소가 삽입될 인덱스.
        마지막 원소의 인덱스가 아님.
    size : int
        현재 저장된 원소의 개수.

    Notes
    -----
    - enqueue: rear 위치에 원소를 삽입한 후 rear를 한 칸 이동.
    - dequeue: front 위치의 원소를 삭제한 후 front를 한 칸 이동.
    - front와 rear의 이동은 배열의 끝에 도달하면 처음으로 순환함.
    """

    def __str__(self):
        """
        큐의 현재 상태를 문자열로 반환.
        """
        if self.is_empty():
            return str(list())

        if self.rear > self.front:
            return "<-" + str(self.array[self.front:self.rear]) + "<-"
        else :
            arr = self.array[self.front:]
            arr.extend(self.array[:self.rear])
            return "<-" + str(arr) + "<-"

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


class CircularDeque(CircularBuffer):
    """
    배열로 구현한 원형 덱.

    Attributes
    ----------
    front : int
        현재 가장 앞쪽 원소가 저장된 인덱스.
    rear : int
        다음 원소가 뒤쪽에 삽입될 인덱스.
        마지막 원소의 인덱스가 아님.
    size : int
        현재 저장된 원소의 개수.

    Notes
    -----
    - add_front: front를 한 칸 이동한 후 해당 위치에 원소를 삽입.
    - add_rear: rear 위치에 원소를 삽입한 후 rear를 한 칸 이동.
    - delete_front: front 위치의 원소를 삭제한 후 front를 한 칸 이동.
    - delete_rear: rear를 한 칸 이동한 후 해당 위치의 원소를 삭제.
    - front와 rear의 이동은 배열의 양 끝을 기준으로 순환함.
    """
    def __str__(self):
        """
        덱의 현재 상태를 문자열로 반환.
        """
        if self.is_empty():
            return str(list())

        if self.rear > self.front:
            return "front" + str(self.array[self.front:self.rear]) + "rear"
        else :
            arr = self.array[self.front:]
            arr.extend(self.array[:self.rear])
            return "front" + str(arr) + "rear"


    def add_front(self, item):
        """
        덱의 front위치에 원소 삽입.

        Parameters
        ----------
        item: object
            삽입할 원소

        Raises
        ------
        OverflowError
            덱이 포화 상태로 원소를 추가할 수 없음
        
        Time Complexity
        ---------------
        O(1)
        """
        if self.is_full():
            raise OverflowError("덱 포화 상태.")
        self.front = self._calc_index(self.front - 1)
        self.array[self.front] = item
        self.size += 1
    
    def add_rear(self, item):
        """
        덱의 rear위치에 원소 삽입.

        Parameters
        ----------
        item: object
            삽입할 원소

        Raises
        ------
        OverflowError
            덱이 포화 상태로 원소를 추가할 수 없음
        
        Time Complexity
        ---------------
        O(1)
        """
        if self.is_full():
            raise OverflowError("덱 포화 상태.")

        self.array[self.rear] = item
        self.rear = self._calc_index(self.rear + 1)
        self.size += 1

    def delete_front(self):
        """
        덱의 front위치에 존재하는 원소를 삭제하고 반환

        Returns
        -------
        object
            반환할 원소

        Time Complexity
        ---------------
        O(1)
        """
        if self.is_empty():
            raise IndexError("덱이 비어있습니다.")

        item = self.array[self.front]
        self.array[self.front] = None
        self.front = self._calc_index(self.front + 1)
        self.size -= 1
        return item

    def get_front(self):
        """
        덱의 front위치에 존재하는 원소를 삭제하지 않고 반환

        Returns
        -------
        object
            반환할 원소

        Time Complexity
        ---------------
        O(1)
        """
        if self.is_empty():
            raise IndexError("덱이 비어있습니다.")

        return self.array[self.front]

    def delete_rear(self):
        """
        덱의 raer위치에 존재하는 원소를 삭제하고 반환

        Returns
        -------
        object
            반환할 원소

        Time Complexity
        ---------------
        O(1)
        """
        if self.is_empty():
            raise IndexError("덱이 비어있습니다.")

        self.rear = self._calc_index(self.rear - 1)
        item = self.array[self.rear]
        self.array[self.rear] = None
        self.size -= 1
        return item
    
    def get_rear(self):
        """
        덱의 raer위치에 존재하는 원소를 삭제하지 않고 반환

        Returns
        -------
        object
            반환할 원소

        Time Complexity
        ---------------
        O(1)
        """
        if self.is_empty():
            raise IndexError("덱이 비어있습니다.")

        item = self.array[self._calc_index(self.rear - 1)]
        return item