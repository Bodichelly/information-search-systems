from utils.file_utils import get_lists_of_letters


def common(list1, list2):
    return list(set([x for x in list1 if x in list2]))


def run_common():
    lists = get_lists_of_letters()
    lists_1 = lists[::2]
    lists_2 = lists[1::2]
    for i in range(len(lists_1)):
        print(f"list 1: {lists_1[i]}, list 2: {lists_2[i]}, result: {common(lists_1[i], lists_2[i])} \n")
