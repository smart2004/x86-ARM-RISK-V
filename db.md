#### Вот примеры SQL-запросов и работы с MySQL, PostgreSQL и Redis.


##### 1. MySQL
Создание базы данных и таблицы
```
CREATE DATABASE school; USE school; 
CREATE TABLE students ( id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100) NOT NULL, age INT, grade VARCHAR(10) ); 
```
Вставка данных
```
INSERT INTO students (name, age, grade) VALUES ('Alice', 10, '5th');

INSERT INTO students (name, age, grade) VALUES ('Bob', 11, '6th'); 
```
Запрос данных
```
SELECT * FROM students;
```
Обновление данных
```
UPDATE students SET grade = '6th' WHERE name = 'Alice'; 
```
Удаление данных
```
DELETE FROM students WHERE name = 'Bob'; 
```

##### 2. PostgreSQL
Создание базы данных и таблицы
```
CREATE DATABASE school; \c school; -- Подключение к базе данных CREATE TABLE students ( id SERIAL PRIMARY KEY, name VARCHAR(100) NOT NULL, age INT, grade VARCHAR(10) ); 
```
Вставка данных
```
INSERT INTO students (name, age, grade) VALUES ('Alice', 10, '5th');

INSERT INTO students (name, age, grade) VALUES ('Bob', 11, '6th'); 
```

Запрос данных
```
SELECT * FROM students; 
```
Обновление данных
```
UPDATE students SET grade = '6th' WHERE name = 'Alice'; 
```
Удаление данных
```
DELETE FROM students WHERE name = 'Bob'; 
```

##### 3. Redis
Redis работает немного иначе, так как это хранилище данных в памяти, а не реляционная база данных. Вот примеры работы с Redis:

Установка соединения
```
import redis # Создание соединения с Redis 
r = redis.Redis(host='localhost', port=6379, db=0) 
```
Добавление данных
```
# Сохранение данных r.set('student:1:name', 'Alice') r.set('student:1:age', 10) r.set('student:1:grade', '5th') r.set('student:2:name', 'Bob') r.set('student:2:age', 11) r.set('student:2:grade', '6th') 
```
Получение данных
```
# Получение данных name = r.get('student:1:name').decode('utf-8') age = r.get('student:1:age').decode('utf-8') grade = r.get('student:1:grade').decode('utf-8') print(f'Student: {name}, Age: {age}, Grade: {grade}') 
```
Удаление данных
```
# Удаление данных r.delete('student:2:name') r.delete('student:2:age') r.delete('student:2:grade') 
```
Заключение
Эти примеры показывают основные операции с MySQL и PostgreSQL, а также работу с Redis. MySQL и PostgreSQL используют SQL-запросы для управления данными, в то время как Redis использует команды для работы с ключами и значениями в памяти.
