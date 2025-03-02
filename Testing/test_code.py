"Must run pip install pytest and then python -m pytest */test_code.py"

import Rectangle

class TestGetAreaRectangle:
    def test_normal_case(self):
        rectangle = Rectangle.Rectangle(2, 3)
        assert rectangle.get_area() == 6, "incorrect area"
    
    def test_negative_case(self):
        """exptect -1 as output to denote error when looking at negative area"""
        rectangle = Rectangle.Rectangle(-1, 2)
        assert rectangle.get_area() == -1, "incorrect negative output"