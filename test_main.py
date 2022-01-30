from test_json import func_read_json
from test_create_directory import func_create_directory, func_create_directories


def func_test_main(path_structure: str, path_directory: str) -> dict:
    """
    Create directories
    Args:
        path_structure: path of dict of structure
        path_directory: path of main directory
    Returns:
        structure_path: structure with paths as dict
    """
    structure = func_read_json(path_structure)
    structure_path = func_create_directories(path_directory, structure)
    return structure_path

if __name__ == "__main__":
    # path
    path_structure = r"C:\00_TUBI\99_GIT\Test_01\00_json\test_structure.json"
    path_directory = r"C:\Users\kekes\OneDrive\Desktop\delete\00_test_main"

    # test
    func_create_directory(path_directory)
    structure_path = func_test_main(path_structure, path_directory)
    print(structure_path)