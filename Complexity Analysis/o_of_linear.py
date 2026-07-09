def papers_names(papers, name):
    for paper in papers:
        if paper == name:
            return True
    return False

papers = ["paper1", "paper2", "paper3"]

search_name = "paper2"

result = papers_names(papers, search_name)

if result == True:
    print(f"{search_name} is in the list of papers.")
else:
    print(f"{search_name} is not in the list of papers.")