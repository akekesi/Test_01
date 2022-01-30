import os
import json
import shutil
from test_create_directory import func_create_directory, func_create_directories


class Prepare:
    def __init__(self, path, structure, files):
        self.path = path
        self.structure = structure
        self.files = files


    def meth_delete_directories(self):
        shutil.rmtree(self.path)
    
    
    def meth_create_directories(self):
        func_create_directory(self.path)
        func_create_directories(self.path, self.structure)


    def meth_create_files(self):
        for key, value in self.files.items():
            for k in value:
                tmp_key = f"00_{key}"
                path_tmp = f"{self.structure[tmp_key]}\{k}.{key}"
                self.files[key][k] = path_tmp
                if not os.path.exists(path_tmp):
                    with open(path_tmp, 'w'): pass


if __name__ == "__main__":
    # value
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

    # test
    prep = Prepare(path, structure, files)
    prep.meth_delete_directories()
    prep.meth_create_directories()
    prep.meth_create_files()
    print(json.dumps(prep.structure, indent=4))
    print(json.dumps(prep.files, indent=4))
