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
        data_2 = [
            "a",
            "b",
            "c"
        ]
        path_1 = r"C:\Users\kekes\OneDrive\Desktop\delete\delete_1.json"
        path_2 = r"C:\Users\kekes\OneDrive\Desktop\delete\delete_2.json"

        # test
        self.assertEqual(func_write_json(path_1, data_1), None)
        self.assertEqual(func_write_json(path_2, data_2), None)


if __name__ == "__main__":
    unittest.main()