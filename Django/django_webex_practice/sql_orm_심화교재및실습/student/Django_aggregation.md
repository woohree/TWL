[toc]

# Django_Aggregation

> [Joins and aggregates](https://docs.djangoproject.com/en/3.1/topics/db/aggregation/#joins-and-aggregates)
>
> [Aggregation](https://docs.djangoproject.com/en/3.1/topics/db/aggregation/#aggregation)
>
> [`QuerySet` API reference - annotate()](https://docs.djangoproject.com/ko/3.1/ref/models/querysets/#annotate)
>
> [`QuerySet` API reference - Aggregation functions](https://docs.djangoproject.com/ko/3.1/ref/models/querysets/#aggregation-functions)

---

## Annotate

- Annotate calculates summary values for each item in the queryset.
- '주석을 달다' 라는 사전적 의미

  - SQL의 `GROUP BY`

- 필드를 하나 만들고 거기에 '어떤 내용'을 채워 넣는다.
- 데이터베이스에 영향을 주지 않고, Querset에 컬럼 하나를 추가하는 것과 같다.

<br>

### 한 영화의 댓글 평점 평균 값 구하기

> Movie 모델과 Comment 모델이 1:N 관계라고 가정

```python
from django.db.models import Avg

movie = Movie.objects.annotate(score_avg=Avg('comment__score')).get(pk=1)
```

- 현재 Comment 모델 테이블이 다음과 같다면,

| id  | content      | score | movie_id |
| --- | ------------ | ----- | -------- |
| 1   | 짱짱         | 10    | 2        |
| 2   | 고양이졸귀탱 | 6     | 1        |
| 3   | 마블 명작    | 8     | 1        |
| 4   | 어벤져스     | 1     | 1        |

> movie_id가 1 (`.get(pk=1)`)이면서, comment 테이블의 score 컬럼의(`comment__score`) 평균(`Avg`)을 `score_avg` 라는 칼럼으로 추가적으로 만들어 붙여서(`annotate`) 결과를 받아보겠다.

- 해당 sql 결과 조회하게 되는 table은 다음과 같이 작성된다. (Movie 테이블의 원본에는 변화가 없다.)

| id  | title     | audience | poster_url | description | score_avg |
| --- | --------- | -------- | ---------- | ----------- | --------- |
| 1   | 캡틴 마블 | 3035808  | https://   | 캡틴 마블.. | 5         |

<br>

---

<br>

### 모든 영화의 댓글 평점 평균 값

```python
movies = Movie.objects.annotate(score_avg=Avg('comment__score'))
```

- 대응되는 SQL 문

  ```sqlite
  SELECT
  "movies_movie"."id", "movies_movie"."title", "movies_movie"."audience", "movies_movie"."poster_url", "movies_movie"."description", AVG("movies_score"."score") AS "score_avg"
  FROM "movies_movie" LEFT OUTER JOIN "movies_comment" ON ("movies_movie"."id" = "movies_comment"."movie_id") GROUP BY "movies_movie"."id", "movies_movie"."title", "movies_movie"."audience", "movies_movie"."poster_url", "movies_movie"."description"
  ```

* 현재 Comment 테이블이 다음과 같다면,

| id  | content      | score | movie_id |
| --- | ------------ | ----- | -------- |
| 1   | 짱짱         | 10    | 2        |
| 2   | 고양이졸귀탱 | 6     | 1        |
| 3   | 마블 명작    | 8     | 1        |
| 4   | 어벤져스     | 1     | 1        |

> Comment 테이블의 score 컬럼의(`comment__score`) 평균(`Avg`)을 `score_avg` 라는 칼럼으로 추가적으로 붙여서(`annotate`) 모든 데이터의 결과를 받아보겠다.

- 해당 sql 결과 조회하게 되는 table은 다음과 같이 작성된다. (Movie 테이블의 원본에는 변화가 없다.)

| id  | title             | audience | poster_url | description | score_avg |
| --- | ----------------- | -------- | ---------- | ----------- | --------- |
| 1   | 캡틴 마블         | 3035808  | https://.. | 캡틴 마블.. | 5         |
| 2   | 항거:유관순이야기 | 1041939  | https://.. | ...         | 10        |
| ... |                   |          |            |             |           |

- 따라서, 템플릿에서 다음과 같이 작성할 수 있다.

  ```django
  <!-- detail.html -->
  
  <h4>종합 평점 : {{ movie.score_avg }}</h4>
  ```

  ```django
  <!-- index.html -->
  
  {% for movie in movies %}
    <a href="{% url 'movies:detail' movie.pk %}">{{ movie.title }}</a><br>
    <p>종합 평점 : {{ movie.score_avg }}</p>
    <img src="{{ movie.poster_url }}" alt="poster">
    <hr>
  {% endfor %}
  ```

<br>

---

<br>

## Aggregate

- Aggregate calculates values for the entire queryset.
- 집계 함수(Avg, Max, Min, Count, Sum 등)을 사용할 때 사용하는 메서드.
- 특정 필드 전체의 합, 평균, 개수 등을 계산할 때 사용
- 집계 함수를 파라미터로 받아서 딕셔너리를 반환

<br>

```python
>>> Book.objects.aggregate(average_price=Avg('price'))
{'average_price': 34.35}
```

- Book 모델의 price 컬럼 값의 평균
- 즉, 모든 도서의 평균 값 (`average_price`)
