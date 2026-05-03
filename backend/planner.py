def generate_plan(topics):
    plan = []
    days = 7

    topics_list = list(topics.keys())

    for i, topic in enumerate(topics_list):
        plan.append(f"Day {i+1}: Study {topic}")

    return plan