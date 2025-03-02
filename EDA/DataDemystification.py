from helpers.FileReader import read
from helpers.config import (get_all_file_path,
                            data_path)

path_log = get_all_file_path(base_path=data_path)

df_cities = read(path=path_log['Cities'])



