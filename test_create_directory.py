import os


def func_create_directories(path, structure):
    """
    Create directory structure
    Args:
        path:   path of main directory
        structure:  structure of directories
    Returns:
        structure:  structure competed with paths 
    """
    for key in structure:
        p = f"{path}/{key}"
        if isinstance(structure[key], dict):
            func_create_directory(p)
            func_create_directories(p, structure[key])
        else:
            func_create_directory(p)
            structure[key] = p
    
    return structure


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
    structure = {
        "00_a": {
            "10_a": "",
            "11_b": "",
            "12_c": {
                "20_a": "",
                "21_b": ""
            }
        },
        "01_a": {
            "10_a": "",
            "11_b": "",
            "12_c": {
                "20_a": "",
                "21_b": ""
            }
        },
        "02_a": ""
    }

    # test
    for p in path:
        res = func_create_directory(p)
        print(f"func_create_directory --> {res}")
    
    res = func_create_directories(path[0], structure)
    print(res)
