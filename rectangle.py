def area(a, b): 
    '''
    Возвращает площадь прямоугольника по заданным сторонам
        Параметры:
            a (int): сторона a - десятичное число
            b (int): сторона b - десятичное число
        Возвращаемое значение:
            area (int): десятичное число - площадь 
        Примеры использования: area(5, 4) Возвращает: Вывод: 20
    '''
    return a * b 

def perimeter(a, b): 
    '''Возвращает периметр прямоугольника по заданным сторонам
        Параметры:
            a (int): сторона a - десятичное число
            b (int): сторона b - десятичное число
        Возвращаемое значение:
            perimeter (int): десятичное число - периметр прямоугольника
        Примеры использования: perimeter(5) Возвращает: 31.41592653589793
    '''
    return (a + b) * 2