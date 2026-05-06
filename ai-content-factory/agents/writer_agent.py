from utils.llm import call_llm

def write_content(topic):
    prompt = f"""
根据以下选题写一篇短内容：

选题：{topic}
"""
    return call_llm(prompt)
