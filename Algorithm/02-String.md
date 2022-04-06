# 02-문자열(String)

## 패턴 매칭

- 고지식한 알고리즘(Brute Force)

  ```python
  t = 'this is a book'
  p = 'is'
  N = len(t)
  M = len(p)
  
  def BruteForce(p, t):
      i = 0  # t의 인덱스
      j = 0  # p의 인덱스
      while j < M and i < N:
          if t[i] != p[j]:
              i = i - j  # 가장 처음 같았던 지점의 다음 지점
              j = -1
          i += 1
          j += 1
      if j == M:
          return i - M  # 찾는 패턴의 시작 위치
      else:
          return -1  # 검색 실패
  ```

  

- KMP 알고리즘

  - 반복되는 패턴을 검사할 시, 겹치는 문자열 다시 검사안하도록 조작

  뭔소린지 잘 모르겠음ㅋㅋ

- 보이어-무어 알고리즘

  - 오른쪽에서 왼쪽으로 비교
  - 알고리즘에 사용하려면 호스풀(horspool)이 비교적 간단한 버전이므로 찾아보고 사용할 것

  이거도 뭔소린지 잘 모름ㅋㅋ
