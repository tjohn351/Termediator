from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

docs = [
"do not",
"don't"
]

tfidf_vectorizer = TfidfVectorizer()

tfidf_matrix = tfidf_vectorizer.fit_transform(docs)
matrix = cosine_similarity(tfidf_matrix[0:len(docs)], tfidf_matrix)

print matrix


# http://www.cs.duke.edu/courses/spring14/compsci290/assignments/lab02.html
# http://text-processing.com/demo/tokenize/