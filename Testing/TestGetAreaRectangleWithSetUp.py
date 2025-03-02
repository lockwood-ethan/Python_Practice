import unittest
import Rectangle

class TestGetAreaRectangleWithSetUp(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle.Rectangle(0,0)
        
    @classmethod
    def setUpClass(self):
        #this method is only run once for the entire class rather than being run for each test which is done for setUp()
        self.rectangle = Rectangle.Rectangle(0, 0)
        
    def test_normal_case(self):
        self.rectangle.set_width(2)
        self.rectangle.set_height(3)
        self.assertEqual(self.rectangle.get_area(), 6, "incorrect area")
        
    def test_negative_case(self):
        """expect -1 as output to denote error when looking at negative area"""
        self.rectangle.set_width(-1)
        self.rectangle.set_height(2)
        self.assertEqual(self.rectangle.get_area(), -1, "incorrect negative input")
        
    def test_geq(self):
        """tests if value is greater than or equal to a particular target"""
        rectangle = Rectangle.Rectangle(2, 3)
        self.assertGreaterEqual(rectangle.get_area, -1)
        
    def test_assert_raises(self):
        """using assertRaises to detect if an expected error is raised when running a particular block of code"""
        with self.assertRaises(ZeroDivisionError):
            a =  1 / 0