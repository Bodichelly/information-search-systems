from os import listdir
from os.path import isfile, join

default_path = "files"


def get_file_names(path=default_path):
    return [f for f in listdir(path) if isfile(join(path, f))]


def get_files_data(file_names, path=default_path):
    data_list = []
    for data in file_names:
        data_list.append(read_text_file(path + "\\" + data))
    return data_list


def load_files_data(path=default_path):
    file_names = get_file_names(path)
    return list(zip(file_names, get_files_data(file_names, path)))


def read_text_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()
