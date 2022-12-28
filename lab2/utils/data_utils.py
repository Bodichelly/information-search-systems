import string
from nltk.stem import PorterStemmer

ps = PorterStemmer()


def get_file_title(file_content):
    return file_content.split('\n')[0]


def stem_term(term):
    strip_term = term.strip(string.punctuation)
    return ps.stem(strip_term.lower())
