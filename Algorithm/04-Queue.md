# 04-큐(Queue)

## 큐

- 뒤에 삽입, 앞에서부터 삭제(인덱스를 기준으로 생각하기, 자료의 길이가 짧아지는 것이 아님)

- 선입선출(FIFO, First-In First-Out)

- front, rear를 사용(시작점, 마지막점)

- enQueue(넣기), deQueue(빼기)

  ```python
  class Queue:
      def __init__(self, *args):
          self.items = list(args)
  
      def peek(self):
          return self.items[0]
  
      def enqueue(self, item):
          self.items.append(item)
  
      def dequeue(self):
          if self.is_empty():
              raise ValueError('큐가 비었다!')
          else:
              item = self.peek()
              self.items.pop(0)
              return item
  
      def is_empty(self):
          return not self.items
  
      def __str__(self):
          return f'Front -> {self.items} <- Rear'
  ```

  



## 원형 큐의 구조

- front와 rear 의 위치가 배열의 마지막 인덱스인 n-1을 가리킨 후, 논리적 순환을 이루어 배열의 처음 인덱스인 0으로 인동해야 함 => %를 사용

## 우선순위 큐(Priority Queue)

- FIFO가 아닌, 우선순위 순서로 먼저 나가게 됨
- 원소의 재배치가 일어나므로 시간이나 메모리 소모가 커짐

## 버퍼(Buffer)

- 데이터를 한 지점에서 다른 지점으로 전송하는 동안 일시적으로 데이터를 보관하는 메모리의 영역

## BFS(Breadth First Search)

- 너비우선탐색

  ```python
  def BFS(G, v, n):  # G그래프, v탐색시작점, n정점의 갯수
      visited = [0] * (n+1)
      queue = []
      queue.append(v)
      visited[v] = 1
      while queue:
          t = queue.pop(0)
          visit(t)
          for i in G[t]:
              if not visited[i]:
                  queue.append(i)
                  visited[i] = visited[t] + 1
  ```

  ```python
  # 그래프 경로 그리기
  def bfs():
      visited = [False for _ in range(V+1)]
      to_visits = [S]
  
      while to_visits:
          current = to_visits.pop(0)
          if not visited[current]:
              visited[current] = True
              print(current, end=' => ')
              if current == G:
                  return visited[G]
          to_visits += graph[current]
  ```

  
