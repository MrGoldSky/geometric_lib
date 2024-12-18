
# Геометрические Функции

Решение предлагает отдельные библиотеки для геометрических фигур, в которых есть функции для подсчёта периметра и площади фигуры.



## `circle.py`

### Функции

#### `area(r)`
Возвращает площадь круга по заданному радиусу.

- **Параметры:**
  - `r` (*int*): радиус круга — десятичное число.
- **Возвращаемое значение:**
  - `area` (*float*): число с плавающей точкой — площадь круга.

**Пример использования:**
```python
from circle import area
print(area(5))  # Вывод: 78.53981633974483
```

#### `perimeter(r)`
Возвращает длину окружности по заданному радиусу.

- **Параметры:**
  - `r` (*int*): радиус окружности — десятичное число.
- **Возвращаемое значение:**
  - `perimeter` (*float*): число с плавающей точкой — длина окружности.

**Пример использования:**
```python
from circle import perimeter
print(perimeter(5))  # Вывод: 31.41592653589793
```

---

## `rectangle.py`

### Функции

#### `area(a, b)`
Возвращает площадь прямоугольника по заданным сторонам.

- **Параметры:**
  - `a` (*int*): сторона прямоугольника — десятичное число.
  - `b` (*int*): сторона прямоугольника — десятичное число.
- **Возвращаемое значение:**
  - `area` (*int*): десятичное число — площадь прямоугольника.

**Пример использования:**
```python
from rectangle import area
print(area(4, 5))  # Вывод: 20
```

#### `perimeter(a, b)`
Возвращает периметр прямоугольника по заданным сторонам.

- **Параметры:**
  - `a` (*int*): сторона прямоугольника — десятичное число.
  - `b` (*int*): сторона прямоугольника — десятичное число.
- **Возвращаемое значение:**
  - `perimeter` (*int*): десятичное число — периметр прямоугольника.

**Пример использования:**
```python
from rectangle import perimeter
print(perimeter(4, 5))  # Вывод: 18
```

---

## `square.py`

### Функции

#### `area(a)`
Возвращает площадь квадрата по заданной стороне.

- **Параметры:**
  - `a` (*int*): сторона квадрата — десятичное число.
- **Возвращаемое значение:**
  - `area` (*int*): десятичное число — площадь квадрата.

**Пример использования:**
```python
from square import area
print(area(4))  # Вывод: 16
```

#### `perimeter(a)`
Возвращает периметр квадрата по заданной стороне.

- **Параметры:**
  - `a` (*int*): сторона квадрата — десятичное число.
- **Возвращаемое значение:**
  - `perimeter` (*int*): десятичное число — периметр квадрата.

**Пример использования:**
```python
from square import perimeter
print(perimeter(4))  # Вывод: 16
```

## `triangle.py`

### Функции

#### `area(a, h)`
Возвращает площадь треугольника по заданной стороне и высоте.

- **Параметры:**
  - `a` (*int*): сторона треугольника — десятичное число.
  - `h` (*int*): высота треугольника — десятичное число.
- **Возвращаемое значение:**
  - `area` (*int*): десятичное число — площадь треугольника.

**Пример использования:**
```python
from triangle import area
print(area(5, 6))  # Вывод: 15.0
```

#### `perimeter(a, b, c)`
Возвращает периметр треугольника по трём сторонам.

- **Параметры:**
  - `a` (*int*): сторона треугольника — десятичное число.
  - `b` (*int*): сторона треугольника — десятичное число.
  - `c` (*int*): сторона треугольника — десятичное число.
- **Возвращаемое значение:**
  - `perimeter` (*int*): десятичное число — периметр треугольника.

**Пример использования:**
```python
from triangle import perimeter
print(perimeter(3, 4, 5))  # Вывод: 12
```
Хеши коммитов
```
9a14a1a (HEAD -> new_features_472417) Edit rectangle.py, added triangle.py
f9cb390 Add rectangle.py
d078c8d (origin/main, origin/HEAD, main, labwork2) L-03: Docs added
8ba9aeb L-03: Circle and square added
```