from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ArxivChatbot:

    def __init__(self, df):

        self.df = df

        self.vectorizer = TfidfVectorizer(
            stop_words="english"
        )

        self.tfidf_matrix = self.vectorizer.fit_transform(
            df["abstract"].fillna("")
        )

    def search(self, query, top_k=5):

        query_vector = self.vectorizer.transform(
            [query]
        )

        similarity = cosine_similarity(
            query_vector,
            self.tfidf_matrix
        )[0]

        top_indices = similarity.argsort()[-top_k:][::-1]

        return self.df.iloc[top_indices]