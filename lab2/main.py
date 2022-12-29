import sys
from create_index import create_index
from cui import search_menu
from utils.file_utils import get_all_files_from_dir, check_dir_path


def search_engine():
    index = {}
    file_titles = {}

    args = sys.argv[1:]
    directory = args[0]

    if check_dir_path(directory) == 1:
        return 1

    files = get_all_files_from_dir(directory)
    create_index(files, index, file_titles)

    if len(args) == 2 and args[1] == '-s':
        search_menu(index, file_titles)
    else:
        print(f'index: {index} \ntitles: {file_titles}')


if __name__ == '__main__':
    search_engine()
