class ArrayList:
    """
    고정된 크기의 배열로 구현한 리스트 자료구조
    """
    
    def __init__(self, capacity=100):
        """
        ArrayList를 초기화.

        Parameters
        ----------
        capacity : int, optional
            리스트의 최대 용량. 기본값은 100.

        Time Complexity
        ---------------
        O(capacity)
            지정된 크기만큼 배열을 초기화.
        """
        self.size = 0
        self.capacity = capacity
        self.array = [None] * self.capacity

    def is_empty(self):
        """
        리스트가 비어 있는지 검사.

        Returns
        -------
        bool
            - True: 리스트가 비어 있음
            - False: 리스트가 비어 있지 않음

        Time Complexity
        ---------------
        O(1)
        """
        return self.size == 0

    def is_full(self):
        """
        리스트가 가득 차 있는지 검사.

        Returns
        -------
        bool
            - True: 리스트가 포화 상태
            - False: 리스트가 포화 상태가 아님

        Time Complexity
        ---------------
        O(1)
        """
        return self.size == self.capacity

    def insert(self, pos, e):
        """
        리스트의 특정 위치에 원소를 삽입.

        Parameters
        ----------
        pos : int
            원소를 삽입할 위치
        e : object
            삽입할 원소

        Raises
        ------
        OverflowError
            리스트가 포화 상태여서 원소를 추가할 수 없는 경우
        IndexError
            삽입 위치가 유효한 범위를 벗어난 경우

        Time Complexity
        ---------------
        Best: O(1)
            리스트의 마지막 위치에 삽입하는 경우
        Worst: O(n)
            리스트의 첫 번째 위치에 삽입하여 모든 원소를 이동하는 경우
        """
        if self.is_full():
            raise OverflowError("리스트 포화")
        
        if not (0 <= pos <= self.size):
            raise IndexError("범위를 벗어난 인덱스")

        for i in range(self.size - 1, pos - 1, -1):
            self.array[i + 1] = self.array[i]

        self.array[pos] = e
        self.size += 1

    def delete(self, pos):
        """
        리스트의 특정 위치에 있는 원소를 삭제하고 반환.

        Parameters
        ----------
        pos : int
            삭제할 원소의 위치

        Returns
        -------
        object
            삭제된 원소

        Raises
        ------
        IndexError
            리스트가 비어 있거나 삭제 위치가 유효한 범위를 벗어난 경우

        Time Complexity
        ---------------
        Best: O(1)
            리스트의 마지막 원소를 삭제하는 경우
        Worst: O(n)
            리스트의 첫 번째 원소를 삭제하여 나머지 원소를 이동하는 경우
        """
        if self.is_empty():
            raise IndexError("빈 리스트는 삭제 불가능")

        if not (0 <= pos < self.size):
            raise IndexError("범위를 벗어난 인덱스")

        item = self.array[pos]

        for i in range(pos + 1, self.size):
            self.array[i - 1] = self.array[i]

        self.size -= 1
        self.array[self.size] = None

        return item

    def get_entry(self, pos):
        """
        리스트의 특정 위치에 있는 원소를 반환.

        Parameters
        ----------
        pos : int
            조회할 원소의 위치

        Returns
        -------
        object
            해당 위치에 저장된 원소

        Raises
        ------
        IndexError
            조회 위치가 유효한 범위를 벗어난 경우

        Time Complexity
        ---------------
        O(1)
            배열의 인덱스를 통해 원소에 직접 접근
        """
        if not (0 <= pos < self.size):
            raise IndexError("범위를 벗어난 인덱스")

        return self.array[pos]
