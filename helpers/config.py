import os
import pathlib

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
data_path = os.path.abspath(os.path.join(root_path,'Data'))

def get_all_file_path(base_path):
    """

    :param path:
    :return:
    """

    path_log = {}
    for file in os.listdir(path=base_path):
        path_log[file.split('.')[0]] = os.path.abspath(os.path.join(base_path,file))

    return path_log



if __name__ == '__main__':

    path_log = get_all_file_path(base_path=data_path)
    print(path_log)
