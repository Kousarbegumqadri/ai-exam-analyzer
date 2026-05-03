from sentence_transformers import SentenceTransformer, util

print("Loading model...")   # 👈 debug

model = SentenceTransformer('all-MiniLM-L6-v2')

topics = [
    "Computer Networks",
    "DBMS",
    "Operating Systems",
    "Data Structures",
    "Algorithms"
]

def classify_question(question):
    print("Classifying:", question)   # 👈 debug
    
    q_embedding = model.encode(question, convert_to_tensor=True)
    topic_embeddings = model.encode(topics, convert_to_tensor=True)

    scores = util.cos_sim(q_embedding, topic_embeddings)
    best_match = topics[scores.argmax()]

    print("Predicted:", best_match)   # 👈 debug
    return best_match