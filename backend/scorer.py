def score_topics(freq):
    scores = {}
    for topic, count in freq.items():
        scores[topic] = count * 1.0  # simple scoring
    return dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))