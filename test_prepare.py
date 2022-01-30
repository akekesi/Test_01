import os
import shutil
from test_create_directory import func_create_directory, func_create_directories

path = r"C:\Users\kekes\OneDrive\Desktop\delete\00_prepare"
structure = {
    "00_json": "",
    "00_txt": ""
}
files = {
    "json": {
        "json_00": "",
        "json_01": "",
        "json_02": ""
    },
    "txt": {
        "txt_00": "",
        "txt_01": "",
        "txt_02": ""
    }
}

shutil.rmtree(path)
func_create_directory(path)
structure_path = func_create_directories(path, structure)

for key, value in files.items():
    for k, v in value.items():
        tmp_key = f"00_{key}"
        path_f = f"{structure[tmp_key]}\{k}.{key}"
        files[key][k] = path_f
        if not os.path.exists(path_f):
            with open(path_f, 'w'): pass
