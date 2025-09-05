import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app.geometry.rectangle_area import rectangle_area


def test_rectangle_area_correct_length():
    width = "3"
    height = "5"
    expected_result = 15.0
    result = rectangle_area(width, height)
    assert result == pytest.approx(expected_result)
    # Act
    actual_result = rectangle_area(width, height)

    # Assert
    assert actual_result == pytest.approx(expected_result)

def test_rectangle_area_string_data():
    """Тестирование вычисления площади со строкой в качестве стороны прямоугольника"""
    # Arrange
    width = "hello"
    height = "5.2"

    # Act & Assert
    with pytest.raises(ValueError) as exc_info:
        rectangle_area(width, height)

    # Проверяем, что сообщение исключения соответствует ожидаемому
    assert str(exc_info.value) == "Введено не числовое значение стороны"

def test_rectangle_area_with_spaces_and_tabs():
    """Тест: обработка строки с пробелами и табуляцией (например, '  3,14  \t  ')"""
    width = "  3,14  \t"
    height = "2"
    expected_area = 6.28

    result = rectangle_area(width, height)

    assert result == pytest.approx(expected_area)


def test_rectangle_area_very_large_numbers():
    """Тест: работа с очень большими числами (проверка на переполнение и тип float)"""
    width = "1e10"      # 10 миллиардов
    height = "1e5"      # 100 тысяч
    expected_area = 1e15  # 1 квадриллион

    result = rectangle_area(width, height)

    assert result == pytest.approx(expected_area)