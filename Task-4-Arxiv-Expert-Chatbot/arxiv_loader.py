import json
import pandas as pd

def load_arxiv_data(file_path, max_papers=5000):

    papers = []

    with open(file_path, "r", encoding="utf-8") as f:

        for i, line in enumerate(f):

            if i >= max_papers:
                break

            paper = json.loads(line)

            categories = paper.get("categories", "")

            # Only Computer Science papers
            if "cs." in categories:

                papers.append({
                    "title": paper.get("title", ""),
                    "abstract": paper.get("abstract", ""),
                    "authors": paper.get("authors", ""),
                    "categories": categories
                })

    df = pd.DataFrame(papers)

    print("Total CS Papers:", len(df))

    return df
if __name__ == "__main__":

    df = load_arxiv_data(
        "dataset/arxiv-metadata-oai-snapshot.json"
    )

    print(df.head())