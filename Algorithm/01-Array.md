# 배열(Array)

## 알고리즘

- 유한한 단계를 통해 문제를 해결하는 절차나 방법

### 시간 복잡도

- 알고리즘의 작업량을 표현
- 빅-오 표기법(Big-O Notation)

## 배열

- 일정한 자료형의 변수들을 하나의 이름으로 열거해 사용하는 구조

### 1차원 배열

- `arr = list()	arr = [0] * 10	  arr = [1, 2, 3]`
- `arr[idx] = 20;` 배열 arr의 idx 원소에 20을 저장하라

## 정렬

- 특정 기준에 의해 오름차순, 혹은 내림차순으로 재배열하는 것
- 키: 자료를 정렬하는 기준 값

### 버블 정렬(Bubble sort)

- 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식
  - 첫 원소부터 인접한 원소끼리 계속 자리를 교환하면서 마지막 자리까지 이동
  - 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬
  - 교환하며 자리를 이동하는 모습이 물 위로 올라오는 거품같다...?
  
- O(n^2)

  ```python
  def BubbleSort(A, n):
      for i in range(n-1, 0, -1):
          for j in range(i):
              if A[j] > A[j+1]:
                  A[j], A[j+1] = A[j+1], A[j]
      return A
  ```

  

### 카운팅 정렬(Counting sort)

- 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘

- O(n+k): n은 리스트 길이, k는 정수의 최댓값

  ```python
  def CountingSort(A, B, k):
      C = [0] * (k+1)
      
      for i in range(len(A)):
          C[A[i]] += 1
          
      for i in range(1, len(C)):
          C[i] += C[i-1]
          
      for i in range(len(B)-1, -1, -1):
          C[A[i]] -= 1
          B[C[A[i]]] = A[i]
  ```

  

## Baby-gin game

```python
# 1, 2, 3 을 포함하는 모든 순열을 생성하는 함수
for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i2 != i1:
            for i3 in range(1, 4):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)
```

![](01-Array.assets/화면 캡처 2022-02-09 150020.png)

```python
# num의 숫자별 카운트 리스트 만들기
num = 123789
c = [0] * 12  # run과 triplete을 같은 인덱스로 검사하기 위해 2칸을 더 늘림

while num > 0:
    c[num % 10] += 1
    num //= 10
    
# 풀이
i = 0
tri = 0
run = 0

while i < 10:
    if c[i] >= 3:  # tri 조사
        c[i] -= 3
        tri += 1
        continue
    if c[i] >=1 and c[i+1] >=1 and c[i+2] >=1:  # run 조사
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1
    
if run + tri == 2: print('베이비진!')
else: print('ㄴㄴ!')
```



## 2차원 배열

- 1차원  list를 묶은 list

- 행, 열이 존재

- ```python
  N = int(input())
  arr = [list(map(int, input())) for _ in range(N)]
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
  a = 1 << 4  # 16
  ```

  - 비트 연산자
    - \& 비트 단위로 AND 연산
    - \| 비트 단위로 OR 연산
    - \<< 피연산자의 비트 열을 왼쪽으로 이동
    - \>> 피연산자의 비트 열을 오른쪽으로 이동

  ```python
  arr = [3, 6, 7, 1, 5, 4]
  n = len(arr) - 1
  for i in range(1<<n):  # 1<<n 부분 집합의 갯수 (0~63 2진수 묶음)
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

  

