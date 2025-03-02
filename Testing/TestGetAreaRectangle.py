import unittest
import Rectangle

# The test based on unittest module
class TestGetAreaRectangle(unittest.TestCase):
    def test_normal_case(self):
        rectangle = Rectangle.Rectangle(2, 3)
        self.assertEqual(rectangle.get_area() , 6, "incorrect area")
        
    def test_negative_case(self):
        """expect -1 as output to denote error when looking at negative area"""
        rectangle = Rectangle.Rectangle(-1, 2)
        self.assertEqual(rectangle.get_area(), -1, "incorrect negative input")
        
    def test_geq(self):
        """tests if value is greater than or equal to a particular target"""
        rectangle = Rectangle.Rectangle(2, 3)
        self.assertGreaterEqual(rectangle.get_area, -1)
        
    def test_assert_raises(self):
        """using assertRaises to detect if an expected error is raised when running a particular block of code"""
        with self.assertRaises(ZeroDivisionError):
            a =  1 / 0
        
# run the test
unittest.main()