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
        try:
            shutil.rmtree(self.path)
        except OSError as e:
            print(f"{e}")
    
    
    def meth_create_directories(self):
        func_create_directory(self.path)
        func_create_directories(self.path, self.structure)


    def meth_create_files(self, structure=True):
        for key, value in self.files.items():
            for k in value:
                if structure:
                    tmp_key = f"00_{key}"
                    path_tmp = f"{self.structure[tmp_key]}\{k}.{key}"
                else:
                    path_tmp = f"{self.path}\{k}.{key}"
                self.files[key][k] = path_tmp
                if not os.path.exists(path_tmp):
                    with open(path_tmp, 'w'): pass


if __name__ == "__main__":
    # value
    path_00 = r"C:\Users\kekes\OneDrive\Desktop\delete\00_prepare"
    path_01 = r"C:\Users\kekes\OneDrive\Desktop\delete\01_prepare"
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
    prep_00 = Prepare(path_00, structure, files)
    prep_00.meth_delete_directories()
    prep_00.meth_create_directories()
    prep_00.meth_create_files()
    print(json.dumps(prep_00.structure, indent=4))
    print(json.dumps(prep_00.files, indent=4))

    prep_01 = Prepare(path_01, structure, files)
    prep_01.meth_delete_directories()
    prep_01.meth_create_directories()
    prep_01.meth_create_files(structure=False)
    print(json.dumps(prep_01.structure, indent=4))
    print(json.dumps(prep_01.files, indent=4))
