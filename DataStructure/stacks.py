class ArrayStack:
    """
    고정된 크기의 배열로 구현한 스택 자료구조
    """
    def __init__(self, capacity=100):
        """
        ArrayStack을 초기화.

        Parameters
        ----------
        capacity: int, optional
            스택의 최대 용량. 기본값은 100.

        Time Complexity
        ---------------
        O(capacity)
            지정된 크기만큼 배열을 초기화
        """
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.top = -1

    def __len__(self):
        """
        스택의 현재 크기를 출력
        
        Time Complexity
        ---------------
        O(1)
        """
        return self.top + 1

    def __str__(self):
        """
        스택을 출력
        """
        return str(self.array[:self.top + 1]) + "<- top"
    
    def is_empty(self):
        """
        스택이 비어 있는지 검사.

        Returns
        -------
        bool 
            - True: 스택이 비어 있음
            - False: 스택이 비어 있지 않음

        Time Complexity
        ---------------
        O(1)
        """
        return self.top == -1

    def is_full(self):
        """
        스택이 가득 차 있는지 검사.

        Returns
        -------
        bool 
            - True: 스택이 포화 상태
            - False: 스택이 포화 상태가 아님

        Time Complexity
        ---------------
        O(1)
        """
        return self.top + 1 == self.capacity

    def push(self, e):
        """
        스택의 Top에 원소를 삽입.

        Parameters
        ----------
        e: object
            삽입할 원소

        Raises
        ------
        OverflowError
            스택이 포화 상태여서 원소를 추가할 수 없는 경우

        Time Complexity
        ---------------
        O(1)
            포화 상태 검사 후 바로 삽입
        """
        if self.is_full():
            raise OverflowError("스택 용량 포화")

        self.top += 1
        self.array[self.top] = e

    def pop(self):
        """
        스택 Top의 원소를 삭제하고 반환.

        Returns
        -------
        object 
            삭제된 Top의 원소

        Raises
        ------
        IndexError
            리스트가 비어있는 경우 

        Time Complexity
        ---------------
        O(1)
        """
        if self.is_empty():
            raise IndexError("스택이 비어있습니다.")

        item = self.array[self.top]
        self.array[self.top] = None
        self.top -= 1
        return item

    def peek(self):
        """
        스택 Top의 원소를 삭제하지 않고 반환.

        Returns
        -------
        object 
            현재 Top의 원소

        Raises
        ------
        IndexError
            리스트가 비어있는 경우 

        Time Complexity
        ---------------
        O(1)
        """
        if self.is_empty():
            raise IndexError("스택이 비어있습니다.")

        return self.array[self.top]
