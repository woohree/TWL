# SQL

## CRUD

### Create

```sqlite
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

```sqlite
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

```sqlite
INSERT INTO users (first_name, last_name) VALUES ('우현', '이');
```

### Delete

```sqlite
DELETE FROM classmates WHERE rowid=7; -- rowid 7 데이터 삭제
```

### `ALTER`

```sqlite
ALTER TABLE articles RENAME TO brandnew_name;  -- 테이블 이름 수정
-- 1. not null 없이 column 추가
ALTER TABLE brandnew_name ADD COLUMN created_at TEXT;
INSERT INTO brandnew_name VALUES ('제목', '내용', datetime('now'));
-- 2. not null + default column 추가
ALTER TABLE brandnew_name ADD COLUMN subtitle TEXT NOT NULL DEFAULT '소제목';
ALTER TABLE brandnew_name RENAME COLUMN title TO real_title;  -- column명 수정
ALTER TABLE brandnew_name DROP COLUMN subtitle;  -- column 제거
```

