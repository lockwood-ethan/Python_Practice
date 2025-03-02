import pytest
import Rectangle

@pytest.fixture
def rectangle():
    return Rectangle.Rectangle(0, 0)

def test_negative_case(rectangle):
    print(rectangle.width)
    rectangle.set_width(-1)
    rectangle.set_height(2)
    assert rectangle.get_area() == -1, "incorrect negative input"