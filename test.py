import unittest
import app3

class TestApp(unittest.TestCase):
	# create test cases
    def test_add_numbers(self):
        self.assertEqual(app3.add_numbers(list(range(5))),10)
        self.assertEqual(app3.add_numbers([-3,0,6,9]),12)
        self.assertEqual(app3.add_numbers([-1.5,-4,10]),4.5)

if __name__ == '__main__':
    unittest.main()