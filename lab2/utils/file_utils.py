import os

data_dir = './mocks/'


def get_lists_of_letters():
    lists_file_data = get_file_data(data_dir + "lists.txt")
    data_into_strings = lists_file_data.split(",")
    data_into_lists = list(map(lambda line: list(filter(None, line.split(" "))), data_into_strings))

    return data_into_lists


def get_file_data(filename):
    lists_file = open(filename, "r")
    data = lists_file.read()
    lists_file.close()
    return data


def get_all_files_from_dir(dir_path):
    files = []

    for filename in os.listdir(dir_path):
        if filename.endswith('.txt'):
            files.append(os.path.join(dir_path, filename))

    return files


def check_dir_path(dir_path):
    if not os.path.exists(dir_path):
        return 1
