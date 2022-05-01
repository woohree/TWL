# SQL

- `SQLite3`으로 실습

## CRUD

### Create

```sql
CREATE TABLE users (
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);
```

### Read

```sql
SELECT * FROM users WHERE age >= 30;
SELECT first_name FROM users WHERE age >= 30;
SELECT age, first_name FROM users WHERE age >= 30 and last_name='김';

SELECT COUNT(*) FROM users;
SELECT AVG(age) FROM users WHERE age >= 30;
SELECT * FROM users WHERE age = (SELECT max(age) FROM users);  -- 가장 나이 많은 사람들
SELECT MAX(balance), * FROM users;
SELECT AVG(balance) FROM users WHERE age >= 30;

-- %: 0 ~ 많이, _: 하나 --
SELECT * FROM users WHERE age LIKE '2_';  -- 20대 검색
SELECT * FROM users WHERE phone LIKE '02-%';  -- 02 지역번호 검색
SELECT * FROM users WHERE first_name LIKE '%준';  -- 준으로 끝나는 이름
SELECT * FROM users WHERE phone LIKE '%-5114-%';  -- 중간번호가 5114

SELECT * FROM users ORDER BY age ASC LIMIT 10;  -- 오름차순 정렬 + 10개만
SELECT * FROM users ORDER BY age ASC, last_name DESC;  -- 나이 오름차순, 성 내림차순으로 정렬
SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;  -- 계좌잔액 내림차순 정렬 + 10명의 이름

SELECT last_name, COUNT(*) AS 수 FROM users GROUP BY last_name;  -- 각 성씨가 몇 명인지
```

### Update

```sql
INSERT INTO users (first_name, last_name) VALUES ('우현', '이');
```

### Delete

```sql
DELETE FROM classmates WHERE rowid=7; -- rowid 7 데이터 삭제
```

### `ALTER`

```sql
ALTER TABLE articles RENAME TO brandnew_name;  -- 테이블 이름 수정
-- 1. not null 없이 column 추가
ALTER TABLE brandnew_name ADD COLUMN created_at TEXT;
INSERT INTO brandnew_name VALUES ('제목', '내용', datetime('now'));
-- 2. not null + default column 추가
ALTER TABLE brandnew_name ADD COLUMN subtitle TEXT NOT NULL DEFAULT '소제목';
ALTER TABLE brandnew_name RENAME COLUMN title TO real_title;  -- column명 수정
ALTER TABLE brandnew_name DROP COLUMN subtitle;  -- column 제거
```



## PGS SQL

```SQL
-- 가장 큰 DATETIME을 가진 동물의 이름
SELECT NAME FROM ANIMAL_INS WHERE DATETIME = (SELECT MAX(DATETIME) FROM ANIMAL_INS)

-- 중복없이 이름 뽑기
SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS

-- 동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회하는 SQL문을 작성해주세요. 이때 결과는 이름이 없는 동물은 집계에서 제외하며, 결과는 이름 순으로 조회해주세요.
SELECT NAME, COUNT(NAME) AS COUNT FROM ANIMAL_INS GROUP BY NAME HAVING COUNT > 1 ORDER BY NAME

-- 09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요
SELECT HOUR(DATETIME) AS HOUR, COUNT(*) AS COUNT FROM ANIMAL_OUTS WHERE 9 <= HOUR(DATETIME) AND HOUR(DATETIME) < 20 GROUP BY HOUR(DATETIME) ORDER BY HOUR(DATETIME)

-- 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요.
WITH RECURSIVE TEMP AS (SELECT 0 AS HOURR UNION ALL SELECT HOURR + 1 FROM TEMP WHERE HOURR < 23)
SELECT HOURR, COUNT(HOUR(OUTS.DATETIME)) FROM TEMP LEFT JOIN ANIMAL_OUTS OUTS ON HOURR = HOUR(OUTS.DATETIME) GROUP BY HOURR ORDER BY HOURR

-- 프로그래밍을 모르는 사람들은 NULL이라는 기호를 모르기 때문에, 이름이 없는 동물의 이름은 "No name"으로 표시해 주세요.
SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name'), SEX_UPON_INTAKE FROM ANIMAL_INS ORDER BY ANIMAL_ID

-- 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회하는 SQL문을 작성해주세요.
SELECT OUTS.ANIMAL_ID, OUTS.NAME FROM ANIMAL_INS INS RIGHT JOIN ANIMAL_OUTS OUTS ON INS.ANIMAL_ID = OUTS.ANIMAL_ID WHERE INS.ANIMAL_ID IS NULL

-- 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 시작일 순으로 조회해야 합니다.
SELECT INS.NAME, INS.DATETIME FROM ANIMAL_INS INS LEFT JOIN ANIMAL_OUTS OUTS ON INS.ANIMAL_ID = OUTS.ANIMAL_ID WHERE OUTS.ANIMAL_ID IS NULL ORDER BY INS.DATETIME LIMIT 3

-- 보호소에 들어올 당시에는 중성화되지 않았지만, 보호소를 나갈 당시에는 중성화된 동물의 아이디와 생물 종, 이름을 조회하는 아이디 순으로 조회하는 SQL 문을 작성해주세요.
SELECT OUTS.ANIMAL_ID, OUTS.ANIMAL_TYPE, OUTS.NAME FROM ANIMAL_OUTS OUTS LEFT JOIN ANIMAL_INS INS ON OUTS.ANIMAL_ID = INS.ANIMAL_ID WHERE INS.SEX_UPON_INTAKE != OUTS.SEX_UPON_OUTCOME ORDER BY OUTS.ANIMAL_ID

-- 동물 보호소에 들어온 동물 중 이름이 Lucy, Ella, Pickle, Rogan, Sabrina, Mitty인 동물의 아이디와 이름, 성별 및 중성화 여부를 조회하는 SQL 문을 작성해주세요.
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE FROM ANIMAL_INS WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')

-- 동물 보호소에 들어온 동물 이름 중, 이름에 "EL"이 들어가는 개의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 이름 순으로 조회해주세요. 단, 이름의 대소문자는 구분하지 않습니다.
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE LOWER(NAME) LIKE '%el%' AND ANIMAL_TYPE = 'Dog' ORDER BY NAME

-- 동물의 아이디와 이름, 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성해주세요. 이때 중성화가 되어있다면 'O', 아니라면 'X'라고 표시해주세요.
SELECT ANIMAL_ID, NAME, CASE WHEN SEX_UPON_INTAKE LIKE '%Neutered%' OR SEX_UPON_INTAKE LIKE '%Spayed%' THEN 'O' ELSE 'X' END AS '중성화' FROM ANIMAL_INS ORDER BY ANIMAL_ID

-- 입양을 간 동물 중, 보호 기간이 가장 길었던 동물 두 마리의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 기간이 긴 순으로 조회해야 합니다.
SELECT OUTS.ANIMAL_ID, OUTS.NAME FROM ANIMAL_OUTS OUTS, ANIMAL_INS INS WHERE OUTS.ANIMAL_ID = INS.ANIMAL_ID ORDER BY DATEDIFF(INS.DATETIME, OUTS.DATETIME) LIMIT 2

-- 각 동물의 아이디와 이름, 들어온 날짜1를 조회하는 SQL문을 작성해주세요. 이때 결과는 아이디 순으로 조회해야 합니다.
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') FROM ANIMAL_INS ORDER BY ANIMAL_ID

-- RANK, 열 하나 늘려서 등수 체크
SELECT empNo, empName, salary,
RANK() OVER (ORDER BY salary DESC) RANK등수, -- 중복 동일 등수, 이후 중복 수 만큼 띄고 등수 지정
DENSE_RANK() OVER (ORDER BY salary DESC) DENSE_RANK등수, -- 중복 동일 등수, 이후 +1 등수
ROW_NUMBER() OVER (ORDER BY salary DESC) ROW_NUMBER등수 -- 중복 동일X 등수
FROM employee

-- NTILE, NTILE함수는 뒤에 함께 적어주는 숫자 만큼으로 등분을 하는 함수입니다.
SELECT empNo, empName, salary,
NTILE(4) OVER (ORDER BY salary DESC) NTILE등분
FROM employee

-- PARTITION BY, 특정 속성 별로 구분을 하고자 할 때 PARTITION BY절을 사용하면 됩니다. 속성마다 등수 구분
SELECT empName, job, salary,
RANK() OVER (PARTITION BY job ORDER BY salary DESC) RANK등수
FROM employee

-- TIMESTAMPDIFF(단위, 날짜1, 날짜2);
-- CHAR_LENGTH(문자열);

```

