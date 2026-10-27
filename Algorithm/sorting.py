def selection_sort(arr: list[int]):
    """
    선택 정렬(Selection Sort) 알고리즘 구현.

    Parameters
    ----------
    arr : list[int]
        정렬할 정수 리스트. 오름차순으로 정렬하며 원본을 수정함.

    Time Complexity
    ---------------
    Average: O(n^2)
    Best: O(n^2)
        - 비교 횟수: n(n-1)/2
        - 교환 횟수: 0
    Worst: O(n^2)
        - 비교 횟수: n(n-1)/2
        - 교환 횟수: n-1

    Space Complexity
    ----------------
    O(1)
        - 입력 크기와 관계없이 일정한 추가 공간 사용.

    Properties
    ----------
    - In-place: Yes (제자리 정렬)
    - Stable: No (Unstable)
    - Comparison-based: Yes (비교 기반 정렬)
    """
    n = len(arr)
    for i in range(n-1):
        min_idx = i 

        for j in range(i+1, n):

            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[min_idx], arr[i] = arr[i], arr[min_idx]


def insertion_sort(arr: list[int]):
    """
    삽입 정렬(Insertion Sort) 알고리즘 구현.

    Parameters
    ----------
    arr : list[int]
        정렬할 정수 리스트. 오름차순으로 정렬하며 원본을 수정함.

    Time Complexity
    ---------------
    Average: O(n^2)
    Best: O(n)
        - 비교 횟수: (n-1)
        - 교환 횟수: 0
    Worst: O(n^2)
        - 비교 횟수: n(n-1)/2
        - 교환 횟수: n(n-1)/2

    Space Complexity
    ----------------
    O(1)
        - 입력 크기와 관계없이 일정한 추가 공간 사용.

    Properties
    ----------
    - In-place: Yes (제자리 정렬)
    - Stable
    - Comparison-based: Yes (비교 기반 정렬)
    """
    n = len(arr)

    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break


def bubble_sort(arr:list[int]):
    """
    버블 정렬(Bubble Sort) 알고리즘 구현.

    Parameters
    ----------
    arr : list[int]
        정렬할 정수 리스트. 오름차순으로 정렬하며 원본을 수정함.

    Time Complexity
    ---------------
    Average: O(n^2)
    Best: O(n^2)
        - 비교 횟수: n(n-1)/2
        - 교환 횟수: 0
    Worst: O(n^2)
        - 비교 횟수: n(n-1)/2
        - 교환 횟수: n(n-1)/2

    Space Complexity
    ----------------
    O(1)
        - 입력 크기와 관계없이 일정한 추가 공간 사용.

    Properties
    ----------
    - In-place: Yes (제자리 정렬)
    - Stable: yes
    - Comparison-based: Yes (비교 기반 정렬)
    """
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
def merge_sort(arr: list[int]) -> list[int]:
    """
    병합 정렬(Merge Sort) 알고리즘 구현.

    Parameters
    ----------
    arr : list[int]
        정렬할 정수 리스트. 오름차순으로 정렬하며 원본을 수정하지 않음.

    Time Complexity
    ---------------
    Average: O(n log n)
    Best: O(n log n)
        - 비교 횟수: O(n log n)
        - 교환 횟수: 0
    Worst: O(n log n)
        - 비교 횟수: O(n log n)
        - 교환 횟수: 0
    - 배열을 절반씩 분할하여 재귀적으로 정렬함.
    - 분할 깊이: O(log n)
    - 각 단계의 병합 비용: O(n)

    Space Complexity
    ----------------
    O(n)
        - 슬라이싱과 병합 과정에서 새로운 리스트를 생성함.
        - 재귀 호출 스택: O(log n)
        - 전체 최대 보조 공간: O(n)

    Properties
    ----------
    - In-place: No (별도의 리스트를 사용하는 정렬)
    - Stable: Yes (안정 정렬)
    - Comparison-based: Yes (비교 기반 정렬)
    - Divide and Conquer: Yes (분할 정복)

    Returns
    -------
    list[int]
        오름차순으로 정렬된 리스트.
    """
    n = len(arr)

    if n <= 1:
        return arr

    m = n//2
    L = merge_sort(arr[:m])
    R = merge_sort(arr[m:])

    i = 0
    j = 0

    result = []

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            result.append(L[i])
            i += 1
        else:
            result.append(R[j])
            j += 1

    if i == len(L):
        return result + R[j:]
    
    else:
        return result + L[i:]
    

def quick_sort(arr: list[int]) -> list[int]:
    """
    퀵 정렬(Quick Sort) 알고리즘 구현.

    Parameters
    ----------
    arr : list[int]
        정렬할 정수 리스트. 오름차순으로 정렬하며 원본을 수정하지 않음.

    Time Complexity
    ---------------
    Average: O(n log n)
        - 비교 횟수: O(n log n)
        - 피벗을 기준으로 평균적으로 균형 있게 분할되는 경우.
    Best: O(n)
        - 비교 횟수: O(n)
        - 모든 원소가 동일하여 재귀 분할이 발생하지 않는 경우.
        - 서로 다른 원소들이 균형 있게 분할되는 경우: O(n log n)
    Worst: O(n^2)
        - 비교 횟수: O(n^2)
        - 피벗이 계속 최솟값 또는 최댓값으로 선택되는 경우.
        - 이미 정렬된 배열이나 역순 배열 등에서 발생 가능.

    Space Complexity
    ----------------
    O(n)
        - S, M, L 리스트를 생성하여 원소를 분할함.
        - 재귀 호출 스택을 포함한 최대 보조 공간은 O(n).
        - 최악의 경우 누적 할당량은 O(n^2).

    Properties
    ----------
    - In-place: No (별도의 리스트를 사용하는 정렬)
    - Stable: Yes (안정 정렬)
    - Comparison-based: Yes (비교 기반 정렬)
    - Partition: 3-way partition (S, M, L)

    Returns
    -------
    list[int]
        오름차순으로 정렬된 새로운 리스트.
    """
    n = len(arr)
    if n <= 1:
        return arr
    pivot = arr[0]
    S = []
    M = []
    L = []

    for i in range(n):
        item = arr[i]
        if item < pivot:
            S.append(item)
        elif item > pivot:
            L.append(item)
        else:
            M.append(item)
            
    S = quick_sort(S)
    L = quick_sort(L)

    return S + M + L