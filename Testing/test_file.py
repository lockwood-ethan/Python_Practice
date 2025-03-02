"""Must run pip install pytest and then python -m pytest */test_file.py"""

import Rectangle

def test_normal_case():
    rectangle = Rectangle.Rectangle(2, 3)
    assert rectangle.get_area() == 6, "incorrect area"