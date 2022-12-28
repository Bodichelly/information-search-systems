from lab1.models.helpers.str_utils import clear_word
from lab1.models.indexes.basicIndex import BasicIndex


class ForwardIndex(BasicIndex):
    def index_files(self, files_data):
        for file in files_data:
            name, text = file
            self.indexes[name] = set(map(clear_word, text.split(' ')))

    def search(self, query):
        if not self.indexes:
            raise ValueError("Empty indexes")
        result = []
        for index in self.indexes.keys():
            if query.lower() in self.indexes[index]:
                result.append(index)
        if len(result) == 0:
            return None
        return result
