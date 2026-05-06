from agents.topic_agent import generate_topics
from agents.writer_agent import write_content
from agents.seo_agent import optimize_seo
from agents.review_agent import review_content

def run_pipeline(niche="AI创业", batch_size=5):
    topics = generate_topics(niche, batch_size)
    results = []

    for topic in topics:
        topic = topic.strip()
        if not topic:
            continue

        content = write_content(topic)
        seo = optimize_seo(content)
        review = review_content(content)

        results.append({
            "topic": topic,
            "content": content,
            "seo": seo,
            "review": review
        })

    return results
