"""Text similarity using sentence embeddings and cosine similarity."""
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Small and efficient model (Sentence-BERT)
model = SentenceTransformer('all-MiniLM-L6-v2')


def compute_similarity(text1, text2):
    """Compute cosine similarity between two text strings."""
    embeddings = model.encode([text1, text2])
    similarity_score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return similarity_score


text1 = "Artificial intelligence."
text2 = "Deep Learning."

similarity = compute_similarity(text1, text2)
print(f"Similarity Score: {similarity:.2f}")
