-- 1)
CREATE TABLE countries (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  room_num TEXT NOT NULL,
  check_in TEXT NOT NULL,
  check_out TEXT NOT NULL,
  grade TEXT NOT NULL,
  price INTEGER NOT NULL
);
-- 2)
INSERT INTO countries (room_num, check_in, check_out, grade, price)
VALUES
('B203', '2019-12-31', '2020-01-03', 'suite', 900),
('1102', '2020-01-04', '2020-01-08', 'suite', 850),
('303', '2020-01-01', '2020-01-03', 'deluxe', 500),
('807', '2020-01-04', '2020-01-07', 'superior', 300);
-- 3)
ALTER TABLE countries RENAME TO hotels;
-- 4)
SELECT room_num, price FROM hotels ORDER BY price DESC LIMIT 2;
-- 5)
SELECT grade, COUNT(*) AS grade_count FROM hotels GROUP BY grade ORDER BY grade_count DESC;
-- 6)
SELECT * FROM hotels WHERE (room_num LIKE 'B%') or (grade LIKE 'deluxe');
-- 7)
SELECT * FROM hotels WHERE (room_num NOT LIKE 'B%') and (check_in LIKE '2020-01-04') ORDER BY price;