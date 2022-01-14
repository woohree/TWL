# 인트로

## #Refactoring

결과는 같은데 과정을 바꾸는 것



## 프로그래밍 언어란?

### What?

컴퓨터에게 무언가를 시킬 때 쓰는 말

### Python?

쉽다.

많이 쓴다.

#### 문법

##### 저장

dust == 60

dust에 저장된 값은 60과 같다.

***무엇을?***

숫자, 글자, 참/거짓

***어떻게?***

변수 dust = 40

리스트(변수묶음) dust = [40, 50, 80]

딕셔너리('키'를 붙인 리스트) dust = {'영등포구': 40, ~}



##### 조건

if/elif/else

```python
dust = 90
if dust > 150:
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
elif dust >= 0:
    print('좋음')
else:
    print('지구멸망ㅋ_ㅋ') #dust 값에 따라 입력값이 출력됨
```



##### 반복

while(True면 반복, False면 멈춤)

```python
dust = [10, 12, 15, 19]
n = 0
while n < 3:
    print(dust[n])
    n = n + 1 #10, 12, 15가 출력됨
```

for(정해진 범위 안에서 반복)

```python
a = 'Hello!!'

for i in range(0, 5):
    print(a) #Hello!! 가 5번 출력됨
```



#### 함수

특정한 용도로 동작하는 코드를 한 곳에 모아 놓은 것 ex)박수를 치세요(함수) = 오른손을 가운데로, 왼손을 가운데로 다시 제자리, 반복!

##### 내장함수

print(), abs(), len() 등 파이썬에 기본설정된 함수

##### 모듈(Module)

import를 활용해 불러와서 사용하는 함수

```python
import random

menus = ['치킨', '햄버거', '소꼬리찜', '고추잡채', ]

menu = random.choice(menus)

print(menu) #menus 중 하나 출력
```

```python
import random

range(1, 46)

numbers = range(1, 46)

lucky_number = random.sample(numbers, 6)

print(lucky_number) #numbers 중 6개 숫자 랜덤 출력
```



## 웹 크롤링(Crawling)

```python
# 네이버 금융에서 '코스피 값' 만을 뽑아와 출력하고 싶다.

import requests                             # pip install requests, url에 요청해주는 프로그램
from bs4 import BeautifulSoup               # pip install beautifulsoup4, 해석기

url = 'https://finance.naver.com/sise/'

# 요청을 보내고, 문서를 받는다.
response = requests.get(url)                # url에 요청한 정보를 가져온다.
doc = response.text                         # url의 소스코드

# 구조 파악(parsing)
data = BeautifulSoup(doc, 'html.parser')    # 'html.parser' 를 넣어줘야 출력과정에서 이것저것 설명충을 정리해버릴 수 있다.

# 필요한 데이터 뽑아오기
result = data.select_one('#KOSPI_now')	    # 코스피 숫자에 마우스를 대고 copy selector하면 #KOSPI_now 가 복사된다.

# 데이터 출력
print(result.text)                          # 코스피의 값을 출력한다.


# 정리

# 요청(Request) -> URL
# 응답(Response) -> 문서 1장

# url 요청을 보내고, 문서를 요청하는 프로그램 -> client
# url 요청이 오면, 문서를 주는 프로그램 -> server
```
