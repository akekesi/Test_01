from dataclasses import dataclass
import json


def func_write_json(path: str, data: dict) -> None:
    """
    Write data to json
    Args:
        path:   path of json
        data:   data to write in json
    Returns:
        None
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    return None


def func_read_json(path: str) -> str:
    """
    Read json
    Args:
        path:   path of json
    Returns:
        data:   content of json
    """
    with open(path) as f:
        data = json.load(f)

    return data


if __name__ == "__main__":
    # help
    help(func_read_json)
    help(func_write_json)

    # values
    data = {
        "a": 1,
        "b": 2,
        "c": 3
    }
    path = r"C:\Users\kekes\OneDrive\Desktop\delete.json"

    # test
    res_write = func_write_json(path, data)
    print(f"func_write_json\t--> {res_write}")

    data_read = func_read_json(path)
    print(f"func_read_json\t--> {data_read}")
