# Markdown 학습하기

## 제목(Heading)

가장 큰 제목부터 ~ 6번재로 큰 제목까지 존재

#의 갯수로 제목의 중요도를 지정


## 목록

순서가 있는 목록(Odered list)과 순서가 없는 목록(Unordered list)가 있다.

### 순서가 없는 목록
-혹은 *를 앞에 붙이고 띄어쓰기

- python
- java
- web
- djang
- vue

### 순서가 있는 목록
1을 쓰고 띄어쓰기

1. md 학습
2. git 기초 학습
3. github 학습



## 강조(Emphasis)

글자의 스타일링 지정

### 기울임

` *`로 감싼 글자들은 *기울어집니다.*

1. 굵게: `**`로 감싼 글자들은 **굵어집니다.**

2. 취소: `~~`로 감싼 글자들은 ~~취소선이 생깁니다.~~

3. 인라인 코드: 백틱(`)으로 감싼 글자들은 ``코드처럼 표시됩니다.``



## 코드블럭(Code block)

백틱 3개로 감싼 블럭은 코드 출력용입니다.

```python
def my_func():
	print("Hello world")
```



## 표(Table)

| 이름   | 전공       | 나이 |
| ------ | ---------- | ---- |
| 이우현 | 응용물리학 | 31   |
|        |            |      |
|        |            |      |



## 수식(Latex)

> 원래 마크다운은 지원하지 않으나, Typora가 추가적으로 지원하는 기능 - latex typora 구글링