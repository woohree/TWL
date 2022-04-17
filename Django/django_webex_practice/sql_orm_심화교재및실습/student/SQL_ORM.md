[TOC]

# SQL with django ORM

## 기본 준비 사항

* django app

  * 가상환경 세팅

  * 패키지 설치

  * migrate

    ```bash
    $ python manage.py migrate
    ```
  
* 제공 받은 `users.csv` 파일은 db.sqlite3와 같은 곳에 위치하도록 이동

* `db.sqlite3` 활용

  * `sqlite3`  실행

    ```bash
    $ sqlite3 db.sqlite3
    ```

  * 테이블 확인

    ```sqlite
    sqlite > .tables
    auth_group                  django_admin_log
    auth_group_permissions      django_content_type
    auth_permission             django_migrations
    auth_user                   django_session
    auth_user_groups            auth_user_user_permissions  
    users_user
    ```
    
  * csv 파일 data 로드 및 확인

    ```sqlite
    sqlite > .mode csv
    sqlite > .import users.csv users_user
    
    sqlite > SELECT COUNT(*) FROM users_user;
    100
    ```



---



## 문제

> ORM은 django extensions의 shell_plus에서,
>
> SQL은 수업에서 진행한 [SQLite 확장프로그램](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite) 사용 방식으로 진행

### 1. 기본 CRUD 로직

1. 모든 user 레코드 조회

   ```python
   # orm
   from users.models import User
   User.objects.all()
   ```

      ```sql
   -- sql
   SELECT * FROM users_user;
      ```

2. user 레코드 생성

   ```python
   # orm
   # case1
   User.objects.create(first_name='우현', last_name='이', country='경기', phone='010-1234-5678', blance=99999999999999999)
   # case2
   user = User()
   user.first_name = '우현'
   ...
   user.save()
   ```

   ```sql
   -- sql
   ```

   * 하나의 레코드를 빼고 작성 후 `NOT NULL` constraint 오류를 orm과 sql에서 모두 확인 해보세요.

3. 해당 user 레코드 조회

   - `102` 번 id의 전체 레코드 조회

   ```python
   # orm
   User.objects.get(id=102)
   ```

   ```sql
   -- sql
   ```

4. 해당 user 레코드 수정

   - ORM: `102` 번 글의 `last_name` 을 '김' 으로 수정
   - SQL: `102` 번 글의 `first_name` 을 '철수' 로 수정

   ```python
   # orm
   user = User.objects.get(id=102)
   user.last_name='김'
   user.first_name='철수'
   user.save()
   ```

      ```sql
   -- sql
      ```

5. 해당 user 레코드 삭제

   - ORM: `102` 번 글 삭제
   - `SQL`:  `101` 번 글 삭제 

   ```python
   # orm
   user.delete()
   ```
   
   ```sql
   -- sql
   ```



---



### 2. 조건에 따른 쿼리문

1. 전체 인원 수 

   - `User` 의 전체 인원수

   ```python
   # orm
   User.objects.count()
   ```

   ```sql
   -- sql
   ```

2. 나이가 30인 사람의 이름

   - `ORM` : `.values` 활용
     - 예시: `User.objects.filter(조건).values(컬럼이름)`

   ```python
   # orm
   User.objects.filter(age=30)
   #<QuerySet [<User: 영환>, <User: 보람>, <User: 은영>]>]
   
   User.objects.filter(age=30).values('first_name')
   # <QuerySet [{'first_name': '영환'}, {'first_name': '보람'}, {'first_name': '은영'}]>
   ```

      ```sql
   -- sql
      ```

3. 나이가 30살 이상인 사람의 인원 수

   -  ORM: `__gte` , `__lte` , `__gt`, `__lt` -> 대소관계 활용

   ```python
   # orm
   User.objects.filter(age__gte=30)
   # <QuerySet [<User: 정호>, <User: 경희>, '...(remaining elements truncated)...']>
   User.objects.filter(age__gte=30).count()
   # 43
   ```

      ```sql
   -- sql
      ```

4. 나이가 20살 이하인 사람의 인원 수 

   ```python
   # orm
   User.objects.filter(age__lte=20).count()
   # 23
   ```

   ```sql
   -- sql
   ```

5. 나이가 30이면서 성이 김씨인 사람의 인원 수

   ```python
   # orm
   User.objects.filter(age=30, last_name='김').count()
   # 1
   ```

      ```sql
   -- sql
      ```

6. 나이가 30이거나 성이 김씨인 사람?

   ```python
   # orm
   # 기본
   User.objects.filter(last_name='김') | User.objects.filter(age=30)
   (User.objects.filter(last_name='김') | User.objects.filter(age=30)).count()
   
   # Q활용
   from django.db.models import Q
   User.objects.filter(Q(age=30) | Q(last_name='김'))
   User.objects.filter(Q(age=30) | Q(last_name='김')).count()
   ```

   ```sql
   -- sql
   ```

7. 지역번호가 02인 사람의 인원 수

   - `ORM`: `__startswith` 

   ```python
   # orm
   User.objects.filter(phone__startswith='02').count()
   ```

      ```sql
   -- sql
   SELECT COUNT(*) FROM users_user WHERE phton LIKE '02-%'
      ```

8. 거주 지역이 강원도이면서 성이 황씨인 사람의 이름

   ```python
   # orm
   User.objects.filter(country='강원도', last_name='황').values('first_name')
   ```
   
      ```sql
   -- sql
      ```
   
   8 - 1. ~ 핸드폰 번호
   
   ```python
   User.objects.filter(country='강원도', last_name='황').values('phone')
   ```
   
   

---



### 3. 정렬 및 LIMIT, OFFSET

1. 나이가 많은 사람순으로 10명

   ```python
   # orm
   User.objects.order_by('-age')[:10].values('age')
   # <QuerySet [{'age': 40}, {'age': 40}, {'age': 40}, {'age': 40}, {'age': 40}, {'age': 39}, {'age': 39}, {'age': 39}, {'age': 39}, {'age': 39}]>
   ```

      ```sql
   -- sql
      ```

2. 잔액이 적은 사람순으로 10명

   ```python
   # orm
   User.objects.order_by('balance')[:10].values('first_name')
   ```

      ```sql
   -- sql
      ```

3. 잔고는 오름차순, 나이는 내림차순으로 10명?

      ```python
   # orm
   User.objects.order_by('balance', '-age')[:10]
   # <QuerySet [<User: 우진>, <User: 보람>, <User: 재현>, <User: 영환>, <User: 숙자>, <User: 미경>, <User: 우진>, <User: 명자>, <User: 준호>, <User: 은영>]>
   ```
   
   ```sql
   -- sql
   ```
   
4. 성, 이름 내림차순 순으로 5번째 있는 사람

   ```python
   # orm
   User.objects.order_by('-last_name', '-first_name')[4]
   ```
   
      ```sql
   -- sql
      ```



---



### 4. 표현식

#### 4.1 Aggregate

> - https://docs.djangoproject.com/en/3.2/topics/db/aggregation/#aggregation
>- '종합', '집합', '합계' 등의 사전적 의미
> - 특정 필드 전체의 합, 평균 등을 계산할 때 사용
>- `Django_aggregation.md` 문서 참고

1. 전체 평균 나이

   ```python
   # orm
   from django.db.models import Avg, Sum, Max, Min 등등등
   User.objects.aggregate(Avg('age'))
   # {'age__avg': 28.23}
   User.objects.aggregate(age_average=Avg('age'))
   # {'age_average': 28.23} => 키값 지정 가능
   ```

      ```sql
   -- sql
      ```

2. 김씨의 평균 나이

   ```python
   # orm
   User.objects.filter(last_name='김').aggregate(Avg('age'))
   # {'age__avg': 28.782608695652176}
   
   User.objects.filter(last_name='김').aggregate(Avg('age'), Min('age'), Sum('balance'))
   # {'age__avg': 28.782608695652176, 'age__min': 15, 'balance__sum': 3749100} => 여러개도 동시에 가능
   ```

      ```sql
   -- sql
      ```

3. 강원도에 사는 사람의 평균 계좌 잔고

   ```python
   # orm
   User.objects.filter(country='강원도').aggregate(Avg('balance'))
   ```

   ```sql
   -- sql
   ```

4. 계좌 잔액 중 가장 높은 값

   ```python
   # orm
   User.objects.aggregate(Max('balance'))
   ```

      ```sql
   -- sql
      ```

5. 계좌 잔액 총액

   ```python
   # orm
   User.objects.aggregate(Sum('balance'))
   ```
   
      ```sql
   -- sql
      ```



#### 4.2 Annotate

- 주석을 달다 라는 사전적 의미
- 필드 하나를 만들고, 거기에 어떤 내용을 집어 넣는다.
- db에 영향을 주지 않고, queryset에 컬럼 하나를 추가하는 것과 같다.

1. 지역별 인원 수

   ```PYTHON
   # orm
   User.objects.values('country').annotate(Count('country'))
   # <QuerySet [{'country': '강원도', 'country__count': 14}, {'country': '경기도', 'country__count': 9}, {'country': '경상남도', 'country__count': 9}, {'country': '경상북도', 'country__count': 15}, {'country': '전라남도', 'country__count': 10}, {'country': '전라북도', 'country__count': 11}, {'country': '제주특별자치도', 'country__count': 9}, {'country': '충청남도', 'country__count': 9}, {'country': '충청북도', 'country__count': 14}]>
   ```
   
   ```SQL
   -- sql
   ```
   
   