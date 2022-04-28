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



## PGS SQP

```SQL
SELECT HOUR(DATETIME) AS hour, COUNT(*) FROM ANIMAL_OUTS WHERE 9 <= HOUR(DATETIME) AND HOUR(DATETIME) < 20 GROUP BY HOUR(DATETIME) ORDER BY HOUR(DATETIME)  -- 보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.

SELECT NAME, COUNT(*) AS count FROM ANIMAL_INS WHERE NAME IS NOT NULL GROUP BY NAME HAVING count >= 2 ORDER BY NAME ASC  -- 이름이 없는 동물은 제외하고, 동물 이름 중 두번 이상 쓰인 이름과 해당 횟수 조회, 이름 순으로 정렬

SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS;  -- 중복없이 이름 뽑기

SELECT ANIMAL_TYPE, IFNULL(NAME, "No name") AS NAME, SEX_UPON_INTAKE FROM ANIMAL_INS ORDER BY ANIMAL_ID ASC  -- 입양 게시판에 동물 정보를 게시하려 합니다. 동물의 생물 종, 이름, 성별 및 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성해주세요. 이때 프로그래밍을 모르는 사람들은 NULL이라는 기호를 모르기 때문에, 이름이 없는 동물의 이름은 "No name"으로 표시해 주세요.

SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE NAME LIKE '%EL%' AND ANIMAL_TYPE = 'DOG' ORDER BY NAME -- 보호소에 돌아가신 할머니가 기르던 개를 찾는 사람이 찾아왔습니다. 이 사람이 말하길 할머니가 기르던 개는 이름에 'el'이 들어간다고 합니다. 동물 보호소에 들어온 동물 이름 중, 이름에 "EL"이 들어가는 개의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 이름 순으로 조회해주세요. 단, 이름의 대소문자는 구분하지 않습니다.

SELECT ANIMAL_ID, NAME, CASE WHEN SEX_UPON_INTAKE LIKE '%Neutered%' OR SEX_UPON_INTAKE LIKE '%Spayed%' THEN 'O' ELSE 'X' END AS '중성화' FROM ANIMAL_INS ORDER BY ANIMAL_ID -- 보호소의 동물이 중성화되었는지 아닌지 파악하려 합니다. 중성화된 동물은 SEX_UPON_INTAKE 컬럼에 'Neutered' 또는 'Spayed'라는 단어가 들어있습니다. 동물의 아이디와 이름, 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성해주세요. 이때 중성화가 되어있다면 'O', 아니라면 'X'라고 표시해주세요.

SELECT OUTS.ANIMAL_ID, OUTS.NAME FROM ANIMAL_OUTS AS OUTS, ANIMAL_INS AS INS WHERE OUTS.ANIMAL_ID = INS.ANIMAL_ID ORDER BY DATEDIFF(INS.DATETIME, OUTS.DATETIME) LIMIT 2 -- 입양을 간 동물 중, 보호 기간이 가장 길었던 동물 두 마리의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 기간이 긴 순으로 조회해야 합니다.

SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') FROM ANIMAL_INS ORDER BY ANIMAL_ID -- ANIMAL_INS 테이블에 등록된 모든 레코드에 대해, 각 동물의 아이디와 이름, 들어온 날짜1를 조회하는 SQL문을 작성해주세요. 이때 결과는 아이디 순으로 조회해야 합니다.

SELECT A.ANIMAL_ID, A.NAME FROM ANIMAL_OUTS A LEFT JOIN ANIMAL_INS B ON A.ANIMAL_ID = B.ANIMAL_ID WHERE B.ANIMAL_ID IS NULL -- 천재지변으로 인해 일부 데이터가 유실되었습니다. 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회하는 SQL문을 작성해주세요.

SELECT A.ANIMAL_ID, A.NAME FROM ANIMAL_INS A LEFT JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID WHERE A.DATETIME > B.DATETIME ORDER BY A.DATETIME ASC -- 관리자의 실수로 일부 동물의 입양일이 잘못 입력되었습니다. 보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 시작일이 빠른 순으로 조회해야합니다.

SELECT INS.NAME, INS.DATETIME FROM ANIMAL_INS INS LEFT JOIN ANIMAL_OUTS OUTS ON INS.ANIMAL_ID = OUTS.ANIMAL_ID WHERE OUTS.ANIMAL_ID IS NULL ORDER BY INS.DATETIME LIMIT 3 -- 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 시작일 순으로 조회해야 합니다.

SELECT INS.ANIMAL_ID, INS.ANIMAL_TYPE, INS.NAME FROM ANIMAL_INS INS LEFT JOIN ANIMAL_OUTS OUTS ON INS.ANIMAL_ID = OUTS.ANIMAL_ID WHERE INS.SEX_UPON_INTAKE LIKE '%Intact%' AND (OUTS.SEX_UPON_OUTCOME LIKE '%Spayed%' OR OUTS.SEX_UPON_OUTCOME LIKE '%Neutered%') -- 보호소에서 중성화 수술을 거친 동물 정보를 알아보려 합니다. 보호소에 들어올 당시에는 중성화1되지 않았지만, 보호소를 나갈 당시에는 중성화된 동물의 아이디와 생물 종, 이름을 조회하는 아이디 순으로 조회하는 SQL 문을 작성해주세요.


```

