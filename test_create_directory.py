import os

from test_json import func_write_json


def func_create_directory(path):
    """
    Create directory
    Args:
        path:   path of directory
    Returns:
        None
    """
    try:
        os.mkdir(path)
    except OSError as e:
        print(f"--> not created {path}\n    {e}")
    else:
        print(f"--> created {path}")


if __name__ == "__main__":
    # value
    path = [
        r"C:\Users\kekes\OneDrive\Desktop\delete\00_test",
        r"C:\Users\kekes\OneDrive\Desktop\delete\00_test",
        r"C:\Users\kekes\OneDrive\Desktop\d\00_test"
    ]

    # test
    for p in path:
        res = func_create_directory(p)
        print(f"func_create_directory --> {res}")
