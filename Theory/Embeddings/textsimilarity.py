from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')  # Small and efficient model = Sentence-BERT

def compute_similarity(text1, text2):
    embeddings = model.encode([text1, text2])
    similarity_score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return similarity_score

text1 = "Artificial intelligence."
text2 = "Deep Learning."

similarity = compute_similarity(text1, text2)
print(f"Similarity Score: {similarity:.2f}")

