import unittest
from test_json import func_write_json

class Test(unittest.TestCase):

    def test_func_wite_json(self):
        # values
        data_1 = {
            "a": 1,
            "b": 2,
            "c": 3
        }
        path_1 = r"C:\Users\kekes\OneDrive\Desktop\delete.json"
        self.assertEqual(func_write_json(path_1, data_1), None)


if __name__ == "__main__":
    unittest.main()