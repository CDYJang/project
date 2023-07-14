import unittest
from plus import sum_numbers_from_file
class TestPlus(unittest.TestCase):
    def test_0(self):
        file_path = './data/data.txt'
        with open(file_path, 'r') as file:
            result = sum_numbers_from_file(file)
        self.assertEqual(result,27.0)


if __name__=="__main__":
    unittest.main()