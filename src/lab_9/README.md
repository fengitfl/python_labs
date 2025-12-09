# Лабораторная работа 9 

## Цель работы
Реализовать простое хранилище данных студентов на основе CSV-файла с использованием CRUD-операций.

## Реализованные возможности

### Класс Group
- **Инициализация**: `Group(storage_path)` - создает или открывает CSV-файл

- **Добавление**: `add(student)` - добавляет нового студента

- **Чтение**: `list()` - возвращает всех студентов

- **Поиск**: `find(substr)` - ищет студентов по подстроке в ФИО

- **Обновление**: `update(fio, **fields)` - обновляет данные студента

- **Удаление**: `remove(fio)` - удаляет студента по ФИО

- **Статистика**: `stats()` - собирает статистику по группе (дополнительное задание)

- **Вывод**: `print_stats()` - выводит статисктику по строкам(красивый вид)

## Код group 
![alt text](../../images/lab_9/group1.png)
![alt text](../../images/lab_9/group2.png)
![alt text](../../images/lab_9/group3.png)
![alt text](../../images/lab_9/group4.png)
![alt text](../../images/lab_9/group5.png)

# Создание группы
group = Group("data/lab09/students.csv")

# Добавление студента
student = Student(fio="Никонов Егор",birthdate=date(2007, 11, 16),group="БИВТ25-5",gpa=2.0)
![alt text](../../images/lab_9/add.png)
![alt text](../../images/lab_9/add1.png)

# Получение всех студентов
![alt text](../../images/lab_9/all_students01.png)
![alt text](../../images/lab_9/all_students.png)

# Поиск студентов

![alt text](../../images/lab_9/find1.png)
![alt text](../../images/lab_9/find2.png)

# Обновление данных

![alt text](../../images/lab_9/update1.png)
![alt text](../../images/lab_9/update2.png)

# Удаление студента
![alt text](../../images/lab_9/remove1.png)
![alt text](../../images/lab_9/remove2.png)

# Получение статистики
![alt text](../../images/lab_9/stats1.png)
![alt text](../../images/lab_9/stats2.png)