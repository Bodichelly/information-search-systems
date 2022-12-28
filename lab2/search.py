from common_elements import common as get_common
from utils.data_utils import stem_term


def search(index, query):
    terms_raw = query.split()

    if not len(terms_raw):
        return []

    res = None
    for term_raw in terms_raw:
        stemmed_term = stem_term(term_raw)

        if stemmed_term in index.keys():
            term_files = index[stemmed_term]
        else:
            term_files = []

        if res is None:
            res = term_files
            continue

        res = get_common(res, term_files)
        if not len(res):
            break

    return res
