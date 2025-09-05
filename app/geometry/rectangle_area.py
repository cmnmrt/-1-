# rectangle_area.py

def parse_number(value: str) -> float:
    """
    Проверка корректности ввода стороны прямоугольника
    :param value: пользовательский ввод длины стороны прямоугольника
    :return: number: длина стороны прямоугольника (тип float)
    """
    try:
        input_data = value.strip().replace(',', '.')
        number = float(input_data)
        if number <= 0:
            raise ValueError("Сторона должна быть положительным числом")
        else:
            return number
    except ValueError:
        raise ValueError("Введено не числовое значение стороны")


def rectangle_area(width: str, height: str) -> float:
    """
    Нахождение площади прямоугольника
    :param width: ширина прямоугольника
    :param height: высота прямоугольника
    :return: площадь прямоугольника
    """
    w = parse_number(width)
    h = parse_number(height)
    return w * h