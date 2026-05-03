from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def classify_question(question, topics):
    q_embedding = model.encode(question, convert_to_tensor=True)
    topic_embeddings = model.encode(topics, convert_to_tensor=True)

    scores = util.cos_sim(q_embedding, topic_embeddings)
    best_match = topics[scores.argmax()]

    return best_match