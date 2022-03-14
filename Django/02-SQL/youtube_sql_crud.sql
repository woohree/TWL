-- SQLite
INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
INSERT INTO classmates VALUES ('홍길동', 30, '서울');
SELECT * FROM classmates; -- 조회
SELECT rowid, * FROM classmates; -- pk값 조회하기

DROP TABLE classmates; -- classmates 지우기

CREATE TABLE classmates (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INT NOT NULL,
  address TEXT NOT NULL
);

INSERT INTO classmates (name, age, address) VALUES ('오수정', 30, '서울');

CREATE TABLE classmates (
  -- rowid INTEGER PRIMARY KEY AUTOINCREMENT, -- rowid 재활용X
  name TEXT NOT NULL,
  age INT NOT NULL,
  address TEXT NOT NULL
);

INSERT INTO classmates VALUES ('홍길동', 30, '서울'), ('김철수', 20, '용인'), ('이싸피', 26, '광주'), ('김송송', 50, '수원'), ('박칠칠', 10, '구미');

SELECT rowid, * FROM classmates; -- rowid, 전체 조회
SELECT rowid, name FROM classmates LIMIT 1; -- 하나만 조회
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2; -- 3번째 행 하나만 조회(앞 두개 offset)
SELECT rowid, name FROM classmates OFFSET 2 LIMIT 1; -- 순서바꾸니까 안되넹

SELECT rowid, * FROM classmates WHERE address="서울"; -- address 조건 맞는 것만 
SELECT DISTINCT age FROM classmates; -- 중복빼고 조회

DELETE FROM classmates WHERE rowid=7; -- rowid 7 데이터 삭제
INSERT INTO classmates VALUES ('김핍퍕', 60, '제주'); -- 가장 마지막 rowid 사용 => rowid=5

UPDATE classmates SET name='송송킴', address='제주' WHERE rowid=4; -- 이름, 주소 수정
SELECT rowid, * FROM classmates;



-- csv 파일로 만지기 --
CREATE TABLE users (
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);
-- sqlite3 tuto.sqlite3
-- .mode csv
-- .import users.csv users
-- .tables


SELECT * FROM users WHERE age >= 30;
SELECT first_name FROM users WHERE age >= 30;
SELECT age, first_name FROM users WHERE age >= 30 and last_name='김';

SELECT COUNT(*) FROM users;
SELECT AVG(age) FROM users WHERE age >= 30;
SELECT * FROM users WHERE age = (SELECT max(age) FROM users);  -- 가장 나이 많은 사람들
SELECT MAX(balance), * FROM users;
SELECT AVG(balance) FROM users WHERE age >= 30;

-- %: 많이, _: 하나 --
SELECT * FROM users WHERE age LIKE '2_';  -- 20대 검색
SELECT * FROM users WHERE phone LIKE '02-%';  -- 02 지역번호 검색
SELECT * FROM users WHERE first_name LIKE '%준';  -- 준으로 끝나는 이름
SELECT * FROM users WHERE phone LIKE '%-5114-%';  -- 중간번호가 5114

SELECT * FROM users ORDER BY age ASC LIMIT 10;  -- 오름차순 정렬 + 10개만
SELECT * FROM users ORDER BY age ASC, last_name DESC;  -- 나이 오름차순, 성 내림차순으로 정렬
SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;  -- 계좌잔액 내림차순 정렬 + 10명의 이름

SELECT last_name, COUNT(*) AS 수 FROM users GROUP BY last_name;  -- 각 성씨가 몇 명인지


-- 잠깐 복습 + ALTER TABLE statement

CREATE TABLE articles (
  title TEXT NOT NULL,
  content TEXT NOT NULL
);

SELECT * FROM brandnew_name;
INSERT INTO articles VALUES ('1번 제목', '1번 내용');
ALTER TABLE articles RENAME TO brandnew_name;  -- 테이블 이름 수정
-- 1. not null 없이 column 추가
ALTER TABLE brandnew_name ADD COLUMN created_at TEXT;
INSERT INTO brandnew_name VALUES ('제목', '내용', datetime('now'));
-- 2. not null + default column 추가
ALTER TABLE brandnew_name ADD COLUMN subtitle TEXT NOT NULL DEFAULT '소제목';
ALTER TABLE brandnew_name RENAME COLUMN title TO real_title;  -- column명 수정
ALTER TABLE brandnew_name DROP COLUMN subtitle;  -- column 제거