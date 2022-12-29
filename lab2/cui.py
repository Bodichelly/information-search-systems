from search import search


def search_menu(index, file_titles):
    while True:
        query = input("Enter search query (or 'ENTER' to exit): ")
        if query == '':
            break
        results = search(index, query)

        if len(results):
            print(f"Query results '{query}':\n")
            for i in range(len(results)):
                title = file_titles[results[i]]
                print(f"title: '{title}'\n\t file: '{results[i]}'\n")
        else:
            print(f"No query results '{query}':")

        print('\n\n')

