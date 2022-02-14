# Array 2

## 2차원 배열

- 1차원  list를 묶은 list

- 행, 열이 존재

- ```python
  N = int(input())
  arr = [list(map(int, input()))) for _ in range(N)]
  ```

- 행 우선, 열 우선 순회

- 지그재그 순회

  - 행을 홀짝으로 조건을 주고, 홀 - 열 정순서, 짝 - 열 역순서로 출력

- 문제에서 1,1부터 시작하는 경우

  ```python
  arr = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
  ```

  

### 2차원 배열 탐색

- 델타를 이용

  ```python
  # N x N 배열
  di = [0, 1, 0, -1]  # 우하좌상
  dj = [1, 0, -1, 0]
  for k in range(4):
      ni = i + di[k]
      nj = j + dj[k]
      if 0 <= ni < N and 0 <= nj < N:
          arr[ni][nj]
  
  # 파이썬 특성 이용
  arr = [[1,2,3], [4,5,6], [7,8,9]]
  N = 3
  for i in range(N):
      for j in range(N):
          for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
              ni = i + di
              nj = j + dj
              if 0 <= ni < N and 0 <= nj < N:
                  print(i, j, arr[ni][nj])
          print()
  ```



## 부분집합 합(Subset Sum) 문제

- 부분집합 생성하기

  ```python
  a = [1, 2, 3, 4]
  bit = [0, 0, 0, 0]
  for i in range(2):
      bit[0] = i
      for j in range(2):
          bit[1] = j
          for k in range(2):
              bit[2] = k
              for l in range(2):
                  bit[3] = l
                  for p in range(4):
                      if bit[p] == 1:
                          print(a[p], end = '')
                  print()
  ```

  ```python
  a = 1 >> 4  # 16
  ```

  - 비트 연산자
    - \& 비트 단위로 AND 연산
    - \| 비트 단위로 OR 연산
    - \<< 피연산자의 비트 열을 왼쪽으로 이동
    - \>> 피연산자의 비트 열을 오른쪽으로 이동

  ```python
  arr = [3, 6, 7, 1, 5, 4]
  n = len(arr)
  for i in range(1<<n):  # 1<<n 부분 집합의 갯수 (0~32 2진수 묶음)
      for j in range(n):  # 원소의 수만큼 비트를 비교함
          if i & (1<<j):  # i의 j번 비트가 1인 경우
              print(arr[j], end='')  # j번 원소 출력
      print()
  ```

  

## 검색(Search)

- 저장된 자료 중 원하는 항목을 찾는 작업

  - 순차 검색(sequential)

    ```python
    # 정렬 안된 경우
    def sequentialSearch(a, key):
        i = 0
        while i < len(a) and a[i] != key:
            i += 1
        if i < len(a):
            return i
        else:
            return -1
    ```

    ```python
    # 정렬된 경우
    def sequentialSearch(a, key):
        i = 0
        while i < len(a) and a[i] < key:
            i += 1
        if i < len(a) and a[i] == key:
            return i
        else:
            return -1
    ```

  - 이진 검색(binary) - 정렬된 자료만 가능

    ```python
    def binarySearch(a, key):
        start = 0
        end = len(a) - 1
        while start <= end:
            middle = (start+end) // 2
            if a[middle] == key:
                return True
            elif a[middle] > key:
                end = middle - 1
            else:
                start = middle + 1
        return False
    ```



## 인덱스

### 선택 정렬 (버블 정렬 반대?)

- 주어진 자료에서 가장 작은 값의 원소부터 차례대로 선택해 위치를 교환하는 방식

  ```python
  def selectionSort(a):
      for i in range(len(a)-1):
          minidx = i
          for j in range(i+1, len(a)):
              if a[minidx] > a[j]:
                  minidx = j
          a[i], a[minidx] = a[minidx], a[i]
  ```

- k번째로 작은 원소를 찾기

  ```python
  def selectionSort(a, k):
      for i in range(k):
          minidx = i
          for j in range(i+1, len(a)):
              if a[minidx] > a[j]:
                  minidx = j
          a[i], a[minidx] = a[minidx], a[i]
      return a[k-1]
  ```

  

