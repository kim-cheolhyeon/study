# 선택 정렬
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
    - Untable
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
            
def merge_sort(arr: list[int]) -> None:
    pass



# 퀵 정렬
class QuickSort:
    pass

# 기수 정렬
class RadixSort:
    pass

# 계수 정렬
class CountSort:
    pass

# 힙 정렬
class HeapSort:
    pass

