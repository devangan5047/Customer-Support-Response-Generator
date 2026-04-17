import json
from rank_bm25 import BM25Okapi
from app.utils.text_preprocessing import preprocess
from app.config import TOP_K

class BM25Service:
    def __init__(self, filepath):
        with open(filepath, "r") as f:
            self.documents = json.load(f)

        self.corpus = [preprocess(doc["content"]) for doc in self.documents]
        self.bm25 = BM25Okapi(self.corpus)

    def retrieve(self, query):
        tokenized_query = preprocess(query)
        scores = self.bm25.get_scores(tokenized_query)

        ranked = sorted(
            list(enumerate(scores)),
            key=lambda x: x[1],
            reverse=True
        )

        top_docs = []
        for idx, score in ranked[:TOP_K]:
            doc = self.documents[idx]
            doc["score"] = score
            top_docs.append(doc)

        return top_docs