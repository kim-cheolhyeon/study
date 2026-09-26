class ArraySet:
    """
    고정된 크기의 배열로 구현한 집합 자료구조.

    원소의 중복을 허용하지 않으며, 현재 구현에서는 원소의 순서를
    정렬하지 않고 삽입된 상태로 저장한다.

    원소를 항상 정렬된 상태로 유지하면 탐색 성능을 개선할 수 있지만,
    현재 구현에서는 이를 고려하지 않는다.

    Notes
    -----
    - 내부 배열의 크기가 고정되어 있으므로 capacity를 초과하여
      원소를 저장할 수 없다.
    - 합집합, 교집합, 차집합을 생성할 때 결과 집합의 기본 용량을
      100으로 생성하기 때문에 결과 원소가 100개를 초과하면
      OverflowError가 발생할 수 있다.
    - 현재 원소 탐색은 선형 탐색을 사용한다.
    - 합집합에서 insert()연산을 사용하는 경우 매번 중복 검사를 시행함 -> copy()매서드를 만들어 시간 단축 가능
    """

    def __init__(self, capacity=100):
        """
        ArraySet을 초기화.

        Parameters
        ----------
        capacity : int, optional
            집합의 최대 용량. 기본값은 100.

        Time Complexity
        ---------------
        O(capacity)
            지정된 크기의 내부 배열을 생성하고 초기화.
        """
        self.size = 0
        self.capacity = capacity
        self.array = [None] * capacity

    def is_empty(self):
        """
        집합이 비어 있는지 검사.

        Returns
        -------
        bool
            - True: 집합이 비어 있음
            - False: 집합이 비어 있지 않음

        Time Complexity
        ---------------
        O(1)
        """
        return self.size == 0

    def is_full(self):
        """
        집합이 가득 차 있는지 검사.

        Returns
        -------
        bool
            - True: 집합이 포화 상태
            - False: 집합이 포화 상태가 아님

        Time Complexity
        ---------------
        O(1)
        """
        return self.size == self.capacity

    def find_index(self, e):
        """
        집합에서 특정 원소의 인덱스를 탐색.

        Parameters
        ----------
        e : object
            탐색할 원소.

        Returns
        -------
        int or None
            원소가 존재하면 해당 원소의 인덱스를 반환하고,
            존재하지 않으면 None을 반환.

        Time Complexity
        ---------------
        Best: O(1)
            첫 번째 위치에서 원소를 찾은 경우.
        Worst: O(n)
            마지막 위치에서 찾거나 원소가 존재하지 않는 경우.
        """
        for i in range(0, self.size):
            if self.array[i] == e:
                return i

        return None

    def is_contain(self, e):
        """
        특정 원소가 집합에 포함되어 있는지 검사.

        Parameters
        ----------
        e : object
            포함 여부를 검사할 원소.

        Returns
        -------
        bool
            - True: 원소가 집합에 존재함
            - False: 원소가 집합에 존재하지 않음

        Time Complexity
        ---------------
        Best: O(1)  
        Worst: O(n)  
            내부적으로 find_index()를 사용하여 선형 탐색.
        """
        return self.find_index(e) is not None

    def insert(self, e):
        """
        집합에 새로운 원소를 삽입.

        이미 존재하는 원소인 경우에는 중복 삽입하지 않는다.

        Parameters
        ----------
        e : object
            삽입할 원소.

        Raises
        ------
        OverflowError
            집합이 포화 상태여서 새로운 원소를 삽입할 수 없는 경우.

        Time Complexity
        ---------------
        Best: O(1)
            검사할 원소를 첫 번째 위치에서 발견한 경우.
        Worst: O(n)
            중복 여부를 확인하기 위해 전체 집합을 탐색하는 경우.
        """
        if self.is_full():
            raise OverflowError("용량 포화")

        if self.is_contain(e):
            return

        self.array[self.size] = e
        self.size += 1

    def delete(self, e):
        """
        집합에서 특정 원소를 삭제하고 삭제된 원소를 반환.

        삭제할 원소의 위치에 마지막 원소를 이동시켜 빈 공간을 채운다.
        따라서 삭제 후 원소의 기존 순서는 유지되지 않는다.

        Parameters
        ----------
        e : object
            삭제할 원소.

        Returns
        -------
        object
            삭제된 원소.

        Raises
        ------
        KeyError
            삭제하려는 원소가 집합에 존재하지 않는 경우.

        Time Complexity
        ---------------
        Best: O(1)
            첫 번째 위치에서 삭제할 원소를 찾은 경우.
        Worst: O(n)
            원소를 찾기 위해 전체 집합을 탐색하는 경우.

        Notes
        -----
        원소를 찾은 이후 실제 삭제 연산 자체는 O(1)이다.
        마지막 원소를 삭제 위치로 이동시키기 때문에
        배열의 원소들을 한 칸씩 이동할 필요가 없다.
        """
        idx = self.find_index(e)

        if idx is None:
            raise KeyError("존재하지 않는 원소")

        item = self.array[idx]
        self.array[idx], self.array[self.size - 1] = self.array[self.size - 1], None
        self.size -= 1

        return item

    def union(self, setB: "ArraySet"):
        """
        현재 집합과 다른 집합의 합집합을 생성.

        두 집합 중 하나 이상에 포함된 모든 원소를 포함하는
        새로운 ArraySet 객체를 반환한다.

        Parameters
        ----------
        setB : ArraySet
            합집합 연산을 수행할 다른 집합.

        Returns
        -------
        ArraySet
            현재 집합과 setB의 합집합.

        Raises
        ------
        OverflowError
            결과 집합의 용량을 초과하는 경우.

        Time Complexity
        ---------------
        O((n + m)^2)

            n은 현재 집합의 원소 수,
            m은 setB의 원소 수.

            각 원소를 insert()할 때마다 중복 검사를 위해
            선형 탐색을 수행하므로 최악의 경우 제곱 시간복잡도를 가짐.

        Notes
        -----
        결과 집합을 기본 용량 100으로 생성하기 때문에 합집합의 크기가
        100을 초과하면 OverflowError가 발생할 수 있다.
        """
        union = ArraySet()

        for idx in range(self.size):
            union.insert(self.array[idx])

        for idx in range(setB.size):
            union.insert(setB.array[idx])

        return union

    def intersect(self, setB):
        """
        현재 집합과 다른 집합의 교집합을 생성.

        두 집합에 모두 포함된 원소만 저장한 새로운 ArraySet 객체를 반환.

        Parameters
        ----------
        setB : ArraySet
            교집합 연산을 수행할 다른 집합.

        Returns
        -------
        ArraySet
            현재 집합과 setB의 교집합.

        Raises
        ------
        OverflowError
            결과 집합의 용량을 초과하는 경우.

        Time Complexity
        ---------------
        O(nm + n^2)

            n은 현재 집합의 원소 수,
            m은 setB의 원소 수.

            현재 집합의 각 원소마다 setB에서 선형 탐색을 수행하고,
            교집합에 원소를 삽입할 때도 중복 검사를 수행함.

        Notes
        -----
        n과 m의 크기가 비슷하다고 가정하면 일반적으로
        O(n^2) 수준의 시간복잡도로 볼 수 있다.
        """
        inter = ArraySet()

        for idx in range(self.size):
            item = self.array[idx]

            if setB.is_contain(item):
                inter.insert(item)

        return inter

    def difference(self, setB: "ArraySet"):
        """
        현재 집합과 다른 집합의 차집합을 생성.

        현재 집합에는 존재하지만 setB에는 존재하지 않는 원소만
        저장한 새로운 ArraySet 객체를 반환한다.

        Parameters
        ----------
        setB : ArraySet
            차집합 연산에서 제외할 원소를 가진 집합.

        Returns
        -------
        ArraySet
            현재 집합에서 setB의 원소를 제외한 차집합.

        Raises
        ------
        OverflowError
            결과 집합의 용량을 초과하는 경우.

        Time Complexity
        ---------------
        O(nm + n^2)

            n은 현재 집합의 원소 수,
            m은 setB의 원소 수.

            현재 집합의 각 원소마다 setB에서 선형 탐색을 수행하고,
            결과 집합에 삽입할 때도 중복 검사를 수행함.

        Notes
        -----
        n과 m의 크기가 비슷하다고 가정하면 일반적으로
        O(n^2) 수준의 시간복잡도로 볼 수 있다.
        """
        diff = ArraySet()

        for idx in range(self.size):
            item = self.array[idx]

            if not setB.is_contain(item):
                diff.insert(item)

        return diff
