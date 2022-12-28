from utils.data_utils import get_file_title, stem_term
from utils.file_utils import get_file_data


def create_index(filenames, index, file_titles):
    for filename in filenames:

        file_content = get_file_data(filename)
        file_titles[filename] = get_file_title(file_content)

        terms_raw = file_content.split()
        for term_raw in terms_raw:
            stemmed_term = stem_term(term_raw)

            if not (stemmed_term in index):
                index[stemmed_term] = []
            if filename not in index[stemmed_term]:
                index[stemmed_term].append(filename)

    return 0
